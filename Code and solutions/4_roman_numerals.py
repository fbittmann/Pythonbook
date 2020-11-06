


#Felix Bittmann, 2020

roman_numerals = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
	(50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

def to_roman(integer):
	if not isinstance(integer, int) or not 0 < integer < 4000:
		raise ValueError()
	output = ""
	for value, symbol in roman_numerals:
		while integer >= value:
			output += symbol
			integer -= value
	return output
	
	
def from_roman(roman):
	if not isinstance(roman, str):
		raise ValueError()
	output = 0
	for value, symbol in roman_numerals:
		while roman.startswith(symbol):
			output += value
			roman = roman[len(symbol):]
	return output
	
	
for i in range(1, 4000):
	assert i == from_roman(to_roman(i))
	
print(to_roman(2020))
