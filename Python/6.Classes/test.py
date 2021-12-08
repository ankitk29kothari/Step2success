a='wekdkdww'
d={}

for i in a:
	x=d.get(i,0)
	d[i]=x+1




y=d.values()
print(max(y))
l1=list(d.keys())
l2=list(d.values())
#print(l2)

s=(l2.index(max(y)))
print(l1[s])





########################################

a=0
b=1
c=0
def fab(x,a,b,c):
	for i in range(0,x):
		
		
		yield(a)
	
		c=a+b
		a=b
		b=c

x=fab(10,a,b,c)
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())



