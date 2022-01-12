#############################
#                            #
#      Step2success.in       #
#        copyright           #
############################## 


#SQLite is a relational database management system contained in a C library. In contrast to many other database management systems, 
#SQLite is not a client–server database engine. Rather, it is embedded into the end program
# only can use in local system
import sqlite3 
 
db='ankit2.db'

def create(): 
                      
       
       con = sqlite3.connect(db) # connect database
       c=con.cursor() 
       c.execute('''CREATE TABLE emp01
       	(id integer,
       	name text,
       	email text,
       	phone_no integer
       	)''')
       c.execute("INSERT INTO emp01 VALUES (1,'Ankit','ankit.kothari@orange.com',8882663652)")
       con.commit()



def insert():
	con = sqlite3.connect(db) # connect database
	c=con.cursor() 
	c.execute("INSERT INTO emp01 VALUES (2,'xyz','ankit.kothari@orange.com',8882663652)")
	con.commit()
	print('Inserted')


#insert()
def read():

	    print('reading database')
	    con = sqlite3.connect(db) # connect database
	    c=con.cursor() 
	    
	    for row in c.execute('SELECT * FROM emp01 ORDER BY name DESC ' ):
	    	
		  
		    print(row)
		
		    	
		
	    con.close()


def update(name,email,phone_no): 
                      
       
       con = sqlite3.connect(db) # connect database
       c=con.cursor() 
       
       c.execute("UPDATE  emp01 SET name='{}',email='{}',phone_no= '{}' WHERE id='1'".format(name,email,phone_no))
       print('Updated sucessfully')
       read()




# uncomment to call any functions

#create()
#update('ankit','xx.gmail.com',123)
read()