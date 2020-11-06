


#Felix Bittmann, 2020


import random

def game(goal):
	income = 20
	r = 0
	balance = 0
	machines = []
	while balance < goal:
		r += 1
		balance += income + r
		interest = sum(0.05 if r - t <= 10 else 0.03 for t in machines)
		balance += balance * interest
		price = 50 * 2 ** len(machines)
		if balance >= price and len(machines) < 5:
			machines.append(r)
			balance -= price
	return r, machines


def game2(best, goal):
	income = 20
	r = 0
	balance = 0
	machines = []
	while balance < goal:
		if r >= best:
			return None
		r += 1
		balance += income + r
		interest = sum(0.05 if r - t <= 10 else 0.03 for t in machines)
		balance += balance * interest
		price = 50 * 2 ** len(machines)
		if balance >= price and len(machines) < 5 and random.randint(0, 1) == 1:
			machines.append(r)
			balance -= price
	return r,  machines
	
	
def simulation(n):
	best = 999
	for i in range(n):
		output = game2(best, 5000)
		if output:
			best, machines = output
	return best, machines


if __name__ == '__main__':
	print(game(5000))
	print(simulation(10 ** 5))
	
	
	
########################################################################
### Task 1 ###
########################################################################

def computer1(p_fail):
	start = p_fail
	chips = 0
	time = 0
	while time < 168:
		if random.random() < p_fail:
			time += 6
			p_fail = start
		else:
			chips += 1
			p_fail += 0.002
			time += 1
	return chips
	
	
def sim1(p_fail, reps):
	"""How many chips are produced on average?"""
	return sum(computer1(p_fail) for i in range(reps)) / reps
	
"""Baseline with failrate 0.05"""	
print(sim1(0.05, 9000))
		
		
		
########################################################################
### Task 2 ###
########################################################################

def sim2():
	for p in range(10, 60, 2):		#Von 1% zu 6% in Schritten von 0,2%
		print("Basline-Failrate:", p / 1000)
		print(round(sim1(p / 1000, 9000), 2))
		print("******************************************")
		

"""Max. failrate for 120 chips per week?"""		
sim2()
