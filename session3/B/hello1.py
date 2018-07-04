from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/recipe', methods=['GET'])
def recipe():
	title = request.args.get('title')
	description = request.args.get('desc')
	directions = request.args.get('dir')
	return render_template('recipe.html', title=title, directions=directions, description=description)