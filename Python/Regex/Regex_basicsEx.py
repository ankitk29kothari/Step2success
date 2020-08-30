import re

text='My name is ankit Kothari & ankit \
is working in Obs.maattres My phone no is 808-266-132A and 907.432.4512 cat, bat, mat, lat'

text2='t ha@ hahahaha2 hadfdfd'

pattern=re.compile(r'[897]0\d[.-]\d{3}[.-]\d*')
pattern1=re.compile(r'\b[^b]at\w*')
matches=pattern1.finditer(text)

for i in matches:
	print(i)



'''
Ques1
#cat,bat,mat,lat,ank,kot
output=cat,mat,lat
3 digit
1 alpha 

ans [^b]at
'''

