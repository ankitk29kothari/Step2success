import pandas
#import pandas libarary
#pip install pandas on cmd

#reading file in the same folder or provide the path
df=pandas.read_excel("input.xlsx")
#df_filter=df.filter(['switch',"input", "fping"]) 

#print(df_filter)



################################################
#filter wheere fping is empty
#df=df[df.fping.isnull()]
df=df[df["fping"] == 'reachable']
print(df)
print('======')









