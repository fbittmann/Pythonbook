




#Felix Bittmann, 2020


from itertools import combinations
def distance(p1, p2):
	"""Distance of two points"""
	xdiff = p1[0] - p2[0]
	ydiff = p1[1] - p2[1]
	return (xdiff ** 2 + ydiff ** 2) ** 0.5


def bruteforce(points):
	"""Finds the pairing with the shortest distance"""
	return min(
		(distance(*pairing), pairing)
		for pairing in combinations(points, 2)
	)
	
	
def mindistance(pointlist):
	"""Finding the shortest distance with divide and conquer"""
	length = len(pointlist)	
	if length < 5:		#Base Case
		return bruteforce(pointlist)
	
	points_left = pointlist[:length // 2]
	points_right = pointlist[length // 2:]
	min_left = mindistance(points_left)
	min_right = mindistance(points_right)
	d = min(min_left, min_right)[0]
	limit_left = [p for p in points_left if abs(p[0] - points_right[0][0]) <= d]
	limit_right = [p for p in points_right if abs(p[0] - points_left[-1][0]) <= d]
	distances = [min_left, min_right]
	for x in limit_left:
		for y in limit_right:
			distances.append((distance(x, y), (x, y)))
	return min(distances)
	
	
import time
import random

def timetest():
	random.seed(12345)
	allpoints = [(random.random() * 100, random.random() * 100) for i in range(5000)]
	start = time.monotonic()
	print(bruteforce(allpoints))
	print(time.monotonic() - start)
	
	start = time.monotonic()
	allpoints.sort()
	print(mindistance(allpoints))
	print(time.monotonic() - start)
	
	
#The runtime is about 10 seconds, depending on your system
if __name__ == '__main__':
	print(timetest())




#Appendix


def calculator(operator, *args):
	if operator == "add":
		return sum(args)
	if operator == "multiply":
		res = 1
		for element in args:
			res *= element
		return res
		
		
# ~ print(calculator("add", 1, 2, 3))
# ~ print(calculator("multiply", 1, 2, 3, 4))


def display(name, **kwargs):
	print("Hello", name)
	for key, value in kwargs.items():
		print(key, value)

# ~ display("User", Day = 1, Place = "West", Flag = True)

	
	
########################################################################
### Task 1 ###
########################################################################


def mindistance2(points):
	points.sort()
	def inner(points):
		length = len(points)	
		if length < 5:		#Base Case
			return bruteforce(points)
		
		points_left = points[:length//2]
		points_right = points[length//2:]
		min_left = inner(points_left)
		min_right = inner(points_right)
		d = min(min_left, min_right)[0]
		limit_left = [p for p in points_left if abs(p[0] - points_left[0][0]) <= d]
		limit_right = [p for p in points_right if abs(p[0] - points_right[-1][0]) <= d]
		distances = [min_left, min_right]
		for x in limit_left:
			for y in limit_right:
				distances.append((distance(x, y), (x, y)))
		return min(distances)
	return inner(points)
	

random.seed(12345)
allpoints = [(random.random() * 100, random.random() * 100) for i in range(5000)]
print(mindistance2(allpoints))		
