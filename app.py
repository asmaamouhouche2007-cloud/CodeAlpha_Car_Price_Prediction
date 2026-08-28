import os 
from dotenv import load_dotenv
from flask import render_template,redirect,request,Flask,flash,url_for
from src.predict import predict
import pandas as pd
load_dotenv()
app=Flask(__name__)
app.config['SECRET_KEY']=os.environ.get('SECRET_KEY')

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=('POST',))
def make_prediction():
    try:
        new_car = {
            'Car_Name': request.form['Car_Name'],
            'Year': int(request.form['Year']),
            'Present_Price': float(request.form['Present_Price']),
            'Driven_kms': int(request.form['Driven_kms']),
            'Fuel_Type': request.form['Fuel_Type'],
            'Selling_type': request.form['Selling_type'],
            'Transmission': request.form['Transmission'],
            'Owner': int(request.form['Owner'])
        }
        new_data=pd.DataFrame([new_car],index=[0])
        lower_bound,upper_bound=predict(new_data)
        return render_template('result.html',lower_bound=f'{lower_bound}',upper_bound=f'{upper_bound}')
    except Exception as e:
        flash(f'Error in Making Prediction :{str(e)}','danger')
        return render_template(url_for('home'))
if __name__=='__main__':
    app.run(port=5002)   
