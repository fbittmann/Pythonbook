



#Felix Bittmann, 2020


def norm(vector):
	"""Norm of a vector"""
	return sum(x ** 2 for x in vector) ** 0.5


def crossproduct(a, b):
	"""cross product of vectors a and b"""
	assert len(a) == len(b) == 3
	return [a[1] * b[2] - a[2] * b[1],
		a[2] * b[0] - a[0] * b[2],
		a[0] * b[1] - a[1] * b[0]]


def line_point_distance(line, point):
	"""Computes the distance between a line and a point.
	The line is entered as a tuple with support and direction. Support, 
	direction and point are given as lists with 3 elements.
	"""
	support, direction = line
	d = [s - p for s, p in zip(support, point)]
	return norm(crossproduct(d, direction)) / norm(direction)
	
	
def point_point_distance(x, y):
	"""Distance between two points in 2D"""
	assert len(x) == len(y) == 2
	return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5	
	
	
def norm_vector(vector):
	length = norm(vector)
	return [x / length for x in vector]


def falls_on_line(point_a, point_b, point_c, tolerance):
	"""Tests whether a b c lie on a line"""
	direction_ab = norm_vector([a - b for a, b in zip(point_a, point_b)])
	direction_bc = norm_vector([b - c for b, c in zip(point_b, point_c)])
	scalar_product = sum(x * y for x, y in zip(direction_ab, direction_bc))
	return 1 - abs(scalar_product) < tolerance
	
	
def compute_distance(vector, a, b, c):
	diagonal = ((0, 0, 0), (1, 1, 1)) # support and direction
	distances = [point_point_distance(vector, p) for p in (a, b, c)]
	distance = line_point_distance(diagonal, distances)
	return distance, distances, vector
	
	
def move_vector(vector, coordinate, movement):
	if coordinate == 0:
		return [vector[0] + movement, vector[1]]
	else:
		return [vector[0], vector[1] + movement]
		
		
import math
def circlefinder(a, b, c, tolerance=0.01, maxiter=10**5):
	if a == b or b == c or c==a:
		raise ValueError("Enter three distinct points!")
	if falls_on_line(a, b, c, tolerance=0.1):
		raise ValueError("All given points lie on one line!")
	center = [(a[0] + b[0] + c[0]) / 3, (a[1] + b[1] + c[1]) / 3]
	step = 1
	dist1, distances, _ = compute_distance(center, a, b, c)
	for iteration in range(maxiter):
		candidates = []
		for sign in (-1, 1):
			for coordinate in (0, 1):
				candidates.append(compute_distance(move_vector(center, coordinate, sign * step), a, b, c))
		new_dist1, new_distances, new_center = min(candidates)
		if new_dist1 < dist1:
			dist1, distances, center = new_dist1, new_distances, new_center
		else:
			step *= 0.5
		if dist1 < 0.01 * tolerance:
			break
	else:
		raise ArithmeticError("Does not converge")
		
	dist_a, dist_b, dist_c = distances
	if not (math.isclose(dist_a, dist_b, abs_tol=tolerance) 
	and math.isclose(dist_a, dist_c, abs_tol=tolerance)):
		raise ArithmeticError("Found point is not true center")
	return (round(center[0], 3), round(center[1], 3)), round(dist_a, 3)
	
if __name__ == '__main__':	
	print(circlefinder((2,2), (-5,1), (-1,-6)))




#Appendix

def date_adder(func):
	date = "2020_03_04"	
	def inner(*args, **kwargs):
		print("Current date:", date)
		return func(*args, **kwargs)
	return inner
	
# ~ if __name__ == '__main__':	
	# ~ circlefinder = date_adder(circlefinder)
	# ~ print(circlefinder((2, 2), (-5, 1), (-1, -6), 3))
