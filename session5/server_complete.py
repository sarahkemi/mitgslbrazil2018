from flask import Flask
from flask import request, jsonify

app = Flask(__name__)

todo_list = ['iron clothes','do programming hw','build a startup']


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/todos', methods=['GET'])
def todos():
    return jsonify(todo_list)


@app.route('/add', methods=['PUT'])
def add_todo():
    if request.method == 'PUT':
        json = request.get_json()
        if 'todo' in json.keys():
            todo_list.append(json['todo'])
            return jsonify('todo ({}) added'.format(json['todo']))
    return jsonify('error when adding todo')


@app.route('/delete', methods=['DELETE'])
def delete_todo():
    if request.method == 'DELETE':
        json = request.get_json()
        if 'todo' in json.keys():
            if json['todo'] in todo_list:
                todo_list.remove(json['todo'])
                return jsonify('todo ({}) deleted'.format(json['todo']))
    return jsonify('error when deleting todo')


if __name__ == "__main__":
    app.run(debug=True)