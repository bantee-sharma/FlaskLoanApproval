from flask import Flask,request
import pickle

file = open("classifier.pkl","rb")
model = pickle.load(file)

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
        loan = request.get_json()

        if loan["Gender"] == "Male":
            Gender = 0
        else:
            Gender = 1
        
        if loan['Married'] == "No":
            Married = 0
        else:
            Married = 1

        ApplicantIncome = loan['ApplicantIncome']
        LoanAmount = loan['LoanAmount']
        Credit_History= loan['Credit_History'] 


        input_data = [Gender, Married, ApplicantIncome, LoanAmount, Credit_History]
        result = model.predict([input_data])

        if result == 0:
            pred = "Rejected"
        else:
            pred = "Approved"

        return {"loan_approval_status":pred}

