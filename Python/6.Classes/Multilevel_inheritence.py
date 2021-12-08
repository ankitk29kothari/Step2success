class mamals():
	def __init__(self):
		self.eyes=2
		self.ear=2
		self.hair='yes'
		self.vegetarian='True'


class dog():
	def  __init__(self):
		mamals. __init__(self)
		self.danger='yes'

class cat(dog):
	def __init__(self):
		dog. __init__(self)
		
		self.hair='Brown'
		self.vegetarian='True'
		self.bark='No'
		self.four_legs='yes'
		


x=dog()
print(vars(x))

y=cat()
print(vars(y))
#print(help(y))