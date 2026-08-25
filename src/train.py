import joblib
from src.data_loader import load_data,split_data
from src.preprocessing import data_cleaning,encode_categoricals
from src.model import create_model,evaluate_model
def train():
    # loading the data
    data=load_data('C:/Users/ACER/Downloads/CodeAlpha_Car_Price_Prediction/dataset/car data.csv')
    # data cleaning 
    data=data_cleaning(data)
    data=encode_categoricals(data)
    #splitting data
    train_X,val_X,train_y,val_y=split_data(data)
   
    # creating and fitting the model
    model=create_model()
    model.fit(train_X,train_y)
    # evaluating the model
    mae=evaluate_model(model,val_X,val_y)
    print(f'The absolute errore : {mae:.2f}')
    # saving the trained model 
    joblib.dump(model,'models/trained_model.pkl')
if __name__=='__main__':
    train()   