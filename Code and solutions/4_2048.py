



#Felix Bittmann, 2020


import random
import itertools

def combine(numbers):
	numbers = [z for z in numbers if z != 0]
	for z in range(0, len(numbers) - 1):
		if numbers[z] == numbers[z + 1]:
			numbers[z] = numbers[z] * 2
			numbers[z + 1] = 0
	numbers = [z for z in numbers if z != 0]
	return numbers + [0 for z in range(4 - len(numbers))]	
	
	
def update_grid(grid, direction):
	if direction == "left":
		grid = [combine(row) for row in grid]
	elif direction == "right":
		grid = [combine(row[::-1])[::-1] for row in grid]
	elif direction == "up":
		grid = [combine(row) for row in zip(*grid)]
		grid = [list(row) for row in zip(*grid)]
	elif direction == "down":
		grid = [combine(row[::-1])[::-1] for row in zip(*grid)]
		grid = [list(row) for row in zip(*grid)]
	return grid
	
	
def newnumber(grid):
	output = grid[:]		#Copy of the original grid
	columnpos = [0, 1, 2, 3]
	rowpos = [0, 1, 2, 3]
	random.shuffle(columnpos)
	random.shuffle(rowpos)
	for row in rowpos:
		for col in columnpos:
			if output[row][col] == 0:
				output[row][col] = 2
				return output
	return output
	
	
def game_won(grid):
	return any(512 in row for row in grid)
	
	
def display(grid, move, score):
	mapping = {0: "[  ]", 2: "[2^1]", 4: "[2^2]", 8: "[2^3]", 16: "[2^4]", 32: "[2^5]", 64: "[2^6]", 128: "[2^7]", 256: "[2^8]",
	512:"[2^9]"}
	for row in grid:
		for col in row:
			print(mapping[col], end= "")
		print("")
	print("================")
	print("Current move:", move)
	print("Score:", score)
	
	

KEYS = {
	"\x1b[D": "left",
	"\x1b[C": "right",
	"\x1b[A": "up",
	"\x1b[B": "down",
	}

def main():
	grid = [[0] * 4 for i in range(4)]
	grid [3][0] = 2
	grid [3][1] = 2
	for move in itertools.count(1):
		score = sum(sum(row) for row in grid)
		display(grid, move, score)
		if game_won(grid):
			break
		while True:
			userinput = input()
			if userinput in KEYS:
				break
			print("Input not valid! Only use arrow keys!")
		grid = update_grid(grid, KEYS[userinput])
		grid = newnumber(grid)
		for i in range(40):
			print()
	print("Game won!")
	
	
if __name__ == '__main__':
	main()
	
	
#######################################################################
### Task 1 ###
########################################################################

def is_game_lost(feld):
	"""We try all different moves. If they are not possible, the grid will
	not change. If the grid cannot change at all, the game must be lost"""
	for option in ("left", "right", "up", "down"):
		if grid != move(grid, option):
			return False
	return True
