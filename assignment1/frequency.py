"""
Coursera 2013 - Introduction to Data Science Assignment1

Parses Tweet objects (https://dev.twitter.com/docs/platform-objects/tweets) 
obtained for Twitter's streaming API, sample endpoint and displays the
frequency for every word that appears in the tweets.

"""
import sys
import json
import re

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

def print_frequency(tweet_file):
	"""
	Prints the frequency of words (word counts) for all tweets in
	the tweet file.
	"""
	tweets = load_tweets(tweet_file)
	parsed = parse_tweets(tweets)

	terms = {}
	for words in parsed:
		for w in words:
			terms[w] = terms[w]+1 if w in terms.keys() else 1

	freq_all = sum([v for (k,v) in terms.items()])
	freqs = map(lambda (k,v): { k: float(v)/freq_all }, terms.items())
	
	for d in freqs:
		print "%s %s" % (d.items()[0])

def main():
    tweet_file = open(sys.argv[1])

    print_frequency(tweet_file)

    tweet_file.close()

if __name__ == '__main__':
    main()