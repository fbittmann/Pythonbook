



#Felix Bittmann, 2020


def primegenerator(n=2):
	"""Creates consecutive prime numbers larger or equal to n"""
	if n <= 2:
		yield 2
		n = 3
	if n % 2 == 0:
		n += 1
	
	while True:
		for divisor in range(3, int(n ** 0.5 + 1), 2):
			if n % divisor == 0:
				break
		else:			#break never reached
			yield n
		n += 2
		

if __name__ == '__main__':		
	primes = primegenerator()
	for i in range(5):
		print(next(primes))


	import itertools
	primes = primegenerator()
	print(list(itertools.islice(primes, 100, 120)))




########################################################################
### Task 1 ###
########################################################################

t = primegenerator()
res= [next(t) for i in range(5000)]
print(res[:20])


########################################################################
### Task 2 ###
########################################################################
"""Only twins and triplets"""

twins = 0
for i in range(0, len(res) - 1):
	if res[i] + 2 == res[i + 1]:
		twins += 1
print("Total twins:", twins)


"""Triplets have the form (p, p+2, p+6), see
https://en.wikipedia.org/wiki/Prime_triplet"""
triplets = 0
for i in range(0, len(res) - 2):
	if res[i] + 2 == res[i + 1] and res[i] + 6 == res[i + 2]:
		triplets += 1
print("Total triplets:", triplets)



########################################################################
### Task 3 ###
########################################################################
"""Our procedure for finding a semi-prim number is two-step.
First we have to factorize the number and then test whether both factors are prime numbers.
If this is the case, we have to check whether these two divisors are prime numbers each.
Then a semi-prim number is found, otherwise not"""


def primtest(n):
	"""Test whether n is prime"""
	if n % 2 == 0:
		return False
	for i in range(3, int(n**0.5 + 1), 2):
		if n % i == 0:
			return False
	else:
		return True

def semiprime(n):
	"""Test whether n is semiprime"""
	selection = []
	for i in range(2, n // 2):
		if n % i == 0:
			j = n // i
			selection.append([i, j])
	for i, j in selection:
		print(i, j)
		if primtest(i) and primtest(j):
			return True
		else:
			return False

print(semiprime(35))
print(semiprime(91))
