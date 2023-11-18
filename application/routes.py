from application import app
from flask import jsonify, request

@app.route("/")
def index():
    return "Hello World"


