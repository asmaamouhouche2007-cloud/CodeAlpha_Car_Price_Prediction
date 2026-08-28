import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
'''def data_cleaning(df):
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
    '''
def create_preprocessor(df):
    data=df[['Year', 'Present_Price', 'Driven_kms',
       'Fuel_Type', 'Selling_type', 'Transmission', 'Owner']]
    columns=data.columns
    numerical_columns=data.select_dtypes(exclude='str').columns
    categorical_columns=[ col for col in columns if col not in numerical_columns]
    numerical_transformer=SimpleImputer(strategy='median')
    categorical_transformer=Pipeline(steps=[
    ('imputation',SimpleImputer(strategy='most_frequent')),
    ('onehot',OneHotEncoder(handle_unknown='ignore'))])
    preprocessor=ColumnTransformer(transformers=[
    ('num',numerical_transformer,numerical_columns),
    ('cat',categorical_transformer,categorical_columns)])
    return preprocessor
def clean_training_data(preprocessor,X_train):
        X_train=X_train.drop(columns=['Car_Name'])
        processed_train=preprocessor.fit_transform(X_train)
        return processed_train,preprocessor
def clean_data(preprocessor,X_test):
    X_test=X_test.drop(columns=['Car_Name'])
    processed_test=preprocessor.transform(X_test)
    return processed_test
    
