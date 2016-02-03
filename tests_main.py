from nltk.tokenize import RegexpTokenizer
import unittest
import main
import os


SAMPLE = os.path.join(os.path.dirname(__file__), 'dummy.txt')


class MainTest(unittest.TestCase):

	maxDiff = None

	def setUp(self):

		self.testdata = open(SAMPLE).read()

	def tearDown(self):

		self.testdata = None

	# Test if able to read from file
	def test_readfile(self):

		self.assertTrue(main.read_file(SAMPLE) == self.testdata)

	# Test file text is changed to list of strings
	def test_file_to_list(self):

		tokenizer = RegexpTokenizer(r'\w+')
		content = tokenizer.tokenize(self.testdata)
		words = [word.lower() for word in content]
		self.assertEqual(main.file_to_list(SAMPLE), words)

	# Test word and count are put into dict
	'''def test_word_and_count_to_dict(self):

		word_dict = {}
		words = main.file_to_list(SAMPLE)
		ignore_words = ['a', 'this', 'for', 'we', 'it']
		
		for word in set(words):
			
			if word in ignore_words:

				continue

			else:

				word_dict[word] = words.count(word)

		self.assertEqual(main.word_count(SAMPLE), word_dict)'''