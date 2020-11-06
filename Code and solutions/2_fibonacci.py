


#Felix Bittmann, 2020


def fibonacci(n):
	assert n > 0
	a, b  = 1, 1
	for i in range(n):
		print(a)
		a, b = b, a + b
		

def fibonacci2(n):
	elements = [1, 1]
	for i in range(n):
		elements.append(elements[-1] + elements[-2])
	return elements[:-2]	
	
	
def fibonacci3(n):
	elements = {1:1, 2:1}
	def inner(n):
		if n not in elements:
			next_element = inner(n-1) + inner(n-2)
			elements[n] = next_element
		return elements[n]			
	return inner(n)


#Appendix
def fac(n):
	print("Computing the factorial of:", n)
	if n == 1:				#Base Case
		print("Return: ", 1)
		return 1
	else:					#calling itself
		result = n * fac(n - 1)
		print("Return: ", result)
		return result		


if __name__ == '__main__':
	fibonacci(10)
	print(fibonacci2(10))
	print(fibonacci3(10))
	fac(6)
	
	
######################################################################
# Assignments #
######################################################################

########################################################################
### Task 2 ###
########################################################################
"""The problem with this formula is that the accuracy of the results depends
on the decimal places that are included in the analyses. If the numbers become
too large, the decimal places are "lost" and the results become wrong.
Let's look at an example of the problem."""

def binet(i):
	"""Create the ith Fibonacci number with the formula by Moivre-Binet"""
	return int((1 / (5**0.5)) * (((1 + 5**0.5) / 2)**i - ((1 - 5**0.5) / 2)**i))
	
a = fibonacci2(2000)
n1 = 10
print(binet(n1 + 1), a[n1])
#Results match

n2 = 1000
print(binet(n2 + 1) == a[n2])
#Results do not match any longer
	

"""To understand it, we pick a term from the equation and look at it in detail.
For example we see that root(5) occurs three times in total. But this number is
irrational now, so it has infinitely many decimal places. So for a detailed result
we first have to provide this number with many decimal places and then calculate it.
Otherwise we will get wrong results for large numbers. A conversion is possible in different
ways. Here you can see that the formula "nothing is given to you". Whether you want to have a
lot of decimal places or simply add up all the previous terms is up to you

"""
	

########################################################################
### Task 3 ###
########################################################################
import time

tstart = time.time()
x1 = fibonacci2(500)
tend = time.time()
print("Without recursion:")
print(round(tend - tstart, 4))


tstart = time.time()
x2 = [fibonacci3(i + 1) for i in range(500)]
tend = time.time()
print("With recursion:")
print(round(tend - tstart, 4))
assert x1 == x2 
	
########################################################################
### Task 4 ###
########################################################################
golden = (1 + 5 ** 0.5) / 2
elements = fibonacci2(10 ** 5)
for n in (1, 2, 3, 4, 5):
	empratio = elements[(10 ** n) - 1] / elements[(10 ** n) - 2]
	deviation = abs(golden / empratio)
	print(n, empratio, deviation)
#Wie erkennbar wird, reichen bereits 100 Zahlen aus, um eine sehr gute Näherung zu erhalten

########################################################################
### Task 5 ###
########################################################################	
#Total sum of all reciprocals der ersten 5000 Glieder
elements = fibonacci2(5000)
total = 0
for element in elements:
	total += 1 / element 
print("Sum of the reciprocals:", total)

########################################################################
### Task 6 ###
########################################################################
def zeckendorf(n):
	"""Splits a natural number n into one or more Fibonacci numbers,
	whereby directly consecutive Fibonacci numbers may not occur"""
	numbers = fibonacci2(n + 1)
	numbers.sort(reverse=True)
	result = ""
	skip = False
	for pos, number in enumerate(numbers):
		if skip:
			skip = False
			continue
		if number <= n and n - number >= 0:
			n -= number
			result += str(len(numbers) - pos)
			skip = True
		if n == 0:
			return result
			
print(zeckendorf(19))			
	

	
########################################################################
### Task 7 ###
########################################################################


"""The trick is to use a default, which can be ignored at the first call,
but then always explicitly set the Dict with the stored values
carries along"""

def fibonacci4(n, elements = None):
	if elements == None:
		elements = {1:1, 2:1}
	if n in elements:
		return elements[n]
	else:
		nextelement = fibonacci4(n-1, elements) + fibonacci4(n-2, elements)
		elements[n] = nextelement
		return nextelement
		
print(fibonacci4(10))
