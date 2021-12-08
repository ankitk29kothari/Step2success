a=2
b=0


try:
	c=a/b
	print(c)

except ZeroDivisionError:
	print("no. cant be divide bt zero")

except ValueError:
	print("only int are allowed")

except:
	print("error")