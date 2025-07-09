from flask import Flask, request
import pickle

file = open("classifier.pkl","rb")
model = pickle.load(file)

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world"

@app.route("/predict")
def hii():
    return "Welcome to flask"