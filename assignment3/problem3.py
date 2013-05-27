"""
Problem 3

Consider a simple social network dataset consisting of key-value pairs 
where each key is a person and each value is a friend of that person. 
Describe a MapReduce algorithm to count he number of friends each person has.
"""

import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
	person = record[0]
	mr.emit_intermediate(person, 1)

def reducer(key, list_of_values):
	mr.emit((key, sum(list_of_values)))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
