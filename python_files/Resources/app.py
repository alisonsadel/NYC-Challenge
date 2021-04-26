import os 
from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
import matplotlib.pyplot as plt 
import numpy as np 
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/final_project"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

def __str__(self):
    return self.crime

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/loader',methods=['POST'])
def loader():  

    return render_template('loader.html', prediction_text='Sales should be $ {}'.format(output))

# ,methods=['POST']

@app.route('/dashboard')
def results():

    results = db.session.execute("SELECT * FROM crime")
    print(results) #only for test
    return render_template('dashboard.html', results = results)

    #need code that runs the linear regression

    #need code that runs the random forest 

    #need code that runs a map
    
    # Redirect results to the dashboard page
    # return redirect("/dashboard")

if __name__ == "__main__":
    app.run(debug=True)