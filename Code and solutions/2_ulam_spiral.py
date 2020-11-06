



#Felix Bittmann, 2020


def cart_to_matrix(position, size):
	"""Converts a position from the Cartesian system to the list-matrix"""
	column = (size // 2) + position[0]
	row = (size // 2) - position[1]
	return (row, column)
	
	
def next_position(data, position):
	empty = []
	# Positions bottom, right, top and left
	# Order is relevant so corners are treated correctly
	for x, y in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
		px, py = position[0] + x, position[1] + y
		pos = cart_to_matrix((px, py), len(data))
		if data[pos[0]][pos[1]] == "":
			empty.append((px, py, px ** 2 + py ** 2))
	return min(empty, key=lambda f: f[2])[:2]
	

def ulam(n):
	size = max(15, (int(n ** 0.5) // 2) * 2 + 11)
	data = [[""] * size for i in range(size)]
	i = cart_to_matrix((0, 0), size)
	data[i[0]][i[1]] = 1
	i = cart_to_matrix((0, 1), size)
	data[i[0]][i[1]] = 2
	position = (1, 1)
	for counter in range(3, n + 1):
		a = cart_to_matrix(position, size)
		data[a[0]][a[1]] = counter
		position = next_position(data, position)
	print_field(data)
	
	
def print_field(data):
	size = len(data)
	print("".join(["*" for i in range(size * 4)]))
	for row in data:
		for element in row:
			if element == "":
				print(" " * 4, end = "")	#Exactly 4 spaces
			else:
				print( f"{element:02d} ", end = "")	#Space before the f-string
		print("")
	print("".join(["*" for i in range(size * 4)]))
	
	
if __name__ == '__main__':	
	print(ulam(55))
