import memory_profiler as mem_profile
import random
import time

names=['john','adai','Nupur','Mayank']
sub=['maths','English','Hindi','Physics']

print('Memory (Before): ' + str(mem_profile.memory_usage()) + 'MB' )

def people_list(no):
	result=[]
	for i in range(no):
		person={
			id:i,
			'name':random.choice(names),
			'sub':random.choice(sub)

		}

		result.append(person)
	return(result)



def people_generators(no):
	
	for i in range(no):
		person={
			id:i,
			'name':random.choice(names),
			'sub':random.choice(sub)

		}

		
	yield(person)

#a=people_list(1000000)
a=people_generators(100000)
print(next(a))


print('Memory (After): ' + str(mem_profile.memory_usage()) + 'MB' )