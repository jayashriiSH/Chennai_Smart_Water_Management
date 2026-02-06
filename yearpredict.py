import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score



df = pd.read_csv("chennai_water_2019_2025_zonewise_dataset.csv")

df.head()



features = [
    "baseline_supply_2019",
    "baseline_usage_2019",
    "rainfall_mm",
    "reservoir_level_percent",
    "population_growth_factor",
    "heat_index"
]


X = df[features]
y = df["derived_demand"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)
model = RandomForestRegressor(
    n_estimators=300,
    max_depth=14,
    min_samples_split=4,
    random_state=42
)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Absolute Error (MLD):", round(mae, 2))
print("R2 Score:", round(r2, 3))


importance = pd.Series(
    model.feature_importances_,
    index=features
).sort_values(ascending=False)

plt.figure(figsize=(10,5))
importance.plot(kind="bar")
plt.title("Feature Importance - Water Demand Prediction")
plt.ylabel("Importance")
plt.show()



sample = X.iloc[-1:].copy()

# simulate next year
sample["population_growth_factor"] *= 1.017
sample["heat_index"] *= 1.05
sample["rainfall_mm"] = 1100

predicted_demand = model.predict(sample)

print("Predicted Water Demand:", round(predicted_demand[0],2), "MLD")
