#!usr/local/env python3.5
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
from collections import Counter
import operator
import sys


def read_file(inputfile):

	with open(inputfile) as f:

		return f.read()

def ignored_words():

	with open('ignored_words.txt') as f:

		tokenizer = RegexpTokenizer(r'\w+')
		content = tokenizer.tokenize(f.read())
		return content

def file_to_list(inputfile):

	text = read_file(inputfile)
	tokenizer = RegexpTokenizer(r'\w+')
	content = tokenizer.tokenize(text)
	words = [word.lower() for word in content]

	return words

def word_count(inputfile):

	word_dict = {}
	words = file_to_list(inputfile)

	for word in set(words):

		if word in ignored_words():

			continue

		else:

			word_dict[word] = words.count(word)

	return word_dict

def count_words(inputfile):

	word_dict = word_count(inputfile)

	return top_20(word_dict)

def top_20(word_dict):

	top_20_words = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)[:20]

	return top_20_words


count_words(sys.argv[-1])

###########Ignore###########

'''def histgram(top_20_words):

	with open('histogram.txt', 'w') as f:

		columns = 80
		n_occurrences = 10
		labels, values = zip(*top_20_words)
		label_width = max(map(len, labels))
		data_width = columns - label_width - 1
		plot_format = '{:%d}|{:%d}' % (label_width, data_width)
		max_value = float(max(values))

		for i in range(len(labels)):

			v = int(values[i]/max_value*data_width)
			return (f.write(plot_format.format(labels[i], '#'*v)))'''