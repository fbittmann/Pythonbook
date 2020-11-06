



#Felix Bittmann, 2020



import random


def pi2(n):
	inside = 0
	for i in range(n):
		x, y = random.random(), random.random()
		distance = (x ** 2 + y ** 2) ** 0.5
		if distance <= 1:
			inside += 1
	return 4 * (inside / n)
	
	
print(pi2(10**6))
print(pi2(10**7))




#Appendix



random.seed(123)
print(random.random())

random.seed(123)
print(random.random())


print([random.randrange(50, 100, 5) for i in range(10)])

data = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
print(random.choice(data))
print(random.sample(data, k=5))
print(random.choices(data, k=5))



########################################################################
### Task 1 ###
########################################################################

import math
import statistics as stats

def pitester():
	referenz = str(math.pi)
	for prez in (2, 3, 4, 5, 6, 7):
		correct = []
		for r in range(50):
			res = str(pi2(10 ** prez))
			counter = 0
			for i in range(len(res)):
				if referenz[i] == res[i]:
					counter += 1
				else:
					break
		correct.append(counter)
		print("Digits:", 10**prez)
		print("Correct on average:", stats.mean(correct))


"""Comment in to test since this takes some time"""		
# ~ pitester()	


########################################################################
### Task 2 ###
########################################################################


def monty(change):
	"""The idea here is this: the game master is guaranteed to open a door with
	a goat and you are guaranteed to switch. If you have chosen a goat in the beginning,
	you are guaranteed to win. Conversely, if you have chosen a goat in the first choice,
	you will have a goat afterwards. So here we only turn the selections around."""
	stage = [0, 0, 1]		#Two goats, one loss
	random.shuffle(stage)
	select1 = random.randint(0, 2)
	if change == False:
		if stage[select1] == 1:
			return True
		else:
			return False
	else:
		if stage[select1] == 1:	#First win, now loss
			return False
		else:
			return True			#First loss, now win
		
		
def simulation(n):
	win_change = sum([monty(change = True) for i in range(n)]) / n
	win_nochange = sum([monty(change = False) for i in range(n)]) / n

	print("Odds to win with change:", win_change)
	print("Odds to win when keeping the first guess:", win_nochange)
	
"""Comment in to run"""		
# ~ simulation(5000)


########################################################################
### Task 3 ###
########################################################################
import math
def birthday_formula(n):
	"""What is the probability that n people in a group have at least 2 birthdays on the same day?"""
	return 1 - (math.factorial(365) / (math.factorial(365 - n) * (365 ** n)))
	

def birthday_simulation(n, runs=5000):
	"""What is the probability that n people in a group have at least 2 birthdays on the same day?"""
	def doubledates(n):
		dates = random.choices(range(365), k=n)
		seen = set()
		for element in dates:
			if element not in seen:
				seen.add(element)
			else:
				return True
		return False
	
	ndoubles = sum(doubledates(n) for i in range(runs))
	return ndoubles / runs

"""Hier einkommentieren"""		
# ~ print(birthday_formula(25))
# ~ print(birthday_simulation(25))


########################################################################
### Task 4 ###
########################################################################
def lotto_simulation(numbers, runs):
	"""What is the average win after a certain number of lottery draws?
	The own numbers are given as a list where the last number stands for the extra_number"""
	assert len(numbers) == 7 and 0 <= numbers[-1] <= 9
	drawn = range(1, 50)	#1-49
	extra_number = range(0, 10)	#0-9
	quota = {(2, 1): 5, (3, 0): 10, (3, 1): 20, (4, 0): 42, (4, 1): 109,
		(5, 0): 3340, (5, 1): 10022, (6, 0): 574596, (6, 1): 8949642}
	winnings = 0
	for i in range(runs):
		z1 = list(random.sample(drawn, k=6))
		z2 = random.choice(extra_number)
		correct = sum(1 for zahl in numbers[:-1] if zahl in z1)
		if numbers[-1] == z2:
			correct_extra_number = 1
		else:
			correct_extra_number = 0
		if (correct, correct_extra_number) in quota:
			winnings += quota[(correct, correct_extra_number)]
	return winnings - (1.5 * runs)		#Ein Spiel kostet 1,50
	
# ~ print(lotto_simulation([22, 47, 3, 5, 30, 11, 6], 52 * 50))

