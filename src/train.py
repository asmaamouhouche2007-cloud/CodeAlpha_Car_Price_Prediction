import joblib
from src.data_loader import load_data,split_data
from src.preprocessing import create_preprocessor,clean_data,clean_training_data
from src.model import create_fit_model,evaluate_model,residual_calculation
def train():
    # loading the data
    data=load_data('C:/Users/ACER/Downloads/CodeAlpha_Car_Price_Prediction/dataset/car data.csv')
    #splitting data
    train_X,val_X,train_y,val_y=split_data(data)
    # data cleaning 
    preprocessor=create_preprocessor(data)
    train_X,preprocessor=clean_training_data(preprocessor,train_X)
    joblib.dump(preprocessor, 'models/preprocessor.pkl')
    val_X=clean_data(preprocessor,val_X)
    # creating and fitting the model
    model=create_fit_model(train_X,train_y,val_X,val_y)
    # evaluating the model
    mae=evaluate_model(model,val_X,val_y)
    print(f'The absolute errore : {mae:.2f}')
    # saving the trained model 
    joblib.dump(model,'models/trained_model.pkl')
    # residual calculation
    residual_std=residual_calculation(model,train_X,train_y)
    joblib.dump(residual_std, 'models/residual_std.pkl')
if __name__=='__main__':
    train()   