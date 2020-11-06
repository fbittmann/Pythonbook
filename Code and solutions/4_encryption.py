



#Felix Bittmann, 2020

import random
from functools import partial

def generate_hash(string):
	"""Hashes a string"""
	data = [ord(element) for element in string]
	sum1, sum2 = 0, 0
	for element in data:
		sum1 = (sum1 + element * 11111) % (10 ** 6)
		sum2 = (sum2 + sum1) % (10 ** 6)
	return str(sum1) + str(sum2)


def turnaround(inputstring):
	return inputstring[::-1]
	

def twister(inputstring):
	assert len(inputstring) % 2 == 0
	output = ""
	for i in range(0, len(inputstring) - 1, 2):
		output += inputstring[i + 1]
		output += inputstring[i]
	return  output


def zipper(inputstring, reverse=False):
	assert len(inputstring) % 2 == 0
	output = ""
	if not reverse:
		for i in range(0, len(inputstring) // 2):
			output += inputstring[i]
			output += inputstring[-i - 1]
	else:
		a = [inputstring[i] for i in range(0, len(inputstring), 2)]
		b = [inputstring[i] for i in range(1, len(inputstring), 2)][::-1]
		for i in range(len(inputstring) // 2):
			output += a[i]
		for i in range(len(inputstring) // 2):
			output += b[i]
	return  output


def encrypt(message, password):
	"""Encrypts a message"""
	message = message.upper()
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"	
	if len(message) % 2 == 0:
		message += "".join(random.choices(alphabet, k=20)) + "ZZ"
	else:
		message += "".join(random.choices(alphabet, k=20)) + "AAA"
	
	hashvalue = generate_hash(password)
	funclist = [turnaround, zipper, twister]
	
	for element in hashvalue:
		rest = int(element) % 3
		message = funclist[rest](message)	
	return message


def decrypt(code, password):
	"""Decrypts the code"""
	hashvalue = generate_hash(password)[::-1]
	funclist = [turnaround, partial(zipper, reverse=True), twister]
	for element in hashvalue:
		rest = int(element) % 3
		code = funclist[rest](code)
	if code.endswith("ZZ"):
		return code[:-22]
	else:
		return  code[:-23]





if __name__ == '__main__':
	a = ["Hallo", "Hello", "12345678", "12334567", "averylongstringisreducedbythehashing"]
	for element in a:
		print(generate_hash(element))
		
		
	message = "MEETMEATTHEOLDBRIDGEATSEVEN"
	password = "mysecret"
	code = encrypt(message, password)
	print(code)
	
	decode = decrypt(code, password)
	print(decode)
	assert message == decode
