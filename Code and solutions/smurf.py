

import random




def draw():
	return random.randint(1, 36)
	
	
def spent_money():
	collection = []
	total_sum = 0
	while len(collection) < 36:
		total_sum += 10
		smurf = draw()
		if smurf not in collection:
			collection.append(smurf)
	collection.sort()
	print(len(collection))
	return total_sum
	
	
	
if __name__ == '__main__':
	print(spent_money())
