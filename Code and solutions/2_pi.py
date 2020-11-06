


#Felix Bittmann, 2020


import math
import itertools

def arctan(z, places):
	extra_places = math.ceil(math.log10(places / math.log10(z)))
	sign = -1
	term = 10 ** (places + extra_places) // z
	result = term
	for power in itertools.count(3, 2):
		term //= z ** 2
		if term < power:
			break
		result += (sign * term) // power
		sign *= -1
	return result // (10 ** extra_places)
	
	
def pi(places):
	return 4 * (4 * arctan(5, places) - arctan(239, places))
	
	
if __name__ == '__main__':	
	print(pi(30))




########################################################################
### Task 1 ###
########################################################################


import time


tstart = time.time()
a = pi(2500)
duration = time.time() - tstart
print("duration:", duration)



tstart = time.time()
a = pi(5000)
duration = time.time() - tstart
print("duration:", duration)


"""Notice the non-linear increase!"""


########################################################################
### Task 2 ###
########################################################################
"""To avoid a long runtime these lines are commented out as default."""
# ~ many = str(pi(20_000))

# ~ tel = "9345699"
# ~ datum = "19951206"
# ~ print(tel in many)
# ~ print(datum in many)



########################################################################
### Task 3 ###
########################################################################

def euler(digits):
	"""BTW, Euler is pronounced like 'Oiler'"""
	digits += 10		#Just be on the safe side
	total = 2 * (10**digits)	#First both terms
	denominator = 1
	counter = 2
	term = None
	while term != 0:
		denominator = denominator * counter
		term = (10**digits) // denominator
		total = total + term
		counter += 1
	return int(str(total)[:-10])	#Zusaetzliche Stellen wieder entfernen
	
print(euler(100))
