a=[5,4,3,2,1]
a=[1,2,3,7,5,6,4,8,9]
import time
sorted=True


for i in range(0,len(a)):
	print('main')
	sorted=True
	for j in range(1,len(a)-i):
		if a[j]<a[j-1]:
			a[j],a[j-1]=a[j-1],a[j]
			print('inner')
			print(a)
			time.sleep(1)
			sorted=False
	if sorted:
		break

print(a)	