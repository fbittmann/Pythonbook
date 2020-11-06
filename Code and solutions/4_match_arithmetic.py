


#Felix Bittmann, 2020



n_same = ["1+", "+=", "23", "35", "90", "60", "69"]
n_diff = ["-+", "-=", "17", "39", "56", "59", "68", "98", "08"]


def replace_at_index(string, index, character):
	return string[:index] + character + string[index+1:]
	
	
def add_match(string):
	for i, char in enumerate(string):
		for less, more in n_diff:
			if char == less:
				yield replace_at_index(string, i, more)
				
				
def change_match(string):
	for i, char in enumerate(string):
		for char1, char2 in n_same:
			if char == char1:
				yield replace_at_index(string, i, char2)
			if char == char2:
				yield replace_at_index(string, i, char1)
		for less, more in n_diff:
			if char == more:
				one_match_less = replace_at_index(string, i, less)
				yield from add_match(one_match_less)
				
			
def solver(equation):
	for candidate in change_match(equation):
		if candidate.count("=") == 1:
			try:
				if eval(candidate .replace('=','==')):
					return  candidate
			except SyntaxError:
				pass
	raise RuntimeError("No solution found")
	
	
print(solver("185+15=270"))



# Appendix

def flatten(inputlist):
	"""Flattens a list"""
	for element in inputlist:
		if not isinstance(element, list):
			yield element
		else:
			yield from flatten(element)
			
a = [1, 2, 3, [8, 77, [3, 4], 7], 5, [34, [], 43]]
# ~ print(list(flatten(a)))



########################################################################
### Task 1 ###
########################################################################

def solver2(equation):
	found = []
	for candidate in change_match(equation):
		if candidate.count("=") == 1:
			try:
				if eval(candidate.replace('=','==')):
					found.append(candidate)
			except SyntaxError:
				pass
	if found:
		return found
	else:
		raise RuntimeError("No solutions found!")


# ~ print(solver2("185+15=270"))


########################################################################
### Task 2 ###
########################################################################
import random
def generator():
	while True:
		term1 = str(random.randint(10, 99))
		sign1 = random.choice(["+", "-"])
		term2 = str(random.randint(10, 99))
		outcome = str(random.randint(1, 198))
		equation = term1 + sign1 + term2 + "=" + outcome
		if "0" in equation or "00" in equation or "000" in equation:
			continue
		try:
			solution = solver(equation)
			if solution == equation:
				continue
		except RuntimeError:
			continue
		return(equation, solution)
		
# ~ print(generator())
