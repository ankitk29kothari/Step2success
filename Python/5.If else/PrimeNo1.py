prime_no=[2] 



for i in range(2,1000):
	for j in prime_no:
		if i%j==0:
			print('i=',i,'j=',j,'prime_no=',prime_no)
			print('breaking statment bcz condnt not satisfied')
			print('\n\n')
			break
	else:
		prime_no.append(i)
		print('i=',i,'j=',j,'prime_no=',prime_no)


print((prime_no))



print((prime_no))
