



with open("wordlist.txt", encoding="utf-8") as newfile:  
	data = newfile.readlines()
	print(len(data))
	print(data[:20])
	print(list(data[5]))
	

	words = [line.rstrip().lower() for line in data]
	words = [word.replace("'", "") for word in words]
	print(words[:5])
	longwords = [word for word in words if len(word) > 2]
	
	longwords.sort(key=len)
	print(longwords[0])
	print(longwords[-1])
	longwords.sort(key=lambda word: word[::-1])
	print(longwords[:20])


def counter(string, character):
	return sum (1 for element in string if element == character)
	
f = lambda word: sum(1 for character in word if character == "g")



longwords.sort(key=lambda wort: sum(1 for zeichen in wort if zeichen == "g"), reverse = True)
print(longwords[:3])



########################################################################
### Task 1 ###
########################################################################

def is_palindrom(string):
	"""Is a string palindromic?"""
	return string == string[::-1]


########################################################################
### Task 2 ###
########################################################################


import random
def passgen(max_length, min_length, wordlist, n):
	"""Generates random passphrases"""
	
	allwords = []
	for i in range(n):
		pw = []
		while True:
			length = sum(len(x) for x in pw)
			if min_length <= length <= max_length:
				break
			elif length > max_length:
				pw.pop(-1)
				#Here we include a failsafe
				#if we are too long
				if sum(len(x) for x in pw) + 3 > max_length:
					pw.pop(-1)
			else:
				pw.append(random.choice(wordlist))
		allwords.append("".join(pw))
	for element in allwords:
		print(element)		

# ~ passgen(26, 20, words, 20)


########################################################################
### Aufgabe 3 ###
########################################################################

def diversity(word):
	"""Wir berechnen die Diversitaet als die Anzahl der einmalig enthaltenen
	Buchstaben, was wir recht simpel mit einem Dict loesen"""
	histogramm = {}
	for char in word.lower():
		if char not in histogramm:
			histogramm[char] = 1
		else:
			histogramm[char] += 1
	# ~ print(histogramm)
	unique = 0
	for value in histogramm.values():
		if value == 1:
			unique += 1
	return unique / len(word)
	
	
print(diversity("Cobalamine"))


def tester(wordlist, minlength):
	"""Welche Woerter haben die hoechste Diversitaet?"""
	results = [(diversity(word), word) for word in wordlist if len(word) >= minlength]
	results.sort(reverse = True)
	print(results[:10])
	
# ~ tester(words, 6)
# ~ tester(words, 15)



########################################################################
### Task 4 ###
########################################################################
def anagramfinder(word, wordlist):
	def histogram(word):
		output = {}
		for char in word.lower():
			if char not in output:
				output[char] = 1
			else:
				output[char] += 1
		return output
	
	anagrams = []		
	for element in wordlist:
		if len(element) == len(word) and histogram(element) == histogram(word):
			anagrams.append(element)
	return anagrams
	
	
# ~ print(anagramfinder("renovate", words))
