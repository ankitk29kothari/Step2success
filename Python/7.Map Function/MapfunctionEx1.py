#The map() function executes a specified function for each item in a iterable. The item is sent to the function as a parameter.

def myfunc(n):
  return len(n)

x = map(myfunc, ('Step', '2', 'success'))


print(list(x))