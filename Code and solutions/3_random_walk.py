



#Felix Bittmann, 2020


import time
import math
import random

def randomwalk(steps):
	position = (0, 0)
	for i in range(steps):
		angle = random.random() * 360
		xpos = position[0] + math.cos(math.radians(angle))
		ypos = position[1] + math.sin(math.radians(angle))
		position = (xpos, ypos)
	return position
	
	
	
def random_pos(position, nrows, ncolumns):
	while True:
		angle = random.random() * 360
		xpos = position[0] + math.sin(math.radians(angle))
		ypos = position[1] + math.cos(math.radians(angle))
		position = (xpos, ypos)
		gridpos = postogrid(position, nrows, ncolumns)
		if 0 <= gridpos[1] <= nrows - 1 and 0 <= gridpos[0] <= ncolumns - 1:
			return position
			
			
def postogrid(position, nrows, ncolumns):
	xpos, ypos = position	#tuple unpacking
	columnpos = int(xpos + ncolumns / 2)
	rowpos = int(-ypos + nrows / 2)
	return (columnpos, rowpos)
	
	
	
def display_grid(particles, nrows, ncolumns):
	screen = [[" "] * ncolumns for i in range(nrows)]
	for element in particles:
		xgrid, ygrid = postogrid(element, nrows, ncolumns)
		screen[ygrid][xgrid] = "*"
	print("#" * (ncolumns + 2))
	for row in screen:
		print(f"#{''.join(row)}#")
	print("#" * (ncolumns + 2))
	
	
	
FPS = 10
def main(n, nrows=18, ncolumns=50):
	particles = [(0, 0)] * n
	while True:
		particles = [
			random_pos(p, nrows, ncolumns)
			for p in particles
		]
		print("")
		display_grid(particles, nrows, ncolumns)
		time.sleep(1 / FPS)
		
		
# ~ main(5)	#Comment in to run code


########################################################################
### Task 1 ###
########################################################################
"""If you are using radians the values can only be from 0 to 2 Pi (2*3.141)"""

def randomwalk2(steps):
	position = (0, 0)
	for i in range(steps):
		r = random.random() * 6.283185
		xpos = position[0] + math.cos(r)
		ypos = position[1] + math.sin(r)
		position = (xpos, ypos)
	return position


########################################################################
### Task 2 ###
########################################################################

"""Different symbols"""


def display2(partikel, n_zeilen, n_spalten):
	screen = [[" "] * n_spalten for _ in range(n_zeilen)]
	for element in partikel:
		xgrid, ygrid = postogrid(element[0], n_zeilen, n_spalten)
		screen[ygrid][xgrid] = element[1]
	print("#" * (n_spalten + 2))
	for zeile in screen:
		print(f"#{''.join(zeile)}#")
	print("#" * (n_spalten + 2))
	
		
FPS = 10
def main2(n, n_zeilen=18, n_spalten=50):
	symbols = ["*", "#", "@", "+", "o"]
	partikel = [((0, 0), random.choice(symbols)) for i in range(n)]
	while True:
		partikel = [[random_pos(p[0], n_zeilen, n_spalten), p[1]] for p in partikel]	
		display2(partikel, n_zeilen, n_spalten)
		time.sleep(1 / FPS)

# ~ main2(5)


########################################################################
### Task 3 ###
########################################################################


FPS = 10
def main3(n, n_zeilen=18, n_spalten=50):
	symbols = ["*", "#", "@", "+", "o"]
	partikel = [((random.randint(0, n_spalten), random.randint(0, n_zeilen)), random.choice(symbols)) for i in range(n)]
	while True:
		partikel = [[random_pos(p[0], n_zeilen, n_spalten), p[1]] for p in partikel]	
		display2(partikel, n_zeilen, n_spalten)
		time.sleep(1 / FPS)
		
# ~ main3(10)
