#############################
#                            #
#      Step2success.in       #
#        copyright           #
##############################           
#Flask is light weighted framework here we are creating functions same like python just difference is here we are mapping the function 
#with @app route so we are calling the function from web and return the data to web
#pip install flask        

from flask import * 

app = Flask(__name__)






#1st function / by default address(home page)
@app.route('/')
def student():
   return ('Hello Iam Ankit')
   #return value to url.


@app.route('/home')
def student2():
   return ('Hello Iam Flask2')
   #return value to url.


@app.route('/Sahil')
def sahil():
   return ('<h1>Sahil is bca grad</h1>')
   #return value to url.

	

if __name__ == '__main__':
   app.run(port=5000,debug=True)
   #change port acc to your convienence