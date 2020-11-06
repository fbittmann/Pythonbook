




#Felix Bittmann, 2020


def chaosformula(x, r, n, prec):
	for i in range(n):
		print(round(x, prec))
		x = x * r * (1 - x)
		
		
def logistic(x, r):
	while True:
		yield x
		x = x * r * (1 - x)
		
	
from itertools import islice
def cyclefinder(x, r):
	numbers = logistic(x, r)
	# skip first million iterators
	numbers = islice(numbers, 10**6, None)
	seen = {}
	for iteration, x in enumerate(numbers):
		for element in seen:
			if abs(element - x) < 1e-6:
				return iteration - seen[element]
		seen[x] = iteration
		
		
def find_discontinuity(x, r1, precision=4):
	p1 = cyclefinder(x, r1)
	stepsize = 0.1
	while stepsize > 0.1 ** precision:
		r2 = r1 +  stepsize
		print(r1, r2)
		p2 = cyclefinder(x, r2)
		if p1 == p2:
			r1 = r2
		else:
			stepsize /= 2
	return round((r1 + r2) / 2, precision)
	
if __name__ == '__main__':	
	print(find_discontinuity(0.5, 2.7))
	print(find_discontinuity(0.5, 3.1))
