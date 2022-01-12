#############################
#                            #
#      Step2success.in       #
#        copyright           #
##############################           
#Flask is light weighted framework here we are creating functions same like python just difference is here we are mapping the function 
#with @app route so we are calling the function from web and return the data to web
#pip install flask        

from flask import *
from oceane import *

app = Flask(__name__)


import datetime
name='ankit kothari'
import json
import time
import threading
global_lock = threading.Lock()
names=['kothari ankit', 'chaurasia swati']


#1st function / by default address(home page)
@app.route('/')
def student():
   return render_template('index1.html',names=names)
   #return Static HTML template store in Templates & pass this dynamic varibale time and name in that



# when user fill the details in signup form and send we are using post method then passing all that varibales in this fntn
@app.route('/result',methods = ['POST','GET'])
def result():

   if request.method == 'POST':

      result = request.form

      #print('result',type(result),result)
      name=[]
      tickets=[]
      for key in result:
         r=result.getlist(key)
         if str(r[0]) !='':
            print(r[0],r[1])
            name.append(r[1])
            tickets.append(r[0])
      try:
        
        while global_lock.locked():
          time.sleep(0.01)
          continue
        global_lock.acquire()
        browser(tickets,name)
      except:
        try:
          browser(tickets,name)
        except:
          pass
      global_lock.release()
      print('done')

      #db query insert into this ...
      #Insert into user 
   a= {
  "data": [
    
    [2012, 10, 11],
    [2013, 10, 11],
    [2014, 10, 11],
    [2015, 10, 11],
    [2016, 10, 11]
  ]
}

   return jsonify(a)

      





	

if __name__ == '__main__':
   app.run(port=5165,threaded=True)
   #change port acc to your convienence