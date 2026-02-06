import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

# =========================
# Load data and model
# =========================
df = pd.read_csv("monthly_rainfall_data.csv")
model = joblib.load("chennai_rainfall_model.pkl")

months = ["Jan","Feb","Mar","April","May","June",
          "July","Aug","Sept","Oct","Nov","Dec"]

# =========================
# UI
# =========================
st.set_page_config(page_title="Chennai Rainfall Intelligence", layout="centered")

st.title("🌧️ Chennai Rainfall Prediction & Trend Analysis")

st.divider()

year = st.number_input("Select Year", 1901, 2035, 2025)
month = st.selectbox("Select Month", months)

# =========================
# Monthly rainfall
# =========================
if st.button("🔍 Get Rainfall"):

    if year <= 2021:
        value = df[df["Year"] == year][month].values[0]
        st.success(f"🌧️ Rainfall in {month} {year}: **{value:.2f} mm**")

    else:
        # use average monthly pattern for prediction
        monthly_avg = df[months].mean().values.reshape(1, -1)
        predicted_annual = model.predict(monthly_avg)[0]
        predicted_month = predicted_annual / 12

        st.warning("Predicted (AI Estimated)")
        st.success(f"🌧️ Rainfall in {month} {year}: **{predicted_month:.2f} mm**")

# =========================
# Yearly trend
# =========================
st.divider()
st.subheader("📈 Yearly Rainfall Trend")

yearly_rain = df[["Year","Total"]]

plt.figure(figsize=(10,4))
plt.plot(yearly_rain["Year"], yearly_rain["Total"])
plt.xlabel("Year")
plt.ylabel("Rainfall (mm)")
plt.title("Chennai Annual Rainfall Trend (1901–2021)")
st.pyplot(plt)    