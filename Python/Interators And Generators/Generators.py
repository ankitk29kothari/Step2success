'''def square(no):
	list=[]
	for i in range(0,no):
		list.append(i*i)
	return(list)


s=square(1000000)
print(s)'''


#Through Generators

def square(no):
	
	for i in range(2,no):
		yield(i*i)

		#pause

		yield('Function resume')

		yield(i*i*i)
	


s=square(1000000)
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))

