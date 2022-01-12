import concurrent.futures
from concurrent.futures import ProcessPoolExecutor
import time

def do_something(i):
	
	
	time.sleep(1)
	return(i*i*i*i*i*i*i*i)
	





			

def main():
	list1=[1,2,4,5,6,3,4,5]
	with concurrent.futures.ThreadPoolExecutor(max_workers = 4) as executor:
	#with concurrent.futures.ProcessPoolExecutor() as executor:
		results=executor.map(do_something,list1)
		for i in results:
			print(i)
	

if __name__ == '__main__':
	main()