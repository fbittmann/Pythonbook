


#Felix Bittmann, 2020

import random

def is_palindrome(string):
	"""Tests whether a given string is a palindrome"""
	return string == string[::-1]


def rest(left, right):
	"""Finds the part of the construct that prohibits the formation of a palindrome"""
	left = "".join(left)
	right = "".join(right)
	return left[len(right):] or right[:-len(left)]


def wordfinder(wordlist, string, start, blocked):
	"""Finds a suitable match"""
	if start:
		for word in wordlist:
			if word.startswith(string) and word not in blocked:
				return word
	else:
		for word in wordlist:
			if word.endswith(string) and word not in blocked:
				return word
	return None			#no suitable match found
	

def main(minlength):
	with open("wordlist.txt", encoding="utf8") as data:
		wordlist = [row.strip().upper() for row in data]
		#wordlist = [word for word in wordlist if len(word) > 4]
	left =  ["A", "MAN", "A", "PLAN"]
	right = ["A", "CANAL", "PANAMA"]
	
	total = "".join(left) + "".join(right)
	blocked = set()
	last_right = False
	while len(total) < minlength or not is_palindrome(total):
		loose_end = rest(left, right)
		if loose_end == "":
			while True:
				newword = random.choice(wordlist)
				if newword not in blocked:
					break
		else:
			newword = wordfinder(wordlist, loose_end[::-1], last_right, blocked)
	
		if not newword:					#Backtrack
			if last_right:
				right.pop(0)
				last_right = False
			else:
				left.pop(-1)
				last_right = True
		else:
			blocked.add(newword)
			if last_right:
				left.append(newword)
				last_right = False
			else:
				right.insert(0, newword)
				last_right = True
	
		total = "".join(left) + "".join(right)
	
		print("Loose end: ", loose_end)
		print("New word: ", newword)
		print(left, right)
	assert is_palindrome(total)
	return total



if __name__ == '__main__':
	main(30)
