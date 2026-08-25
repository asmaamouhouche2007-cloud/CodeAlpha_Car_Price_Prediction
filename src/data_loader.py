import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(filepath):
    """Loads the raw car data from a CSV file."""
    df = pd.read_csv(filepath)
    return df

def split_data(df):
    """Splits the data into features (X) and target (y), then into train/test sets."""
    X=df.drop('Selling_Price',axis=1)
    y=df['Selling_Price']
    # splitting data into training data and validation data 
    train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)
    return train_X,val_X,train_y,val_y