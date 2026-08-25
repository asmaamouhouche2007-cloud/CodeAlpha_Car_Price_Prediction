from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

def create_model():
    """Returns a Random Forest Regressor with chosen hyperparameters."""
    return RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)

def evaluate_model(model, X_test, y_test):
    """Evaluates the model using Mean Absolute Error."""
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    return mae