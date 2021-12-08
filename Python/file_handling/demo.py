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






