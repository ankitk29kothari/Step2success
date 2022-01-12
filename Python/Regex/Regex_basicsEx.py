import re

text='My name is ankit Kothari & ankit \
is working in Obs.maattres My phone no is 808-266-132A and 907.432.4512 cat, bat, mat, lat'

text2='SRT\SRT 359891 Quote 455  Burgos Aranda spain  MLAN Maintenance change_55 form.xlsx'



pattern=re.compile(r'[897]0\d[.-]\d{3}[.-]\d*')
#pattern=re.compile(r'\w[a]\w[,]')

#pattern1=re.compile(r'\w\w\w\w?\w?.\d\d\d\d?\d?\d?')

matches=pattern.findall(text)
pattern=re.compile(r'\w[a]\w[,]')

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

'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
import re 
name=input()
pattern=re.compile(r'[1-9][0-9][0-9][-][0-9][0-9][0-9][-][0-9]{4}')
x=pattern.findall(name)

d={}
for i in x:
    d[i]=x.count(i)

max=0
max2=''
for k,v in d.items():
    if v>=max:
        max=v
        max2=k

print(max2)



    

import re 
name=input()
pattern=re.compile(r'[1-9][0-9][0-9][-][0-9][0-9][0-9][-][0-9]{4}')
x=pattern.findall(name)

d={}
for i in x:
    d[i]=x.count(i)

max=0
max2=''
for k,v in d.items():
    if v>=max:
        max=v
        max2=k

print(max2)
