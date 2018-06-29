from flask import Flask
from flask import request


app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello, World!'


@app.route('recipe')
def recipes():
    recipe_title = 'pizza'
    return render_template('recipe.html', title=recipe_title)


@app.route('/recipe_args', methods=['GET'])
def recipes_arg_example():
    return request.args.get('title')
    # this returns 'pizza' if the url is
    # http://127.0.0.1:5000/recipe?title=pizza