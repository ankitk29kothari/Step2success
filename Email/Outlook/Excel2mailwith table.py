import pandas as pd
import time

# pip install  pypiwin32
#pip install pandas


import os
import sys
import win32com.client
import win32com
s= win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
o = win32com.client.Dispatch("Outlook.Application")
#######################################################


 

#print(df)
########################################################
#READING EXCEL
df=pd.read_excel('ankit.xlsx','Sheet1')
col_name=df.columns
print(col_name)
to=df['to']
cc=df['cc']
sub=df['subject']
body1=df['body1']
body2=df['body2']
body3=df['body3']
body4=df['body4']


#############################################################
#FUNCTION TO SEND MAIL
def send_mail(mail_to,mail_cc,mail_subject,mail_body1,mail_body2):




	mail_html="""<!DOCTYPE html>
<html>
<head>
<style>
#customers {{
 
  border-collapse: collapse;
  width: 100%;
}}

#customers td, #customers th {{
  border: 1px solid #ddd;
  padding: 8px;
   text-align: center;
}}

#customers tr:nth-child(even){{background-color: #f2f2f2;}}

#customers tr:hover {{background-color: #ddd;}}

#customers th {{
  padding-top: 5px;

  padding-bottom: 5px;
  text-align: center;
  background-color: #05000E;
  color: orange;
}}
</style>
<body>
Last Update (No of Days)

<table  id="customers">  
	<tr>
	<th>{}</th><th>{}</th>
	</tr>

	<tr>

	<td>{} </td> <td> {}</td>


	</tr>



	</table>


	""".format(col_name[1],col_name[2],mail_body1,mail_body2)

	Msg = o.CreateItem(0)
	Msg.To = mail_to
	Msg.CC = mail_cc
	#Msg.BCC = "more email addresses here"
	    
	Msg.Subject = mail_subject
	Msg.HTMLBody = mail_html
	    
	#attachment1 = "Path to attachment no. 1"

	#Msg.Attachments.Add(attachment1)
	 
	Msg.Send()
################################################################################3




# EXCEL TO MAIL FUNTN

for a,b,c,d,e,f,g in zip(to,cc,sub,body1,body2,body3,body4):
	print(a,b,c,d,e,f,g)
	#print(a)
	
	send_mail(a,b,c,d,e)
	time.sleep(300)
