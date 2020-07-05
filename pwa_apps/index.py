from flask import Flask ,render_template,jsonify, request
app = Flask(__name__)


@app.route('/')
def show_all():
	


	return render_template('index.html')

@app.route('/service-worker.js')
def sw():
    return app.send_static_file('service-worker.js')

if __name__ == '__main__':
   app.run(host= '0.0.0.0',port= 5030,debug=True	)