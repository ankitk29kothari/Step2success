
from flask import * 

app = Flask(__name__)
import pandas as pd





###########################################
#main page
@app.route('/')
def mainpage():


	a=2
	b=5
	c=str(b-a)
	output=f'diff of {a} & {b} is {c}'


	return(output)





@app.route('/daily_report')
def report():


	df=pd.read_excel(r'C:\Users\mcjp2518\Desktop\step2successs\Step2success\Pandas\read\input.xlsx')
	df=(df.to_html())

	return(df)





@app.route('/user')
def user():


	name='user details'


	return(name)



if __name__ == '__main__':
   app.run(port=82,debug=True,host='0.0.0.0')

