from flask import Flask

app=Flask(__name__)
app.config['SECRET_KEY']='4791628bb0b13ce0c676dfde280ba786'

from application import routes