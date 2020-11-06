



#Felix Bittmann, 2020


class Sheep:
	def __init__(self):
		self.position = [random.random() * SIZE, random.random() * SIZE]
		self.hunger = 0
		self.pregnant = 0
		self.age = 0
		
		
	def move(self):
		while True :
			x = self.position[0] + random.random() * 4 - 2
			y = self.position[1] + random.random() * 4 - 2
			if 0 <= x < SIZE and 0 <= y < SIZE:
				break
		self.position = (x, y)
		
		
	def eat(self, grass):
		xpos, ypos = map(int, self.position)
		if grass[xpos, ypos] == 2:
			self.hunger = 0
			grass[xpos, ypos] = 0
			
			
	def distance(self, other):
		xdiff = self.position[0] - other.position[0]
		ydiff = self.position[1] - other.position[1]
		return (xdiff ** 2 + ydiff ** 2) ** 0.5
		
		
	def alive(self):
		return self.age < 20 and self.hunger < 3


	def horny(self):
		return self.pregnant == 0 and self.hunger == 0
		
		
def display_statistics(allsheep, round):
	hunger = pregnant = grass =	age = 0
	for sheep in allsheep:
		hunger += sheep.hunger
		age += sheep.age
		if sheep.pregnant > 1:
			pregnant += 1
	print("Round: ", round)
	print("Total number of sheep: ", len(allsheep))
	print(f"Average hunger: {hunger / len(allsheep):.2f}")
	print(f"Average age: {age / len(allsheep):.2f}")
	print("Pregnant: ", pregnant)
	print("#" * 40)
	
	
	
import time
import random
from itertools import combinations
SIZE = 10
def simulation(rounds):
	grass = {(x, y): 2 for x in range(SIZE) for y in range(SIZE)}
	allsheep = [Sheep() for i in range(10)]
	for round in range(rounds):
		# Grass is growing
		for pos in grass:
			if grass[pos] < 2:
				grass[pos] += 1
		random.shuffle(allsheep)
		
		# Move and eat
		lambs = 0
		for sheep in allsheep:
			sheep.age += 1
			sheep.hunger += 1
			sheep.move()
			sheep.eat(grass)
			if sheep.pregnant == 8:
				sheep.pregnant = 0
				lambs += 1
			elif sheep.pregnant > 0:
				sheep.pregnant += 1
		allsheep.extend(Sheep() for i in range(lambs))
		display_statistics(allsheep, round)
		
		# Mating
		horny_sheep = [sheep for sheep in allsheep if sheep.horny()]
		tired_sheep = set()
		for sheep, partner in combinations(horny_sheep, 2):
			if sheep in tired_sheep or partner in tired_sheep:
				pass
			elif sheep.distance(partner) <= 1:
				sheep.pregnant = 1
				tired_sheep.update([sheep, partner])
		
		# Death
		allsheep = [sheep for sheep in allsheep if sheep.alive()]
		if not allsheep:
			break
		time.sleep(0.7)
		
		
# ~ simulation(30)


########################################################################
### Task 1 ###
########################################################################
import itertools
class Person:
	def __init__(self):
		self.position = (random.random() * SIZE, random.random() * SIZE)
		self.status = 0			#Healthy (0), infected (1), immune (2)
		self.infect_status = 0	#Current stage of infection
		
		
				
	def move(self):
		"""Persons can move one meter"""
		while True :
			x = self.position[0] + random.random() * 2 - 1
			y = self.position[1] + random.random() * 2 - 1
			if 0 <= x < SIZE and 0 <= y < SIZE:
				break
		self.position = (x, y)
				
	def distance(self, other):
		"""Distance to other person"""
		return (
			(self.position[0] - other.position[0]) ** 2
			+ (self.position[1] - other.position[1]) ** 2
		) ** 0.5


def statistics(persons):
	n = len(persons)
	healthy, infected, immune = 0, 0, 0
	for p in persons:
		if p.status == 0:
			healthy +=1
		elif p.status == 1:
			infected += 1
		elif p.status == 2:
			immune += 1
	print(f"Alive: {n} | healthy: {healthy} | infected: {infected} | immune: {immune}")
		
		
def simulation(runden, npersons, infected):
	MORTALITY = 0.01			#Probability that an infected person dies on a given day
	CHANCE = 0.40			#Probability that an infected person infects another person when in contact
	persons = [Person() for i in range(npersons)]
	random.shuffle(persons)
	for i, p in enumerate(persons):
		if i < infected:
			p.status = 1
	
	for r in range(runden):
		#Moving
		for p in persons:
			p.move()
		
		#Infection:
		for p1, p2 in itertools.combinations(persons, 2):
			if p1.distance(p2) < 2 and (p1.status == 1 or p2.status == 1) and random.random() < CHANCE:
				# ~ print("INFECTION!")
				if p1.status == 0:
					p1.status = 1
				if p2.status == 0:
					p2.status = 1
					
		#Aging
		for p in persons:
			if p.status == 1:
				p.infect_status += 1
			if p.infect_status >= 10:
				p.status = 2
				
		#Dying
		survivors = []
		for p in persons:
			if p.status == 1 and random.random() < MORTALITY:
				#Person dies
				continue
			else:
				survivors.append(p)
		persons = survivors
		print(f"Round: {r + 1}")
		statistics(persons)
		if len(persons) == 0:
			break
		time.sleep(0.6)

SIZE = 15			
simulation(30, 20, 2)
