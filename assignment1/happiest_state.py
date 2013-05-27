"""
Coursera 2013 - Introduction to Data Science Assignment1

Analyzes tweets and determines the 'hapiest state' by calculating the 
summed sentiment score for words in all Tweets that came from a specific state.
"""

import time
import sys
import json
import re

state_mapping = { 
	"alabama": "al",
	"alaska": "ak",
	"arizona": "az",
	"arkansas": "ar",
	"california": "ca",
	"colorado": "co",
	"connecticut": "ct",
	"delaware": "de",
	"florida": "fl",
	"georgia": "ga",
	"hawaii": "hi",
	"idaho": "id",
	"illinois": "il",
	"indiana": "in",
	"iowa": "ia",
	"kansas": "ks",
	"kentucky": "ky",
	"louisiana": "la",
	"maine": "me",
	"maryland": "md",
	"massachusetts": "ma",
	"michigan": "mi",
	"minnesota": "mn",
	"mississippi": "ms",
	"missouri": "mo",
	"montana": "mt",
	"nebraska": "ne",
	"nevada": "nv",
	"new hampshire": "nh",
	"new jersey": "nj",
	"new mexico": "nm",
	"new york": "ny",
	"north carolina": "nc",
	"north dakota": "nd",
	"ohio": "oh",
	"oklahoma": "ok",
	"oregon": "or",
	"pennsylvania": "pa",
	"rhode island": "ri",
	"south carolina": "sc",
	"south dakota": "sd",
	"tennessee": "tn",
	"texas": "tx",
	"utah": "ut",
	"vermont": "vt",
	"virginia": "va",
	"washington": "wa",
	"west virginia": "wv",
	"wisconsin": "wi",
	"wyoming": "wy" }

token_regex = re.compile(r'\w+')
abbr_state_regex = re.compile(r'\w{2}')

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

def parse_tweet(tweet):
	"""
	Parses a list of tweets, splitting the ``text`` of the tweet into tokens 
	based on a regular expression.  If there is no ``text`` property then
	an empty list is returned.
	"""
	
	if 'text' not in tweet.keys():
		return []

	# Obtain a list of words
	return token_regex.findall(tweet['text'])

def parse_user_loc(tweet, abbr_states):
	"""
	Checks for both state abbreviations (from set ``abbr_states``) and full
	names of states in the User ``location`` property.  

	Returns empty list if no full state name or abbreviation is found.
	"""
	tokens = token_regex.findall(tweet['user']['location'])
	abbr_state = filter(lambda t: t in abbr_states, tokens)
	
	if not len(abbr_state) is 0:
		# Found a state abbreviation, return it.
		return abbr_state[0]

	# Check for full state names
	states = filter(lambda t: t in state_mapping.keys(), tokens)

	if not len(states) is 0:
		# Found a full state, return the abbreviation
		state = states[0]
		return state_mapping[state]

	return None

def print_happy_state(sent_file, tweet_file):
	"""
	Given a file with sentiment scores and a file containing tweets separated
	by a newline, parses the tweets into JSON objects and determines which
	state had words that accumulated the highest sentiment score and is therefore
	the `happiest state`.
	"""
	# Sentiment scores
	scores = SentimentScore(sent_file)

	# Filtered tweets (deleted tweets removed)
	tweets = filter(lambda t: 'delete' not in t.keys(), load_tweets(tweet_file))

	# A list of 2-character abbreviated state names
	abbr_states = set(map(lambda (k,v): v, state_mapping.items()))

	# State scores as a dictionary from state abbreviations
	state_scores = dict.fromkeys(abbr_states, 0)

	# Filter all the tweets that have a location property set on them
	state_tweets = filter(
		lambda t: 'place' in t.keys() \
			and t['place'] is not None \
			and t['place']['name'].lower() in state_mapping.keys(), tweets)

	# Set of ID's that have a valid state in place['name']
	state_tweet_ids = set(map(lambda t: t['id'], state_tweets))

	# Figure out the rest of the tweets to analyze using user['location']
	rest_tweets = filter(lambda t: t['id'] not in state_tweet_ids, tweets)

	if len(state_tweets) > 0:
		rest_tweets.extend(state_tweets)

	for t in rest_tweets:
		text =  parse_tweet(t)
		if len(text) is 0:
			# No text in tweet, skip
			continue
		
		# Sum the scores of words in the tweet's text
		score = sum([scores.get_score(w) for w in text])

		if t['id'] in state_tweet_ids:
			# At this point, there will be a corresponding entry in the state mapping
			# for this state.
			state = t['place']['name'].lower()
			key = state_mapping[state]
		else:
			# Try and get a location from the tweet, if it's not None then
			# it's a valid state so do something otherwise continue
			key = parse_user_loc(t, abbr_states)
			if key is None: 
				continue

		# The key will be a valid state, add to it's total
		state_scores[key] = state_scores[key] + score

	sent_max = 0
	happy_state = ""
	for (k,v) in state_scores.items():
		if v > sent_max:
			sent_max = v
			happy_state = k

	print happy_state.upper()

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    print_happy_state(sent_file, tweet_file)

    sent_file.close()
    tweet_file.close()

if __name__ == '__main__':
    main()