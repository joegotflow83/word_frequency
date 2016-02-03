#!usr/local/env python3.5
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
import operator
import sys



def read_file():

	with open() as f:

		return f.read()

def count_words(inputfile):

	with open(inputfile) as f:

		word_dict = {}
		tokenizer = RegexpTokenizer(r'\w+')
		content = tokenizer.tokenize(f.read())
		words = [word.lower() for word in content]

	for word in set(words):

		if word in ignored_words():

			continue

		else:

			word_dict[word] = words.count(word)

	return top_20(word_dict)

def top_20(word_dict):

	top_20_words = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)[:20]

	print(top_20_words)

def ignored_words():

	with open('ignored_words.txt') as f:

		tokenizer = RegexpTokenizer(r'\w+')
		content = tokenizer.tokenize(f.read())
		return content

count_words(sys.argv[-1])