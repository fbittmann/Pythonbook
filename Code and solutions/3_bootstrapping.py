


#Felix Bittmann, 2020


import random
from statistics import mean, median, stdev

def histogram(data, bins=None):
	"""Draws a histogram from numerical data"""
	maxvalue = max(data)
	minvalue = min(data)
	totalwidth = abs(maxvalue - minvalue)
	ndata = len(data)
	if not bins:
		#Rice's rule or 20 bins max
		bins = int(min((2 * ndata**(1/3)), 20))
	binwidth = totalwidth / bins
	bindata = []
	maxelements = 0
	for i in range(bins):
		lowerbound =  minvalue + i * binwidth
		upperbound = lowerbound + binwidth
		nelements = sum(1 for element in data if lowerbound <= element < upperbound)
		if nelements > maxelements:
			maxelements = nelements
		midvalue = lowerbound + 0.5 * binwidth
		bindata.append([nelements, midvalue])
	
	maxheight = 25
	print("-" * 40)
	for row in bindata:
		binheight = int((maxheight / maxelements) * row[0])
		print(f"{row[1]: 4.2f}  {'#' * binheight}")
	print("-" * 40)
	print(f"N: {ndata}")
	print(f"Mean: {mean(data):4.02f}")
	print(f"Median: {median(data):4.02f}")
	print(f"Standard deviation: {stdev(data):4.02f}")


def bootstrap(func, data, n):
	empvalue = func(data)
	resamples = [func(random.choices(data, k=len(data))) for i in range(n)]
	stderr = stdev(resamples)
	ci = (round(empvalue - 1.96 * stderr, 2), round(empvalue + 1.96 * stderr, 2))
	histogram(resamples)
	print(f"Empirical value: {empvalue:4.02f} | Bootstrap Stderr: {stderr:4.02f} | 95%-CI: {ci}")
	
	
if __name__ == '__main__':
	random.seed(1234)
	data =  [round(random.normalvariate(0, 1), 3) for i in range(300)]
	histogram(data)
	
	
	# ~ testresults = [4, 5, 7, 7, 9, 10, 11, 13, 15, 18, 19, 19, 22, 23]
	# ~ bootstrap(median, testresults, 2000)
	
	
	
	
# Assignments

def spent_money():
	"""How much money must be spent until the collection is complete on average?"""
	collection = []
	total_sum = 0
	while len(collection) < 36:
		total_sum += 10
		smurf = random.randint(1, 36)
		if smurf not in collection:
			collection.append(smurf)
	return total_sum
	
	
# ~ simulation_smurfs = [spent_money() for i in range(9000)]
# ~ histogram(simulation_smurfs)

