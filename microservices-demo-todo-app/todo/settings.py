import os

DEBUG = True
SVC_HOST = "0.0.0.0"
SVC_PORT = 5001

# Dependencies
SVC_ENDPOINT_USERS = os.environ.get('SVC_ENDPOINT_USERS', "http://127.0.0.1:5000")

