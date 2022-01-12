fruits=['Apple','Banana','Cherry','Mango']
states=['Delhi','Mumbai','Agra','Hyderabad','pune']


for i,j in zip(fruits,states):
	print(i,j)
#for i,j in zip(fruits,states):
#	print(i,j)

for index,i in  enumerate(fruits):
	print(index,i)