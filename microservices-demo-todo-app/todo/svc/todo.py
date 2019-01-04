from flask import Flask, jsonify, make_response
import json
import os

import settings


app = Flask(__name__)


DB_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
with open('{}/db/todo.json'.format(DB_PATH), "r") as jsf:
    TODO_LIST = json.load(jsf)


@app.route('/', methods=['GET'])
def root():
    """Greeting"""
    return "TodoApp: todo service is up"


@app.route('/todo', methods=['GET'])
def todo_list():
    """Returns all the todo items"""
    todos = []
    for username in TODO_LIST:
        for lname in TODO_LIST[username]:
            todos.append(lname)
    return jsonify(lists=todos)


@app.route('/todo/<username>', methods=['GET'])
def user_todo_list(username):
    """Returns all the todo items of a user"""
    if username not in TODO_LIST:
        return "No ToDo found"
    return jsonify(TODO_LIST[username])


def main():
    app.run(host=settings.SVC_HOST, port=settings.SVC_PORT,
            debug=settings.DEBUG)
    

if __name__ == '__main__':
    main()

