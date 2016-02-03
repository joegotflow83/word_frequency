#!usr/local/env python3.5
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
import operator


def read_file():

	with open('sample.txt', 'r') as f:

		return f.read()

def count_words():	

	with open('sample.txt') as f:

		word_dict = {}
		tokenizer = RegexpTokenizer(r'\w+')
		content = tokenizer.tokenize(f.read())
		words = [word.lower() for word in content]
		words = sorted(words)

	for word in set(words):

		word_dict[word] = words.count(word)

	return top_20(word_dict)

def top_20(word_dict):

	top_20_words = dict(sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)[:20])

	print(top_20_words)

count_words()