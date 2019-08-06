from flask import render_template,url_for,jsonify
from application import app
from application.forms import ClassifyFlowers,LoanPredictor
import os
import pandas as pd
import numpy as np
from sklearn.externals import joblib
import time
from PIL import Image


@app.route('/iris_classification',methods=['GET','POST'])
def iris_classification():
    form=ClassifyFlowers()
    ans='Coming Soon'
    imageName='default'
    if form.validate_on_submit():
        sepalL=float(form.sepalLength.data)
        sepalW=float(form.sepalWidth.data)
        petalL=float(form.petalLength.data)
        petalW=float(form.petalWidth.data)
        ans=updatedFindFlowerClass(sepalL,sepalW,petalL,petalW)
        if ans=='Iris-Setosa':
            imageName='iris_setosa'
        elif ans=='Iris-Versicolor':
            imageName='iris_versicolor'
        elif ans=='Iris-Virginica':
            imageName='iris_virginica'
    return render_template("flower.html",form=form,result=ans,file=imageName)


@app.route('/iris_classification/api/v1.0/attributes/<float:aa>/<float:bb>/<float:cc>/<float:dd>',methods=['GET'])
def irisAPI(aa,bb,cc,dd):
    ans=updatedFindFlowerClass(aa,bb,cc,dd)
    result={'result':ans}
    return jsonify(result)

@app.route('/')
def home():
    return render_template("home.html")


def updatedFindFlowerClass(a,b,c,d):
    filename=os.getcwd()+'\\IrisClassification.sav'
    myModel=joblib.load(filename)
    myPrediction=myModel.predict([[a,b,c,d]])
    flower_class=myPrediction[0]
    flower='No flower'
    if flower_class==0:
        flower='Iris-Setosa'
    elif flower_class==1:
        flower='Iris-Versicolor'
    elif flower_class==2:
        flower='Iris-Virginica'
    return flower


@app.route('/loan_predictor',methods=['GET','POST'])
def loan_predictor():
    form=LoanPredictor()
    imageName='default'
    ans='nothing'
    if form.validate_on_submit():
        myDependents=int(form.dependents.data)
        myEducation=int(form.education.data)
        mySelfEmployed=int(form.selfEmployed.data)
        myApplicantIncome=int(form.applicantIncome.data)
        myCoApplicantIncome=int(form.coApplicantIncome.data)
        myLoanAmount=int(form.loanAmount.data)
        myLoanAmountTerm=int(form.loanAmountTerm.data)
        myCreditHistory=int(form.creditHistory.data)
        myPropertyArea=int(form.propertyArea.data)
        ans=predictLoanStatus(myDependents,myEducation,mySelfEmployed,myApplicantIncome
        ,myApplicantIncome,myCoApplicantIncome,myLoanAmount,myCreditHistory,myPropertyArea)
        if ans=='Approved':
            imageName='Approved'
        else:
            imageName='Rejected'
    return render_template('loan.html',form=form,file=imageName)

def predictLoanStatus(a,b,c,d,e,f,g,h,i):
    filename=os.getcwd()+'\\LoanPredictor.sav'
    myModel=joblib.load(filename)
    myPrediction=myModel.predict([[a,b,c,d,e,f,g,h,i]])
    if myPrediction[0]==1:
        return 'Approved'
    else:
        return 'Rejected'


