@app.route('/root')
def helloflask():
    return 'hello flask'

@app.route('/greet/<name>')
def greet(name):
	return "Hello %s" % name
