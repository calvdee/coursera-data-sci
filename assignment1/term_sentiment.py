<<<<<<< HEAD
"""
Coursera 2013 - Introduction to Data Science Assignment1

Calculates the sentiment score for terms in Tweets that are not already
in the AFINN.txt sentiment score file.  The equation to calculate a 
sentiment score was derived from 
http://www.cs.cmu.edu/~rbalasub/publications/oconnor_balasubramanyan_routledge_smith.icwsm2010.tweets_to_polls.pdf.
"""

import sys
import json
import re

class SentimentScore(object):
	"""
	Class to provide an interface to a dictionary of sentiment scores.
	Loads the sentiment file and performs query against a dictionary
	mapping terms to sentiment scores. 
	"""
	_lookup = None

	def __init__(self, sent_file):
		if SentimentScore._lookup is None:
			SentimentScore._lookup = self._build_lookup(sent_file)

	def _build_lookup(self, sent_file):
		"""
		Creates a single instance of the sentiment score lookup.
		"""
		scores = {}
		for line in sent_file:
		  term, score  = line.split("\t")
		  scores[term] = int(score)

		return scores

	def get_score(self, term):
		"""
		Returns the score for the term or 0 if it's not in the lookup. 
		"""
		return self._lookup.get(term, 0)

def load_tweets(fp):
	"""
	Creates in-memory JSON objects from file ``fp``.
	"""

	lst = []

	line = fp.readline()
	while len(line) is not 0:
		data = json.loads(line.strip())
		lst.append(data)
		line = fp.readline()

	return lst

def parse_tweets(tweets):
	"""
	Parses a list of tweets, splitting the value of the ``text`` property
	into tokens based on a regular expression.
	"""
	pattern = re.compile(r'\w+')
	parsed = []
	for t in tweets:
		if 'text' not in t.keys():
			continue

		# Obtain a list of words
		words = pattern.findall(t['text'])
		parsed.append(words)

	return parsed

def hw(sent_file, tweet_file):
	tweets = load_tweets(tweet_file)		# Twitter status objects
	parsed = parse_tweets(tweets)				# The statuses parsed into list of terms
	scores = SentimentScore(sent_file)	# Dictionary of sentiment scores
	
	# A dicitionary to store words with no sentiment score
	zero = {}

	for tweet in parsed:
		"""
		1. Iterate over the words and count (1)+ve sentimate (2)-ve sentiment.
		2. If a word is -ve add it to the local zero dict.
		3. Assign all keys in ``zero_local`` the +ve/-ve ratio.
		"""
		pos, neg = (0, 0)
		zero_local = []
		for word in tweet:
			value = scores.get_score(word)
			if value < 0: neg = neg + 1
			elif value > 0: pos = pos + 1
			else: zero_local.append(word)

		ratio = float(pos)/neg if neg is not 0 else pos 
		
		for t in zero_local:
			zero[t] = zero[t] + ratio if t in zero.keys() else ratio

	for k, v in zero.items():
		print "%s %s" % (k, v)
		
def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])

	hw(sent_file, tweet_file)

	sent_file.close()
	tweet_file.close()
=======
import sys

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)
>>>>>>> aa9293c028291670bb27ec44281d282a85aeef74

if __name__ == '__main__':
    main()
