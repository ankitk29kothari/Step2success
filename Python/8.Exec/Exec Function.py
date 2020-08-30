#This will convert your text as a command in python.So that you can remotely change the code 


file=open('s2s.txt','r')
file=file.read()
print(file)


print('Running file text as command in python')
exec(file)