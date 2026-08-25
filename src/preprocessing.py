import pandas as pd

def data_cleaning(df):
    # dropping the non useful column 
    df = df.drop('Car_Name', axis=1)
    # filling missing values with appropriate values 
    df['Fuel_Type']=df['Fuel_Type'].fillna(df['Fuel_Type'].mode()[0])
    df['Selling_type']=df['Selling_type'].fillna(df['Selling_type'].mode()[0])
    df['Transmission']=df['Transmission'].fillna(df['Transmission'].mode()[0])
    df['Present_Price']=df['Present_Price'].fillna(df['Present_Price'].mean())
    df['Driven_kms']=df['Driven_kms'].fillna(df['Driven_kms'].mean())
    df['Owner']=df['Owner'].fillna(df['Owner'].mean())
    df['Year']=df['Year'].fillna(df['Year'].mean())
    return df
def encode_categoricals(df):
    """Converts text categories into numbers using One-Hot Encoding."""
    df = pd.get_dummies(df, columns=['Fuel_Type', 'Selling_type', 'Transmission'], dtype=int)
    return df