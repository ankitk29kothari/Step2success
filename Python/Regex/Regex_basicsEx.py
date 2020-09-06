import re

text='My name is ankit Kothari & ankit \
is working in Obs.maattres My phone no is 808-266-132A and 907.432.4512 cat, bat, mat, lat'

text2='SRT\SRT 359891 Quote 455  Burgos Aranda spain  MLAN Maintenance change_55 form.xlsx'

pattern=re.compile(r'[897]0\d[.-]\d{3}[.-]\d*')

pattern1=re.compile(r'\w\w\w\w?\w?.\d\d\d\d?\d?\d?')
matches=pattern1.findall(text2)
matches_str=' '.join(matches)
print(matches_str)



'''
Ques1
#cat,bat,mat,lat,ank,kot
output=cat,mat,lat
3 digit
1 alpha 

ans [^b]at
'''

