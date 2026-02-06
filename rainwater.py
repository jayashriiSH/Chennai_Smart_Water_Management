import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib


df = pd.read_csv("monthly_rainfall_data.csv")

print(df.head())
print(df.columns)


X = df[['Jan','Feb','Mar','April','May','June','July','Aug','Sept','Oct','Nov','Dec']]
y = df['Total']


X = df[['Jan','Feb','Mar','April','May','June','July','Aug','Sept','Oct','Nov','Dec']]
y = df['Total']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)
joblib.dump(model, "chennai_rainfall_model.pkl")
print("Model saved successfully!")

y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MAE:", mae)
print("R2 Score:", r2)

