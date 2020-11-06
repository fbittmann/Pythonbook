


#Felix Bittmann, 2020


def countdown1(n, counter=0, sequence=""):
	if n == 1:
		return (counter, sequence)
	counter += 1
	results = []
	if n % 2 == 0:
		results.append(countdown1(n // 2, counter, sequence + "2"))
	if n % 3 == 0:
		results.append(countdown1(n // 3, counter, sequence + "3"))
	results.append(countdown1(n - 1, counter, sequence + "1"))
	return min(results)
	
	
#Uncomment to run code
# ~ import time
# ~ for k in range(20, 320, 20):
	# ~ tstart = time.monotonic()
	# ~ print(k, countdown1(k), round(time.monotonic() - tstart, 3))



def countdown2(n):
	book = {1: (0, "")}
	def inner(n):
		if n in book:
			return book[n]
		results = []
		if n % 2 == 0:
			counter, sequence = inner(n // 2)
			results.append((counter + 1, "2" + sequence))
		if n % 3 == 0:
			counter, sequence = inner(n // 3)
			results.append((counter + 1, "3" + sequence))
		counter, sequence = inner(n - 1)
		results.append((counter + 1, "1" + sequence))
		book[n] = min(results)
		return book[n]
	return inner(n)


#Uncomment to run code	
# ~ if __name__ == '__main__':	
	# ~ import time
	# ~ for k in range(20, 320, 20):
		# ~ tstart = time.monotonic()
		# ~ print(k, countdown2(k), round(time.monotonic() - tstart, 3))
		
		
		
		
	# ~ import sys
	# ~ sys.setrecursionlimit(8888)
	# ~ tstart = time.monotonic()
	# ~ for i in (500, 2000, 5000):
		# ~ print(i, countdown2(i))
	# ~ print(time.monotonic() - tstart)



	# ~ import cProfile
	# ~ cProfile.run("countdown1(30)")
	# ~ cProfile.run("countdown2(30)")
	
	
	
########################################################################
### Task 1 ###
########################################################################
"""Solving the task without recursion. The idea is simply to generate
ALL numbers and pick out the ones of interest. Brute force, but works"""

def countdown_norec(n):
	storage = {1: (0, "")}
	for number in range(2, n + 1):
		a = b = (9**9, "")
		if number % 2 == 0:
			res = storage[number // 2]
			a = (res[0] + 1, "2" + res[1])
		if number % 3 == 0:
			res = storage[number // 3]
			b = (res[0] + 1, "3" + res[1])
		res = storage[number - 1]
		c = (res[0] + 1, "1" + res[1])
		storage[number] = min(a, b, c)
	return storage[n]

print(countdown_norec(43))
