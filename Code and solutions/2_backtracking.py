




#Felix Bittmann, 2020


def posfinder(position, path, deadend, size):
	"""Finding all available squares for the knight"""
	posfields = []
	for a, b in [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
		(1, -2), (1, 2), (2, -1), (2, 1)]:
		a += position[0]
		b += position[1]
		if 0 <= a <= size - 1 and 0 <= b <= size - 1:
		# Position is within the chessboard
			if (a, b) not in path and (path + [(a, b)]) not in deadend:
				posfields.append((a, b))
	return posfields
	
	
def knight(size=5):
	startpos = (0, 0)
	path = [startpos]
	deadend = []
	iteration = 1
	while len(path) < size ** 2:
		iteration += 1
		# Generate all further moves:
		moves = posfinder(path[-1], path, deadend, size)
		if moves:
			path.append(moves[0])
		elif path == [startpos]:
			raise ValueError("Cannot be solved")
		else:
			#Backtrack when in deadend:
			deadend.append(path)
			path = path[:-1]
	print("Iterations:", iteration)
	print(path)
	print([b * size + a for a, b in path])



if __name__ == '__main__':
	print(knight())



########################################################################
### Task 1 ###
########################################################################
	
def npos(position, path, size):
	"""How many options are for a given position"""
	npos = 0
	for a in (-2, -1, 1, 2):
		for b in (-2, -1, 1, 2):
			if abs(a) == abs(b):
				continue
			if (0 <= position[0] + a <= (size - 1) and 0 <= position[1] + b <= (size - 1) and
				(position[0] + a, position[1] + b) not in path):
					npos += 1
	return npos


def springer_problem2(size):
	startpos = (0, 0)
	path = [startpos]
	deadend = []
	iteration = 1
	while len(path) < size ** 2:
		iteration += 1
		# Find all possible moves:
		moves = posfinder(path[-1], path, deadend, size)
		if moves:
			moves2 = [(move, npos(move, path, size)) for move in moves]
			moves2.sort(key=lambda x: x[1])
			path.append(moves2[0][0])
		elif path == [startpos]:
			raise ValueError("Cannot solve the field")
		else:
			#Backtrack if deadend:
			deadend.append(path)
			path = path[:-1]
	print("Iterations:", iteration)
	print(path)
	print([b * size + a for a, b in path])

print(springer_problem2(6))

########################################################################
### Task 2 ###
########################################################################
#See 2_Sudoku.py
