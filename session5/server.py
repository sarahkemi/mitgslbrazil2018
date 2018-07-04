from flask import Flask
from flask import request, jsonify

app = Flask(__name__)

todo_list = ['iron clothes', 'do programming hw', 'build a startup']


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/todos', methods=['GET'])
def todos():
    return jsonify(todo_list)


@app.route('/add', methods=['PUT'])
def add_todo():
    pass  # add code here


@app.route('/delete', methods=['DELETE'])
def delete_todo():
    pass  # delete code here
