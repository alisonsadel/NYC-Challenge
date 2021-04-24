import os 
from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

import matplotlib.pyplot as plt 
import numpy as np 

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():

   

    return render_template('index.html', prediction_text='Sales should be $ {}'.format(output))

# @app.route('/results',methods=['POST'])
# def results():
    
    
    

if __name__ == "__main__":
    app.run(debug=True)