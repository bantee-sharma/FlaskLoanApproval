from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/predict")
def flask():
    return "Welcome to FLASK"