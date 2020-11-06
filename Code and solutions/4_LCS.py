



#Felix Bittmann, 2020

import random
def create_genes(number, length):
	alphabet = "ACGT"
	return [
		"".join(random.choices(alphabet, k=length))
		for i in range(number)
	]
	
	
def lcs(allstrings):
	reference = allstrings[0]
	tested = set()
	for length in range(len(reference), 0, -1):
		for pos in range(0, len(reference) + 1 - length):
			subsequence = reference[pos:pos + length]
			if subsequence not in tested:
				if all(subsequence in sequence for sequence in allstrings[1:]):
					return subsequence
				tested.add(subsequence)
	return ""
	
	
def main():
	data = create_genes(3, 14)
	print(data)
	print(lcs(data))

if __name__ == '__main__':
	random.seed(12345)
	main()
	
