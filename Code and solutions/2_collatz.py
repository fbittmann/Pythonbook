


#Felix Bittmann, 2020



def collatz1(n):
	while n > 1:
		if n % 2 == 0:
			n = n // 2
		else:
			n = (n * 3) + 1
	return True
	
	
	
def collatz2(n):
	seen = set()
	while True:
		if n == 1:
			return True
		elif n in seen:
			return False
		else:
			seen.add(n)
			if n % 2 == 0:
				n = n // 2
			else:
				n = (n * 3) + 1
				
				
				
print(collatz1(22))
print(collatz2(22))



########################################################################
### Task 1 ###
########################################################################

def collatz_counter(n):
	counter = 0
	while n > 1:
		if n % 2 == 0:
			n = n // 2
		else:
			n = (n * 3) + 1
		counter += 1
	return counter

print(collatz_counter(8))	
print(collatz_counter(100))


res = [(i, collatz_counter(i)) for i in range(2, 5001)]
res.sort(key = lambda x: x[1], reverse = True)
"""Longest sequence below 5000"""
print(res[0])


########################################################################
### Task 2 ###
########################################################################

def collatz3(n):
	"""We can stop as soon n is below this very high number (2**60) since all below are already tested"""
	while n > 87 * (2**60):
		if n % 2 == 0:
			n = n // 2
		else:
			n = (n * 3) + 1
	return True
	
print(collatz3((10**5500) - 87845834658388888888593694356934569435693441))
