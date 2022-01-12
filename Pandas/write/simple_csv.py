
import pandas as pd
from pandas import ExcelWriter
#importing function to write excel

from pandas import ExcelFile
#operating system importing for opeing file at end


file_name='s2s_simple.csv'

dict = {'Name':"ankit",  'Age': "10",'Place':"india" }
df = pd.DataFrame(dict,index=[1,2,3])
df.to_csv(file_name,mode='a',header=True,index=False)