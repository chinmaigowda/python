from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome Chandan!!!!'

@app.route('/name')
def name():
	return 'amazon.com'

if __name__ == '__main__':
	app.run(host="0.0.0.0",port="8080")
