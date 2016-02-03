#!usr/local/env python3.5
from nltk import word_tokenize


with open('sample.txt', 'r') as f:

	#print(f.read())
	pass

word_dict ={}

with open('sample.txt') as f:

	tokens = word_tokenize(f.read())
	words = [w.lower() for w in tokens]
	words = sorted(words)

for word in set(words):

	word_dict[word] = words.count(word)

print(word_dict)