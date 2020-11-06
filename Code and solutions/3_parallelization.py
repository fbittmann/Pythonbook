



#Felix Bittmann, 2020



def primegen(n, queue):
	if n % 2 == 0:
		n += 1
	while True:
		for i in range(3, int(n**0.5 + 1), 2):
			if n % i == 0:
				break
		else:
			queue.put(n)
		n += 2
		
		
from multiprocessing import Process, Queue
def multiprimegen(cores, nfinal):
	q = Queue()
	processes = []
	for number in range(1, cores + 1):
		start = 10**14 // number
		process = Process(target=primegen, args=(start, q))
		process.start()
		processes.append(process)
	primes = []
	while len(primes) < nfinal:
		primes.append(q.get())
	for process in processes:
		process.terminate()		#shut down all running prime functions
	return primes
	
	
	
def prime_product(inqueue, outqueue):
	while True:
		prime_a = inqueue.get()
		prime_b = inqueue.get()
		outqueue.put(prime_a * prime_b)
		
		
def serial(cores, nfinal):
	processes = []
	q1 = Queue()
	q2 = Queue()
	for number in range(1, cores + 1):
		start = (10**14) // number
		process = Process(target=primegen, args=(start, q1))
		process.start()
		processes.append(process)
	process = Process(target=prime_product, args=(q1, q2))
	process.start()
	processes.append(process)
	
	output = []
	while len(output) < nfinal:
		output.append(q2.get())
	for process in processes:
		process.terminate()
	return output
	
	
if __name__ == '__main__':
	print(multiprimegen(2, 10))
	print(serial(2, 10))

