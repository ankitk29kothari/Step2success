import pandas
#import pandas libarary
#pip install pandas on cmd

#reading file in the same folder or provide the path
df=pandas.read_excel("input.xlsx")


#use this oine if your headingg is not placed in by deafult o position
'''df=pandas.read_excel("input.xlsx",header=1)'''

col_1=df['switch']
col_2=df['input']
col_3=df['output']
col_4=df['command']

for i,j,k,l in zip(col_1,col_2,col_3,col_4):
	print(f'This is switch - {i}  firing command {l} input rate:{j}, outputrate:{k}')
	print('----')

