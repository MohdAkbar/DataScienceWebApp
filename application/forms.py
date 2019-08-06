from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField,IntegerField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField,FileAllowed

class ClassifyFlowers(FlaskForm):
    sepalLength=StringField('Sepal Length',validators=[DataRequired()])
    sepalWidth=StringField('Sepal Width',validators=[DataRequired()])
    petalLength=StringField('Petal Length',validators=[DataRequired()])
    petalWidth=StringField('Petal Width',validators=[DataRequired()])
    submit=SubmitField('Classify')

class LoanPredictor(FlaskForm):
    loanID=StringField('Loan Id',validators=[DataRequired()])
    gender=SelectField('Gender',choices=[('Male','Male'),('Female','Female')])
    married=SelectField('Married',choices=[('1','Yes'),('0','No')])
    dependents=StringField('Dependents',validators=[DataRequired()])
    education=SelectField('Education',choices=[('1','Graduate'),('0','Not Graduate')])
    selfEmployed=SelectField('Self Employed',choices=[('1','Yes'),('0','No')])
    applicantIncome=IntegerField('Applicant Income')
    coApplicantIncome=IntegerField('Co Applicant Income')
    loanAmount=IntegerField('Loan Amount',validators=[DataRequired()])
    loanAmountTerm=IntegerField('Loan Amount Term',validators=[DataRequired()])
    creditHistory=SelectField('Credit History',choices=[('1','Yes'),('0','No')])
    propertyArea=SelectField('Property Area',choices=[('0','Rural'),('1','Semi Urban'),('2','Urban')])
    submit=SubmitField('Predict')
