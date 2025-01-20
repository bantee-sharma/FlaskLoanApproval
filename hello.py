from flask import Flask

app = Flask(__name__)

#API end points
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ping")
def hello_ping():
    return {'message':'hello ping me'}
