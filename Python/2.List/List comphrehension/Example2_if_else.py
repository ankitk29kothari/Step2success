#Normal Method
#even no method
e=[]
for i in range(0,20):
	if i%2==0:
		e.append(i)
	else:
		e.append('False')
#print(e)

###############################
#By LC


lc=[ i  for i in range(0,20)  if (i%2==0)   ]

lc1=[ i if (i%2==0) else "False" for i in range(0,20)     ]





#Divisible by 2 & 5
#lc2_5=[ i   for i in range(0,20) if (i%2==0) if(i%5==0)  ]
print(lc)
#print(lc2_5)

'''

#############################################################
############################################################
inventory_gsk_name_list=[str(i).strip().lower()for i in df_inventory['GSK Host Name']]

#Equivalen to this
for i in df_inventory['GSK Host Name']:
	inventory_sk_name.append(str(i).strip().lower())'''