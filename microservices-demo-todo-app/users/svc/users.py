from flask import Flask, jsonify, make_response
import json
import os
import requests

import settings


app = Flask(__name__)


DB_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
with open('{}/db/users.json'.format(DB_PATH), "r") as jsf:
    USERS_LIST = json.load(jsf)
    
    
@app.route("/", methods=['GET'])
def root():
    """Greeting"""
    return "TodoApp: users service is up"


@app.route('/users', methods=['GET'])
def user_list():
    """Returns the list of users"""
    resp = make_response(json.dumps(USERS_LIST, sort_keys=True, indent=4))
    resp.headers['Content-Type']="application/json"
    return resp


@app.route('/users/<username>', methods=['GET'])
def user_data(username):
    """Returns info about a specific user"""
    if username not in USERS_LIST:
        return "User not found"
    return jsonify(USERS_LIST[username])


@app.route('/users/<username>/todo', methods=['GET'])
def user_todo_list(username):
    """Returns all todo items of a user"""
    try:
        req = requests.get("%(svc_endpoint)s/todo/%(username)s" % {
            'svc_endpoint': settings.SVC_ENDPOINT_TODO,
            'username': username
        })
    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    text = req.text
    
    try:
        todos = json.loads(text)
        return jsonify(todos)
    except Exception:
        return text


def main():
    app.run(host=settings.SVC_HOST, port=settings.SVC_PORT,
            debug=settings.DEBUG)
    

if __name__ == '__main__':
    main()

