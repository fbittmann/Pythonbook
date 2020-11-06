

#Felix Bittmann, 2020

import copy


def subcheck(data, rowsec, colsec):
	"""Are the numbers from 1-9 unique in a 3x3 subsection?"""
	subsec = []
	for row in range(3 * rowsec, 3 * rowsec + 3):
		for col in range(3 * colsec, 3 * colsec + 3):
			subsec.append(data[row][col])
	for i in range(1, 10):
		if i not in subsec:
			return False
	return True
	

def subpos(data, row, col):
	"""Finds possible numbers for each 3x3 subsection of the matrix"""
	#Zuordnung der Eingabe nach Block
	lookup = ([0,1,2], [3,4,5], [6,7,8])
	for x in range(3):
		if row in lookup[x]:
			rowsec = x
	for y in range(3):
		if col in lookup[y]:
			colsec = y
	subsec = []
	for row in range(3 * rowsec, 3 * rowsec + 3):
		for col in range(3 * colsec, 3 * colsec + 3):
			subsec.append(data[row][col])
	possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	for i in range(1, 10):
		if i in subsec:
			possible.remove(i)
	return possible


def printer(data):
	"""Displays the matrix"""
	print("Matrix")
	for element in data:
		print(element)


def spaltengen(data, col):
	"""Gets a column from the matrix"""
	neuspalte = []
	for row in data:
		neuspalte.append(row[col])
	return neuspalte
	

def all_filled(data):
	"""Is every field filled with a number?"""
	for row in data:
		if 0 in row:
			return False
	return True
	
	
def gewonnen(data):
	"""Tests if the game is won"""
	#Zeilentest
	for row in data:
		for x in range(1, 10):
			if x in row:
				continue
			else:
				return False
	#Spaltentest
	for y in range(0, 9):
		for i in range(1, 10):
			if i in spaltengen(data, y):
				continue
			else:
				return False
	
	#Sektionetest
	for x in range(3):
		for y in range(3):
			if subcheck(data, x, y) == False:
				return False
	return True


def posfinder(data, row, col, deadends):
	"""Which numbers are still possible for a field?"""
	zeilenpos = []
	for i in range(1,10):
		if i not in data[row]:
			zeilenpos.append(i)
	spaltenpos = []
	tempspalte = spaltengen(data, col)
	for i in range(1,10):
		if i not in tempspalte:
			spaltenpos.append(i)
	pos = []
	for i in range(1,10):
		if i in zeilenpos and i in spaltenpos:
			pos.append(i)
	
	pos2 = []	
	subpossibles = subpos(data, row, col)
	if subpossibles == [] or pos == []:
		return []
	else:
		for x in range(1,10):
			if x in pos and x in subpossibles:
				pos2.append(x)
	
	finalpos = []
	for element in pos2:
		tempdaten = copy.deepcopy(data)
		tempdaten[row][col] = element
		if tempdaten not in deadends:
			finalpos.append(element)
	return finalpos


def findempty(data):
	"""Finding the next empty field in a matrix"""
	for row in range(0,9):
		for col in range(0,9):
			if data[row][col] == 0:
				return (row, col)
				
				
def solver(data):
	"""Using backtracking to solve a sudoku"""
	path = [data]
	deadends = []
	while True:
		currentfield = copy.deepcopy(path[-1])
		#Test auf Lösung
		if all_filled(currentfield) == True and gewonnen(currentfield) == True:
			break
		
		nextfield = findempty(currentfield)
		posnumbers = posfinder(currentfield, nextfield[0], nextfield[1], deadends)
		#~ print(nextfield, posnumbers)
		
		if len(path) == 1 and posnumbers == []:
			raise ValueError("Sudoku cannot be solved!")
		
		#Backtrack wenn fail
		if posnumbers == []:
			assert currentfield not in deadends
			deadends.append(currentfield)
			path = path[:-1]
			continue
		else:
			currentfield[nextfield[0]][nextfield[1]] = posnumbers[0]
			path.append(currentfield)
			continue
	print("Solved!")
	printer(path[-1])
	
	
if __name__ == '__main__':
	example = [[0,0,5,0,0,8,0,9,4],
				[8,0,0,0,0,0,2,0,5],
				[0,0,0,9,5,3,0,0,0],
				[0,5,0,0,0,7,6,0,9],
				[0,0,0,2,3,6,0,0,0],
				[2,0,6,5,0,0,0,4,0],
				[0,0,0,8,7,1,0,0,0],
				[5,0,1,0,0,0,0,0,8],
				[6,8,0,4,0,0,1,0,0]]
	solver(example)
	
	
