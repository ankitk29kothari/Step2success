'''a- append, open file and update, if not then create it
r- read, read onl mode
w - write, delete and rewrite,if not then create
x- create, error if file exists , if not then create'''



def read(file_name):
	f=open(file_name,'r')
	value=(f.read())
	print(type(value))
	print(value)


def read_list(file_name):
	f=open(file_name,'r')
	value=f.readlines()
	print(type(value))
	print(value)


def append(file_name,variable):
	f=open(file_name,'a')
	value=f.write(variable)
	f.close()
	read(file_name)


def create(file_name,variable):
	f=open(file_name,'x')
	value=f.write(variable)
	f.close()
	read(file_name)

def write(file_name,variable):
	f=open(file_name,'w')
	value=f.write(variable)
	f.close()
	read(file_name)

'''for i in range(0,10,2):
	append(str(i))
	append('\n')'''



#create("create_file_ex2.txt","hello Iam there!!!!!")
write("create_file_ex2.txt","hello Iam there!!!!!")