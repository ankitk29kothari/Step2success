def add(*args):
	print(args,type(args))
	sum=0
	for i in args:
		sum=sum+i
	print(sum)





#add(1,2,4,7)

##variable length keyword argument
##kwargs-keywords arguments
def data(**x):
	print(x,type(x))
	





data(name='ankit',age=18,education='b.tech')