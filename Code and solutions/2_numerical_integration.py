

#Felix Bittmann, 2020

import math

def integration(function, x1, x2, n):
	if x1 >= x2:
		raise AssertionError("x1 must be smaller than x2!")
	totallength = x2 - x1
	partlength = totallength / n
	totalarea = 0
	for i in range(n):
		xvalue = x1 + partlength * i
		yvalue = eval(function.replace("x", str(xvalue)))
		partarea = yvalue *  partlength
		totalarea += abs(partarea)
	return round(totalarea, 5)

if __name__ == '__main__':
	print(integration("(x)**2", 0, 2, 10**4))
	print(integration("math.sin(x)", 0, 2 * math.pi, 10**4))
