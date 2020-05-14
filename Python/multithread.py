import concurrent.futures
from concurrent.futures import ProcessPoolExecutor
import time



def do_something(sec):
	time.sleep(sec)
	#print(time.perf_counter())
	for i in range(0,100000):
		print(i)
	
	#print(sec,'Done sleeping')
	return(sec)
with concurrent.futures.ThreadPoolExecutor(max_workers = 500) as executor:
		a=executor.submit(do_something,10)
		for i in range(0,10):
			print(i)

def main():
	
	
		
	'''t1=time.perf_counter()

	#with concurrent.futures.ProcessPoolExecutor(max_workers = 60) as executor:
	with concurrent.futures.ThreadPoolExecutor(max_workers = 500) as executor:
		secs=[]

		for _ in range(0,60):
			secs.append(5)

		#a=executor.submit(do_something,1)
		#print(a.result())
		results=executor.map(do_something, secs)
		for result in results:
			print(result)
		print((results))
		t2=time.perf_counter()
		print('Finsihed in',(t2-t1/2),'sec')'''




if __name__ == '__main__':
	main()