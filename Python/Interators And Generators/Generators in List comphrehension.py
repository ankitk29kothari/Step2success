# List comphrehension
#l=[i*i for i in range(0,10000000)]

# With Generators

l=(i*i for i in range(0,10000000))

print(next(l))
print(next(l))
print(next(l))

