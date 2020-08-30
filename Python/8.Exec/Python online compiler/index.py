from flask import * 

app = Flask(__name__)


import datetime
name='ankit kothari'

@app.route('/')
def student():
   return render_template('index.html')















@app.route('/result',methods = ['POST', 'GET'])
def result():

   if request.method == 'POST':

      result = (request.form)
      print(result)
      result=exec((result['code']))
     
      return render_template("result.html",result = result)

      if request.method == 'GET':
      	result = request.form
      	print(result)
      	return render_template("result.html",result = result)





if __name__ == '__main__':
   app.run(port=5036)