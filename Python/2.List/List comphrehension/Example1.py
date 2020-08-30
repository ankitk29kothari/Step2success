#Normal Method

#1.
l=[]
for i in range (0,20):
	l.append(i*i)
print(l)

##############################################
# By List Comphrehension
l_c=[i*i for i in range(0,20)]
print(l_c)


#################################################
#################################################

name='Ankit Kothari'

l2=[]
for i in name:
	l2.append(i)
print(l2)

###############################################
# By List Comphrehension
l_c2=[i for i in name]
print(l_c2)