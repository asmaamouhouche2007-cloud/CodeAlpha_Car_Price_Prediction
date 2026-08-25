CREATE TABLE IF NOT EXISTS prediction_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    prediction_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Car_Name TEXT ,
    Year INTEGER,
    Present_Price REAL,
    Driven_kms REAL,
    Fuel_Type TEXT,
    Selling_type TEXT,
    Transmission TEXT,
    Owner text ,
    Predicted_Price REAL
);
  