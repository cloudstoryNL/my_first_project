from flask import Flask

app = Flask(__name__)

@app.Route('/')
def hello():
    return '<h1>Hello, World!</h1>'