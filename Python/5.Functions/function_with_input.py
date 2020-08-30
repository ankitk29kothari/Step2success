



def add(excel_name):
	import pandas
	df=pandas.read_excel(excel_name)
	print(df)




def sub(a,b):
	print(a-b)




def mul(**kwargs):

	print(kwargs,type(kwargs))
	print(kwargs['name'])



mul(name='ankit',class2='222')




















