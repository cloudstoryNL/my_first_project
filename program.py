from flask import Flask

app = Flash(__name__)

@app.Route('/')
def hello():
    return '<h1>Hello, World!</h1>'

