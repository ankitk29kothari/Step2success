#Multiple Inheritence
class Employee():
    def __init__(self,first_name,last_name):
        self.f_name=first_name
        self.l_name=last_name
        self.email=(self.f_name+'.'+self.l_name+'@xyz.com')
        self.employee_id=(self.f_name+'101')
        self.salary=10000


class Developer(Employee):
    def __init__(self,first_name,last_name,prog,work_exp):
        #super.__init__(self,first_name,last_name)
        Employee.__init__(self,first_name,last_name)
        self.prog=prog
        self.exp=work_exp

class Manager(Employee):
    def __init__(self,first_name,last_name,employees):
        Employee.__init__(self,first_name,last_name)
        self.employees=employees

    def add_emp(self,emp_name):
        if emp_name not in self.employees:
            self.employees.append(emp_name)

    def remove_emp(self,emp_name):
        if emp_name in self.employees:
            self.employees.remove(emp_name)

    def print_emp(self):
        for emp in self.employees:
            print('---->',emp.email)


x=Developer('Ankit',"Kothari",'python',1)

y=Employee('Kumud',"Goyal")
z=Employee('Chirag',"Goyal")

mgr1=Manager('Hasan','Rayan',[x,y,'sakshi'])

mgr1.add_emp(z)
mgr1.remove_emp(x)

print (type(mgr1))
#mgr1.print_emp()

print(mgr1.__dict__)
#print(help(x))
print(x.__dict__)
print(y.__dict__)
#print(x.f_name)