import streamlit as st
import numpy as np
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

# ==============================
# Load model and scaler
# ==============================
model = load_model("monthly_rainfall_lstm.h5")
scaler = joblib.load("rainfall_scaler.pkl")

months = ["Jan","Feb","Mar","April","May","June",
          "July","Aug","Sept","Oct","Nov","Dec"]

# ==============================
# Page config
# ==============================
st.set_page_config(
    page_title="Chennai Rainfall Intelligence",
    layout="centered"
)

st.title("🌧️ Chennai Monthly Rainfall Prediction Dashboard")
st.markdown("AI-powered rainfall forecasting using LSTM Neural Network")

st.divider()

# ==============================
# Input
# ==============================
st.subheader("Enter last 12 months rainfall (mm)")

inputs = []

cols = st.columns(4)

for i in range(12):
    with cols[i % 4]:
        val = st.number_input(
            f"{months[i]}",
            min_value=0.0,
            max_value=1000.0,
            value=50.0
        )
        inputs.append(val)

# ==============================
# Predict
# ==============================
if st.button("🔮 Predict Next 12 Months Rainfall"):

    input_array = np.array(inputs).reshape(-1,1)
    scaled_input = scaler.transform(input_array)
    scaled_input = scaled_input.reshape(1,12,1)

    future = []
    current = scaled_input[0]

    for _ in range(12):
        pred = model.predict(current.reshape(1,12,1))
        future.append(pred[0][0])
        current = np.append(current[1:], pred, axis=0)

    future = np.array(future).reshape(-1,1)
    future_rain = scaler.inverse_transform(future)

    # ==============================
    # Table
    # ==============================
    st.subheader("📊 Predicted Monthly Rainfall")

    result_df = pd.DataFrame({
        "Month": months,
        "Rainfall (mm)": future_rain.flatten().round(2)
    })

    st.dataframe(result_df, use_container_width=True)

    # ==============================
    # Graph
    # ==============================
    st.subheader("📈 Rainfall Forecast Trend")

    fig, ax = plt.subplots(figsize=(10,4))
    ax.plot(months, future_rain, marker="o")
    ax.set_xlabel("Month")
    ax.set_ylabel("Rainfall (mm)")
    ax.set_title("Predicted Monthly Rainfall (Next Year)")
    ax.grid(True)

    st.pyplot(fig)

    # ==============================
    # Insights
    # ==============================
    total = future_rain.sum()

    st.subheader("🔍 AI Insight")

    if total > 1400:
        st.warning("⚠️ High rainfall year — possible flood risk")
    elif total < 900:
        st.error("🚨 Low rainfall year — drought risk")
    else:
        st.success("✅ Normal rainfall year expected")
