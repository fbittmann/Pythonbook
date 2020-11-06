


#Felix Bittmann, 2020


import time
import random
def game_of_life(rounds):
	grid = [
		[random.random() < 0.10 for x in range(50)]
		for y in range(18)
	]
	for i in range(rounds):
		draw_grid(grid)
		grid = update_grid(grid)
		time.sleep(0.6)
		
		
def update_grid(grid):
	new_grid = []
	for y, row in enumerate(grid):
		new_row = []
		for x, cell in enumerate(row):
			neighbors = count_neighbors((x,y), grid)
			if cell and neighbors == 2:
				cell = True
			elif neighbors == 3:
				cell = True
			else:
				cell = False
			new_row.append(cell)
		new_grid.append(new_row)
	return new_grid
	
	
def count_neighbors(position, grid):
	neighbors = 0
	for x in (-1, 0, 1):
		for y in (-1, 0, 1):
			if x == y == 0:
				continue
			xpos, ypos = position[0] + x, position[1] + y
			if 0 <= xpos < len(grid[0]) and 0 <= ypos < len(grid):
				neighbors += grid[ypos][xpos]
	return neighbors
	
	
def draw_grid(grid):
	for row in grid:
		print("".join("#" if cell else " " for cell in row))
	print("#" * len(row))
	
	
game_of_life(30)



########################################################################
### Task 1 ###
########################################################################
#https://de.wikipedia.org/wiki/Conways_Spiel_des_Lebens#Raumschiffe_und_Gleiter


def glider(position, grid):
	output = grid[:]
	xpos, ypos = position
	try:
		output[ypos][xpos] = 1
		output[ypos][xpos + 1] = 1
		output[ypos][xpos + 2] = 1
		output[ypos - 1][xpos] = 0
		output[ypos - 1][xpos + 1] = 0
		output[ypos - 1][xpos + 2] = 1
		output[ypos - 2][xpos] = 0
		output[ypos - 2][xpos + 1] = 1
		output[ypos - 2][xpos + 2] = 0
	except IndexError:
		return grid
	return output


def game_of_life2(r):
	grid = [
		[False for x in range(50)]
		for y in range(18)
	]
	grid = glider((5, 5), grid)
	for i in range(r):
		draw_grid(grid)
		grid = update_grid(grid)
		time.sleep(0.4)
		
# ~ game_of_life2(20)
