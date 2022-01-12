a=2
b=3
c=9

#manually error raising
raise NameError('limit exceed')


# HANDLE THE ERROR AND EXCEPTIONS
try:

	print(a+b)
	print(a+c)

except Exception as e:
	print(e)

else:

	print("else is running")


finally:
	print("Always running")












