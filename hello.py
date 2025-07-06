from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/predict",methods = ["GET","POST"])
def flask():
    if request.method == "GET":
        return "Insurance Prediction"