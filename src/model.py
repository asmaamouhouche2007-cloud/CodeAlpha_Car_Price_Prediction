import xgboost as xgb
from sklearn.metrics import mean_absolute_error

def create_model(train_X,train_y,test_X,test_y):
    """Returns a xgb model."""
    xgb_model = xgb.XGBRegressor(n_estimators=1000, learning_rate=0.1, random_state=42,early_stopping_rounds=5)
    xgb_model.fit(
    train_X, 
    train_y, 
    eval_set=[(test_X, test_y)],
    verbose=False)
    return xgb_model
    
def evaluate_model(model, X_test, y_test):
    """Evaluates the model using Mean Absolute Error."""
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    return mae