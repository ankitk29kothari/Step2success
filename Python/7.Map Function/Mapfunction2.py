#provide input to the function one by one with itteration.
import time
def myfunc(a, b):
	time.sleep(1)
	return a + b



list1=[1,2,3]
list2=[10,11,12]

x = map(myfunc, (list1), (list2))
print(list(x))