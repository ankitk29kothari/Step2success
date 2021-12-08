a=2
b=0


try:
	c=a/b
	print(c)
	

except Exception as e:
	print("error",e)

else:
	print("Iam only run when try finsih properly or except wont run")

finally:
	print("I will always run")