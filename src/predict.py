import pandas as pd
import joblib 
from src.preprocessing import clean_data
import sqlite3
from src.model import residual_calculation
from datetime import datetime
def get_db_connection():
    """helper function that creates a connection to the database of predictions"""
    conn=sqlite3.connect('predictions.db')
    conn.row_factory = sqlite3.Row
    return conn
def predict(new_data):
    model=joblib.load('models/trained_model.pkl')
    preprocessor = joblib.load('models/preprocessor.pkl')
    to_predict=new_data.copy()
    to_predict=clean_data(preprocessor,to_predict)
    prediction=model.predict(to_predict)[0]
    
    # connect to the database to store the new data 
    new_data=new_data.iloc[0]
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute('INSERT INTO prediction_logs'\
    ' (prediction_date,Car_Name,Year,Present_Price,Driven_kms,Fuel_Type,Selling_type,'\
    'Transmission,Owner,Predicted_Price) VALUES(?,?,?,?,?,?,?,?,?,?)',\
    (datetime.now(),new_data.Car_Name,new_data.Year,new_data.Present_Price,\
     new_data.Driven_kms,new_data.Fuel_Type,new_data.Selling_type,new_data.\
     Transmission,new_data.Owner,prediction))
    conn.commit()
    conn.close()
    return prediction
