

#Felix Bittmann, 2020


import random
from itertools import combinations


def find_distance(p1, p2):
	return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def remove_circles(circles):
	remove = set()
	for pair in combinations(circles, 2):
		small_circle, big_circle = sorted(pair, key=lambda c: c[2])
		distance_centers = find_distance(small_circle, big_circle)
		if big_circle[2] >= distance_centers + small_circle[2]:
			# small circle lies within the big circle
			remove.add(small_circle)
	return [c for c in circles if c not in remove]
	
	
def compute_total_area(circles, n, iterations):
	total_simulations = 0	# Area found using simulations
	total_boxes = 0			# Area found using boxes
	skipped_boxes = 0
	total_points = 0
	circles = remove_circles(circles)
	xmin, xmax, ymin, ymax = find_circumscribing_rectangle(circles)
	boxarea = ((xmax - xmin) * (ymax - ymin)) / (n ** 2)
	for box_part in iter_parts(xmin, xmax, ymin, ymax, n):
		if box_inside(box_part, circles):
			skipped_boxes += 1
			total_boxes += boxarea
		else:
			total_points += iterations
			hitrate = find_hitrate(box_part, circles, iterations)
			total_simulations += boxarea * hitrate
	print(f"Share of skipped boxed: {skipped_boxes / n**2}")
	print(f"Total number of all points drawn (in thousands): {total_points // 10**3}")
	return total_simulations + total_boxes
	
	
def find_circumscribing_rectangle(circles):
	xmin = min(c[0] - c[2] for c in circles)
	xmax = max(c[0] + c[2] for c in circles)
	ymin = min(c[1] - c[2] for c in circles)
	ymax = max(c[1] + c[2] for c in circles)
	return xmin, xmax, ymin, ymax
	
	
def iter_parts(xmin, xmax, ymin, ymax, n):
	xsize = (xmax - xmin) / n
	ysize = (ymax - ymin) / n
	for xstep in range(n):
		for ystep in range(n):
			xmin_part = xmin + xstep * xsize
			ymin_part = ymin + ystep * ysize
			yield xmin_part, xmin_part + xsize, ymin_part, ymin_part + ysize
			
			
def box_inside(box, circles):
	xmin, xmax, ymin, ymax = box
	for circle in circles:
		if (find_distance([xmin, ymin], circle) < circle[2] and
			find_distance([xmin, ymax], circle) < circle[2] and
			find_distance([xmax, ymin], circle) < circle[2] and
			find_distance([xmax, ymax], circle) < circle[2]):
			return True
	return False
	
	
def find_hitrate(box, circles, iterations):
	xmin, xmax, ymin, ymax = box
	hits = 0
	for i in range(iterations):
		zx = xmin + (xmax - xmin) * random.random()
		zy = ymin + (ymax - ymin) * random.random()
		for circle in circles:
			if find_distance((zx, zy), circle) < circle[2]:
				hits += 1
				break
	return hits / iterations


if __name__ == '__main__':
	data = [(1.6417233788,   1.6121789534,   0.0848270516,),
	(-1.4944608174 ,  1.2077959613,   1.1039549836,),
	 (0.6110294452,  -0.6907087527,   0.9089162485,),
	 (0.3844862411,   0.2923344616,   0.2375743054,),
	(-0.2495892950,  -0.3832854473,   1.0845181219,),
	 (1.7813504266,   1.6178237031,   0.8162655711,),
	(-0.1985249206,  -0.8343333301,   0.0538864941,),
	(-1.7011985145,  -0.1263820964,   0.4776976918,),
	(-0.4319462812,   1.4104420482,   0.7886291537,),
	 (0.2178372997,  -0.9499557344,   0.0357871187,),
	(-0.6294854565,  -1.3078893852,   0.7653357688,),
	 (1.7952608455,   0.6281269104,   0.2727652452,),
	 (1.4168575317,   1.0683357171,   1.1016025378,),
	 (1.4637371396,   0.9463877418,   1.1846214562,),
	(-0.5263668798,   1.7315156631,   1.4428514068,),
	(-1.2197352481,   0.9144146579,   1.0727263474,),
	(-0.1389358881,   0.1092805780,   0.7350208828,),
	 (1.5293954595,   0.0030278255,   1.2472867347,),
	(-0.5258728625,   1.3782633069,   1.3495508831,),
	(-0.1403562064,   0.2437382535,   1.3804956588,),
	 (0.8055826339,  -0.0482092025,   0.3327165165,),
	(-0.6311979224,   0.7184578971,   0.2491045282,),
	 (1.4685857879,  -0.8347049536,   1.3670667538,),
	(-0.6855727502,   1.6465021616,   1.0593087096,),
	( 0.0152957411,   0.0638919221,   0.9771215985)]
	
	# ~ print(compute_total_area(data, 100, 2000))	#Comment in to run
	
	
	
########################################################################
### Task 1 ###
########################################################################
"""Apparently the number of rectangles is strictly deterministic, here has no random factor.
The more rectangles we define, the more accurate our estimation becomes. If we have an extremely
large number of rectangles, we can theoretically do without a simulation, because the grid is so
fine that good results can already be approximated with it. If we have only a few rectangles and a
lot of points, this is almost like the calculation of pi in a previous chapter, where we did without
rectangles."""

########################################################################
### Task 2 ###
########################################################################

def simulation2():
	true_value = 21.56503660			#Taken from website
	nboxes = (5, 20, 50, 100, 400)
	ndraws = (50, 100, 500, 2000, 5000)
	for nr in nboxes:
		for nz in ndraws:
			print(f"Number of boxes: {nr} | Number of draws: {nz}")
			res = compute_total_area(data, nr, nz)
			absdiff = round(abs(res - true_value), 6)
			print(absdiff)
			print("************************************")
	
	
"""Comment in to run, will take some time."""	
# ~ simulation2()
