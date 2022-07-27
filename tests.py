import unittest

from palindro import is_palindrome

class PalindromeTest(unittest.TestCase):
	def test_can_check_single_word_palindrome(self):
		# jon inputs a word into the function 
		# the function returns a boolean 
		result = is_palindrome(word='dolod') 
		self.assertIsInstance(result, bool)

	def test_can_check_multiple_palindrome(self):
		# jon has a list of palindrome phrases 
		words_list = [
			"Anne, I vote more cars race Rome-to-Vienna",
			"Ah. Satan sees Natasha.",
			"Anne, I vote more cars race Rome to Vienna.",
			"Trug Tim eine so helle Hose nie mit Gurt?",
			'La ruta natural.',
		]

		# jon checks each word, one after the other
		for word in words_list:
			result = is_palindrome(words_list[0])
			self.assertIsInstance(result, bool)

unittest.main()