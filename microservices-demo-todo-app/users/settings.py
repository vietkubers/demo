import os

DEBUG = True
SVC_HOST = "0.0.0.0"
SVC_PORT = 5000

# Dependencies
SVC_ENDPOINT_TODO = os.environ.get('SVC_ENDPOINT_TODO', "http://127.0.0.1:5001")

