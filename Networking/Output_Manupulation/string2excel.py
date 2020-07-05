import os
from collections import defaultdict
import pandas as pd
a= open("sh_ip_int_brief.txt", "r")
b=a.readlines()

data=defaultdict(list)

for i in b:
    if 'up' in i:

        #print(i)
        #print(i[0],"&&                  ",i[1])
        #print('+++++++++++++++++++++++')
        
        try:
            i=i.split()
            data['Interface'].append(i[0])
            data['IP-Address'].append(i[1])
        except:
            pass
print(data)

df = pd.DataFrame(data, columns =['Interface','IP-Address'] )
df.to_excel ('shw_int_brf_output_dataframe.xlsx', index = False, header=True)

os.system('shw_int_brf_output_dataframe.xlsx')