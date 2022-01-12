# Find the no of digit ,alpha & spl chs in user given password using counter
c1=c2=c3=0





a="ank@12222222222222222222223#"
for i in a:

	if i.isdigit():
		print("Digit:", i)
		c1=c1+1


	elif i.isalpha():
		print('Alpha: ', i)


	else:
		print("Spl chs:", i)














print(c1)


