import os
#os.mkdir("astep2success")

#for i in range(0,100):
#	os.mkdir(f"astep2success/{i}")

os.rmdir(f"astep2success/1")



f=open('demo.txt','r')
a=(f.read())



a=a.replace('administratively down','administratively_down')


################################################


b=a.replace(' ',',')
print(b)


d=''
for i in range(0,len(b)):
	print(i,b[i])
	if b[i]==',':
		if b[i+1]==',':
			pass
		else:
			d=d+b[i]
	else:
		d=d+b[i]

print(d)






