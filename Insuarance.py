import pandas as pd

import pickle

import streamlit as st

pickle_in = open("Insurance_Eligibility_model.pkl","rb")
model= pickle.load(pickle_in)
@st.cache_data()
def prediction(Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome , CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,Property_Area):
    if Gender == 'Male':
        Gender = 1
    elif Gender == 'Female':
        Gender = 0
    if Married == "Yes":
        Married = 1
    elif Married == "No":
        Married = 0
    if Education == "Graduate":
        Education = 0
    elif Education == "Not Graduate":
        Education = 1
    if Self_Employed == "Yes":
        Self_Employed = 1
    elif Self_Employed == "No":
        Self_Employed = 0
    if Property_Area == "Urban":
        Property_Area = 2
    elif Property_Area == "Rural":
        Property_Area = 0
    elif Property_Area == "SemiUrban":
        Property_Area = 1


    prediction = model.predict(pd.DataFrame([[Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome , CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,Property_Area]], columns=['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome','CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History','Property_Area']))
    return prediction[0]

st.title("Insurance Eligibility Predictor")
st.header("Please Enter the Appropriate Values")

Gender = st.selectbox("Gender:",["Male","Female"])
Married = st.selectbox("Married:",["Yes","No"])
Dependents= st.number_input("Dependents:",min_value=0.0, max_value=3.0, value=1.0)
Education = st.selectbox("Education:",["Graduate","Not-Graduate"])
Self_Employed = st.selectbox("Self_Employed:",["Yes","No"])
Property_Area = st.selectbox("Property_Area:",["Urban","Rural","SemiUrban"])
Credit_History=st.number_input("Credit_History:",min_value=0.0,max_value=1.0)
LoanAmount = st.number_input("LoamAmount:'",min_value=0.0,max_value=270.0,value=1.0)
ApplicantIncome = st.number_input("ApplicantIncome:",min_value=0.0,max_value=11100.0,value=1.0)
CoapplicantIncome = st.number_input("CoapplicantIncome:",min_value=0.0,max_value=54167.0,value=1.0)
Loan_Amount_Term = st.number_input("Loan_Amount_Term:",min_value=0.0,max_value=480.0,value=1.0)


if st.button("Predictions"):
    Status = prediction(Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome , CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,Property_Area)
    if Status == 1:
        st.success("Congrats You are Eligible for the Insurance")
    else:
        st.success("You are Not Eligible for the Insurance")