import pandas
#import pandas libarary
#pip install pandas on cmd

#reading file in the same folder or provide the path
df=pandas.read_excel("input.xlsx")
df_filter=df.filter(['switch',"input", "fping"]) 

print(df_filter)



################################################
#filter column where fping is empty
df=df[df.fping.isnull()]

# or 

df=df[df["fping"] == 'reachable']
print(df)
print('======')


#Sorting
#df=df.sort_values(by=['name'], ascending=True)

#replace Nan
#import numpy
#df['Project type'] = df['Project type'].replace(np.nan, '')
#repalce values in column
#df_filters['Serial number'] = df_filters['Serial number'].replace('TOBECHECKED', 'Serial number not found in the template')
#Multiple filters
#inner_df=inner_df[(inner_df["Action required"] == 'Add') | (inner_df["Action required"] == 'Remove')  | (inner_df["Action required"] == 'Add (Swap)')  | (inner_df["Action required"] == 'Remove (Swap)') | (inner_df["Action required"] == 'Redeployment')] 
	       




