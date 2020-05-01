import os
import pandas as pd
from collections import defaultdict
cwd = os.getcwd()
print(cwd)
path=cwd+'/dir'



f=[(r.replace(path,""),d,len(file)) for r,d, file in os.walk(path)]
#print(f)

df=defaultdict(list)

for i,j,k in f:
	if k>0:
		i=i.split('\\')
		i1=i[-1]
		i2=(i[-2])
		
		print(i2,i1,k)
		df[i1].append(k)



print(df)
df = pd.DataFrame(df, columns = df,index=[f[0][1]])
print(df)

df.to_excel (r'export_dataframe.xlsx', index = True, header=True)

os.system('export_dataframe.xlsx')