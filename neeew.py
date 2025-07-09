from flask import Flask, request
import pickle

file = open("classifier.pkl","rb")
model = pickle.load(file)

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world"

@app.route("/predict",methods=["GET","POST"])
def hii():
    if request.method == "GET":
        return "We will make prediction"
    else:
        loan_req = request.get_json()

        if loan_req["Gender"] == "Male":
            Gender = 0
        else:
            Gender = 1

        if loan_req['Married'] == "No":
            Married = 0
        else:
            Married = 1

        ApplicantIncome = loan_req['ApplicantIncome']
        LoanAmount = loan_req['LoanAmount']
        Credit_History= loan_req['Credit_History']           

        input_data = [Gender, Married, ApplicantIncome, LoanAmount, Credit_History]
        result = model.predict([input_data])

        if result == 0:
            pred = "Rejected"
        else:
            pred = "Approved"

        return {"loan_approval_status":pred}

        

   


