<<<<<<< HEAD
import time
import sys
import json
import re
import numpy


class SentimentScore(object):
	_lookup = None

	def __init__(self, sent_file):
		if SentimentScore._lookup is None:
			SentimentScore._lookup = self._build_lookup(sent_file)

	def _build_lookup(self, sent_file):
		scores = {} # initialize an empty dictionary
		for line in sent_file:
		  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		  scores[term] = int(score)  # Convert the score to an integer.

		return scores

	def get_score(self, word):
		return self._lookup.get(word, 0)


def load_tweets(fp):
	"""
	Creates in-memory JSON objects from a tweet file ``fp``.
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
	Parses a list of tweets, splitting the ``text`` of the tweet
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

def print_senitments(sent_file, tweet_file):
	tweets = load_tweets(tweet_file)
	scores = SentimentScore(sent_file)
	parsed = parse_tweets(tweets)

	sums = []
	with Timer() as t:
		for word_list in parsed:
			# Sum the scores
			tweet_scores = [scores.get_score(w) for w in word_list]
			summed = sum(tweet_scores)
			sums.append(summed)

		print "tweet_count: %s" % len(tweets)
		print "sum: %s" % str(sum(sums))
		print "mean: %f" % numpy.mean(sums)
			
	print "elapsed compute time: %f" % (t.msecs/1000.0)
=======
import sys

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))
>>>>>>> aa9293c028291670bb27ec44281d282a85aeef74

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
<<<<<<< HEAD

    print_senitments(sent_file, tweet_file)

    sent_file.close()
    tweet_file.close()
=======
    hw()
    lines(sent_file)
    lines(tweet_file)
>>>>>>> aa9293c028291670bb27ec44281d282a85aeef74

if __name__ == '__main__':
    main()
