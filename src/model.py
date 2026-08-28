import xgboost as xgb
from sklearn.metrics import mean_absolute_error
import numpy as np
def create_fit_model(train_X,train_y,test_X,test_y):
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
def residual_calculation(model, X_test, y_test):
    predictions = model.predict(X_test)
    residual=y_test-predictions
    residual_std=np.std(residual)
    return residual_std

