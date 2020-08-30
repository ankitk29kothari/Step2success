
#  write a function to add two no from a and b and give output as 16 & return the index no
a = [5, 3, 6, 11, 8]
b = [4, 7, 2, 21, 10]




























def index():
	for i in a:
		for j in b:
			sum=(i+j)
			if sum==16:
				return("Index is",a.index(i),b.index(j))
				


r=index()
print(r)