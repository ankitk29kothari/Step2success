class Employee():
	def __init__(self,first_name,last_name):
		self.f_name=first_name
		self.l_name=last_name
		self.email=(self.f_name+'.'+self.l_name+'@xyz.com')
		self.employee_id=(self.f_name+'101')

	def details(self):
		print(f'Name of employee {self.employee_id} is {self.f_name} {self.l_name} & email{self.email}')
		self.bounus=(salary*5%)
		
















x=Employee('Ankit',"Kothari")

y=Employee('Kumud',"Goyal")
y.details()

z=Employee('Chirag',"Goyal")
z.details()



































