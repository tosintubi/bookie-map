from flask import Flask, jsonify

app = Flask(__name__)


@app.get('/')
def index():
    return 'hello'

@app.get('/hello')
def say_hello():
    return {"message": "Say Hello"}