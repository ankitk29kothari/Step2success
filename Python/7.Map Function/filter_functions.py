#The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True





adults = filter(myFunc, ages)

print(list(adults))


#for i in adults:
#	print(i)
