string='((Ankit)'
left_paanthesis='('
right_paanthesis=')'
stack=[]
for i in string:
	if i in left_paanthesis:
		stack.append(i)
	if i in right_paanthesis:
		stack.pop()

if len(stack)>0:
	print('Not Match')