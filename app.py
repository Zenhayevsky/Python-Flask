from flask import Flask 

app = Flask(__name__)

@app.route('/hola')
def hola():
    return "hola"

@app.route('/hi')
def hi():
    return "hi"

app.run()
