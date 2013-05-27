"""
Problem 5

Consider a set of key-value pairs where each key is sequence id and 
each value is a string of nucleotides, e.g., GCTTCCGAAATGCTCGAA....

Write a MapReduce query to remove the last 10 characters from each string 
of nucleotides, then remove any duplicates generated.
"""

import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    seq_id = record[0]
    nucleotide = record[1]

    # Trim the nucleotide
    trimmed = nucleotide[:len(nucleotide)-10]

    # Emit just the trimmed nucleotide so reducer will have unique values
    mr.emit_intermediate(trimmed, seq_id)

def reducer(key, list_of_values):   
		# Just emit the nucleotide.
    mr.emit(key)

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
