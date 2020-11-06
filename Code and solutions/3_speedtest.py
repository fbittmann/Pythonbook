



#Felix Bittmann, 2020



import time
import random
import statistics as stats



def speedtest(functions, n):
	assert isinstance(functions, list)
	times = {f: [] for f in functions}
	for run in range(n):
		random.shuffle(functions)
		for function in functions:
			start_time = time.monotonic()
			function()
			end_time = time.monotonic()
			times[function].append(end_time - start_time)
	for function, runtime in times.items():
		print(f"{function}: {stats.mean(runtime):.4f} | {stats.median(runtime):.4f}")




def count1():
	total = 0
	for i in range(500000):
		total += i
	return total 
	
	
def count2():
	return sum(i for i in range(500000))
	
	
print(count1(), count2())
speedtest([count1, count2], 50)


########################################################################
### Task 1 ###
########################################################################
"""To test this function we use both functions here. Both create a list with
the first 500.000 numbers. What is faster, a loop with while or a list-comprehension?"""


def whilecounter(n=50_000):
	output = []
	counter = 0
	while counter < n:
		output.append(counter)
		counter += 1
	return output
	
	
def comprehension(n=50_000):
	return [i for i in range(n)]
	
	

speedtest([whilecounter, comprehension], 25)

#As you see, the comprehension is much faster!




########################################################################
### Task 2 ###
########################################################################
"""Here we first define the decorator as a normal function.
We then attach it to the new function tester and see if everything works"""

def stopwatch(func, *args, **kwargs):
	def inner(*args, **kwargs):
		t_start = time.monotonic()
		res = func(*args, **kwargs)
		t_end = time.monotonic()
		runtime = round(t_end - t_start, 3)
		print(f"Runtime: {runtime}")
		return res
	return inner
	
"""Hier wird nun tester dekoriert und definiert"""	
@stopwatch	
def tester(n):
	time.sleep(0.5)
	return [i for i in range(n)]

print(tester(50))




########################################################################
### Task 3 ###
########################################################################
"""Use oartial from functools to deal with functions that need arguments"""

import functools
f1 = functools.partial(whilecounter, 50_000)
f2 = functools.partial(comprehension, 50_000)
speedtest([f1, f2], 25)
