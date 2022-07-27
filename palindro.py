'''
String Challenge
Have the function StringChallenge(str) take the str parameter being passed 
and return the string true if the parameter is a palindrome, 
(the string is the same forward as it is backward) otherwise return the string false.
The parameter entered may have punctuation and symbols but they should not affect 
whether the string is in fact a palindrome. 
For example: "Anne, I vote more cars race Rome-to-Vienna" should return true.
'''
import re

def is_palindrome(word: str) -> bool:
	# remove any non letter character in word
	new_word = re.sub('\W', '', word).lower()
	if new_word == new_word[::-1]:
		status = True
	else:
		status = False
	return status

def main() -> None:
	words_list = [
		"Anne, I vote more cars race Rome-to-Vienna",
		"Ah. Satan sees Natasha.",
		"Anne, I vote more cars race Rome to Vienna.",
		"Trug Tim eine so helle Hose nie mit Gurt?",
		'La ruta natural.',
	]

	for word in words_list:
		if (response := is_palindrome(word)):
			print(f"{word} - is a palindrome")

if __name__ == "__main__":
	main()