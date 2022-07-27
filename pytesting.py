from palindro import is_palindrome

def test_user_can_check_single_words_for_palindrome():
	word = 'dolod'
	assert isinstance(is_palindrome(word), bool)

def test_user_gets_true_for_correct_palindrome():
	word = 'Amore, Roma.'
	assert is_palindrome(word) is True

def test_user_gets_false_for_incorrect_palindrome():
	word = 'jargony=ie'
	assert is_palindrome(word) is False

def test_user_can_check_multiple_words_for_palindromes():
	words_list = [
		"Anne, I vote more cars race Rome-to-Vienna",
		"Ah. Satan sees Natasha.",
		"Anne, I vote more cars race Rome to Vienna.",
		"Trug Tim eine so helle Hose nie mit Gurt?",
		'La ruta natural.',
	]

	for word in words_list:
		assert is_palindrome(word) is True