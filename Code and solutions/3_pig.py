

#Felix Bittmann, 2020



import random
def randomplay(mytotal, yourtotal):
	roundtotal = 0
	while True:
		if random.randint(0, 1) == 1:
			z = random.randint(1, 6)
			if z == 1:
				return 1
			else:
				roundtotal += z
		else:
			return max(1, roundtotal)
			
			
def greedy(mytotal, yourtotal):
	roundtotal = 0
	while roundtotal + mytotal < 100:
		z = random.randint(1, 6)
		if z == 1:
			return 1
		else:
			roundtotal += z
	return roundtotal
	
	
def get20(mytotal, yourtotal):
	roundtotal = 0
	while roundtotal < 20 and mytotal + roundtotal < 100:
		z = random.randint(1, 6)
		if z == 1:
			return 1
		else:
			roundtotal += z
	return roundtotal
	
	
def risky(mytotal, yourtotal):
	roundtotal = 0
	if 80 <= yourtotal < 100:
		while mytotal + roundtotal < 100:
			z = random.randint(1, 6)
			if z == 1:
				return 1
			else:
				roundtotal += z
		return roundtotal
	else:
		while roundtotal < 20 and mytotal + roundtotal < 100:
			z = random.randint(1, 6)
			if z == 1:
				return 1
			else:
				roundtotal += z
		return roundtotal
		
		
def strategyfinder(wintotal=100):
	def wincheck(i, j, k):
		if (i, j, k) in probability:
			# Probability is already available
			return probability[i, j, k]
		
		if i + k >= wintotal:
			# win is sure
			return 1
		elif j >= wintotal:
			# loss is sure
			return 0
		
		# Probability when rolling the die
		p_roll = 1 - wincheck(j , i + 1, 0)
		for points in range(2, 7):
			p_roll += wincheck(i, j, k + points)
		p_roll /= 6
		# When saving probability that j wins
		p_hold = 1 - wincheck(j, i + max(k, 1), 0)
		# which option is better
		p_best = max(p_roll, p_hold)
		if p_roll > p_hold:
			recommendation[i, j, k] = "roll"
		else:
			recommendation[i, j, k] = "hold"
		probability[i, j, k] = p_best
		return p_best
	probability = {}
	recommendation = {}
	wincheck(0, 0, 0)
	return (probability, recommendation)
	
	
def optimal(mytotal, yourtotal):
	roundtotal = 0
	while True:
		if mytotal + roundtotal >= 100:
			return roundtotal
		res = (mytotal, yourtotal, roundtotal)
		if database[1][res] == "hold":
			return roundtotal
		z = random.randint(1, 6)
		if z == 1:
			return 1
		else:
			roundtotal += z
			
			
from itertools import product
def tournament(strategies, rounds):
	global database
	database = strategyfinder()
	history = {}
	for self in strategies:
		history[self] = {}
		for opponent in strategies:
			if self != opponent:
				history[self][opponent] = 0
	for strat0, strat1 in product(strategies, strategies):
		if strat0 != strat1:
			for r in range(rounds):
				p0, p1 = 0, 0
				while True:
					p0 += strat0(p0, p1)
					if p0 >= 100:
						history[strat0][strat1] += 1
						break
					p1 += strat1(p1, p0)
					if p1 >= 100:
						history[strat1][strat0] += 1
						break
	for self in history:
		print(self.__name__)
		for opponent in history[self]:
			winchance = 100 * history[self][opponent] / (rounds * 2)
			print(opponent.__name__, round(winchance, 1))
		print("_" * 15)


if __name__ == '__main__':
	random.seed(1234)
	tournament((randomplay, greedy, get20, risky, optimal), 5000)
