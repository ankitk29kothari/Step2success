import concurrent.futures
from concurrent.futures import ProcessPoolExecutor
import time
parainko connect

def test ():
	time.sleep(10)
	print(a*a)
	return(a*a)



devices=[1,2,3,4,5,6,7,8,5,5,4,4,3,3,12,2,3,45,6,6,6,6,6]

with concurrent.futures.ThreadPoolExecutor(max_workers = 10) as executor:
	results=executor.map(test,devices)
	#print(list(results))