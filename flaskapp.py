from flask import Flask
app = Flask(__name__)

@app.route('/root')
def helloflask():
	return 'hello flask'

#helloflask()

@app.route('/greet/<name>')
def greet(name):
	return "Hello %s" % name

#greet("chever")
