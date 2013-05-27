"""
Template for writing a MapReduce job.
"""

import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
