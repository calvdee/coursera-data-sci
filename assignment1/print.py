"""
Coursera 2013 - Introduction to Data Science Assignment1

Calls Twitter's search API with a single query and prints the results
of that query.
"""

import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=fanshawe")

o = json.load(response)

results =  o['results']

for r in results:
	print r['text']