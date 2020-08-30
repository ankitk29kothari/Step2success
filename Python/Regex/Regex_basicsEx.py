import re

text='My name is ankit Kothari & ankit \
is working in Obs.My phone no is 808-266-1323 and 907.432.4512'

text2='t ha@ hahahaha2 hadfdfd'

pattern=re.compile(r'[897]0\d[.-]\d{3}[.-]\d+')
matches=pattern.finditer(text)

for i in matches:
	print(i)






