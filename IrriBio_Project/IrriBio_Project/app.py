# app.py

# Import required libraries
import streamlit as st
import numpy as np
import pandas as pd
import pickle

# ---------------------------
# Load the trained ML model safely
# ---------------------------
model = None
try:
    with open("irribio_model.pkl", "rb") as f:
        model = pickle.load(f)
except Exception as e:
    st.error(f"⚠️ Could not load model file: {e}")
    st.info("👉 Please make sure 'irribio_model.pkl' is in the same folder as app.py")

# ---------------------------
# Title of the dashboard
# ---------------------------
st.title("🌱 IrriBio – Smart Irrigation Simulator")

st.write(
    "This simulator uses soil moisture, microbial CO₂ activity, and temperature "
    "to predict whether irrigation is required."
)

# ---------------------------
# Step 1: Input sliders for simulated sensor data
# ---------------------------
soil = st.slider("🌍 Soil Moisture (%)", min_value=10, max_value=90, value=50)
microbe = st.slider("🦠 Microbial CO₂ (ppm)", min_value=200, max_value=800, value=400)
temp = st.slider("🌡️ Temperature (°C)", min_value=15, max_value=40, value=25)

# ---------------------------
# Step 2: Prepare input DataFrame
# ---------------------------
features = pd.DataFrame(
    [[soil, microbe, temp]],
    columns=["Soil_Moisture", "Microbial_CO2", "Temperature"]
)

# ---------------------------
# Step 3: Predict irrigation need
# ---------------------------
if model is not None:
    try:
        prediction = model.predict(features)[0]

        # Step 4: Display result
        if prediction == 1:
            st.success("✅ Irrigation Needed")
        else:
            st.info("❌ No Irrigation Required")
    except Exception as e:
        st.error(f"⚠️ Prediction failed: {e}")

# ---------------------------
# Step 5: Optional – display a simulated soil moisture trend graph
# ---------------------------
st.subheader("📈 Simulated Soil Moisture Trend (Random Example)")
soil_trend = np.random.randint(10, 90, 20)
st.line_chart(soil_trend)

# ---------------------------
# Footer
# ---------------------------
st.caption("🚀 Powered by IrriBio ML Model")
