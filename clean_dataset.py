import pandas as pd

# -------------------------
# Load raw dataset
# -------------------------
df = pd.read_csv("depot_storage_dataset.csv")

# -------------------------
# Basic cleaning
# -------------------------
df = df[df["number_of_ohts"] > 0]
df = df[df["total_storage_ml"] < 50]   # remove unrealistic outliers

df.reset_index(drop=True, inplace=True)

# -------------------------
# Feature engineering
# -------------------------
df["storage_per_oht"] = (
    df["total_storage_ml"] / df["number_of_ohts"]
)

# -------------------------
# Target creation
# 0 = LOW risk
# 1 = MEDIUM risk
# 2 = HIGH risk
# -------------------------
def shortage_label(x):
    if x < 0.5:
        return 2
    elif x < 1.5:
        return 1
    else:
        return 0

df["shortage_risk"] = df["storage_per_oht"].apply(shortage_label)

# -------------------------
# Save cleaned dataset
# -------------------------
df.to_csv("cleaned_water_ml_dataset.csv", index=False)

print("✅ Cleaned dataset created")
print(df.head())
