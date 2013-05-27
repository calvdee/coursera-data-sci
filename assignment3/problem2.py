"""
Problem 2

Implement a relational join as a MapReduce query

SELECT * 
FROM Orders, LineItem 
WHERE Order.order_id = LineItem.order_id
"""

import MapReduce
import sys
import itertools

mr = MapReduce.MapReduce()

def mapper(record):
    key = record[1]

    # Emit the join key (key => order_id) and all the fields for
    # an arbitrary relation that contains the join key field.
    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
	order = list_of_values[0]				# Order will be the first set of fields
	line_items = list_of_values[1:]	# Line items will be the remaining sets of fields

	# Emit an extended list 
	for l in line_items:
		mr.emit(order + l)

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
