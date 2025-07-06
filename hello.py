from flask import Flask,request

# flask --app hello.py run

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/predict",methods = ["GET","POST"])
def flask():
    if request.method == "GET":
        return "Insurance Prediction"
    else:
        return "We are gonna make Prediction"