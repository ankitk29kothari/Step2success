def anagram(s1,s2):
	ht=dict()
	if len(s1)!=len(s2):
		return False
	for i in s1:
		if i in ht:
			ht[i] +=1
		else:
			ht[i] =1
		print(ht)

	for i in s2:
		if i in ht:
			ht[i] -=1
		else:
			ht[i]=1
		print(ht)
	for i in ht:
		if ht[i] !=0:
			return False
	return True

s1="aabccce"
s2="cccbaaf"
s1=s1.replace(" ","").lower()
s2=s2.replace(" ","").lower()

a=anagram(s1,s2)
print(a)

