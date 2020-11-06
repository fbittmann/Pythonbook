


#Felix Bittmann, 2020

def is_palindrome(string):
	if len(string) < 2:
		raise AssertionError("String must have at least 2 characters")
	return string == string[::-1]


def lps(string):
	pal_start = None
	pal_length = 1
	length = len(string)
	for startpos in range(length):
		for endpos in range(length, startpos + pal_length, -1):
			substring = string[startpos:endpos]
			print(substring)
			if is_palindrome(substring):
				pal_start = startpos
				pal_length = len(substring)
				break
	return pal_start, pal_length


if __name__ == '__main__':
	print(lps("TOTABBA"))



########################################################################
### Task 1 ###
########################################################################
import random
def randomgenes(length, n):
	alphabet = ("A", "T", "C", "G")
	allgenes = []
	for i in range(n):
		gene = "".join(random.choice(alphabet) for x in range(length))
		allgenes.append(gene)
	return allgenes
	
print(randomgenes(20, 5))


########################################################################
### Task 2 ###
########################################################################

def increasing(inputstr):
	for i in range(len(inputstr) - 1):
		if inputstr[i + 1] <= inputstr[i]:
			return False
	return True
		

def lis(inputstr):
	best = []
	for pos in range(len(inputstr)):
		for length in range(len(inputstr) - pos):
			part = inputstr[pos: pos + length + 1]
			if not increasing(part):
				break
			if increasing(part) and len(part) >= len(best):
				best = part
	return best
			
test = [1,1,1,1,2,3,4,5,3,3,3,1,2,3,4,5,6,7,8,4,4,5]
print(lis(test))
