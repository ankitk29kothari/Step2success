a=2
b=4

#print(d)

try:
	c=a/b
	print(c)
	

except Exception as e:
	print("error",e)
	print("Iam running")
	

#optionally


else:
	print("Iam only run when try finsih properly or except wont run")

finally:
	print("I will always run")