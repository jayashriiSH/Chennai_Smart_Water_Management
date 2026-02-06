import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df = pd.read_csv("water_leak.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Features
X = df[
    [
        'Pressure (bar)',
        'Flow Rate (L/s)',
        'Temperature (°C)'
    ]
]

# Target: leak (we'll handle burst separately)
y = df['Leak Status']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier(
    n_estimators=150,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

# Save model
joblib.dump(model, "leak_model.pkl")

print("✅ Water Leak Model Trained Successfully")
y_burst = df['Burst Status']

Xb_train, Xb_test, yb_train, yb_test = train_test_split(
    X, y_burst, test_size=0.2, random_state=42
)

burst_model = RandomForestClassifier(n_estimators=150)
burst_model.fit(Xb_train, yb_train)

joblib.dump(burst_model, "burst_model.pkl")

print("✅ Leak & Burst models trained successfully")
