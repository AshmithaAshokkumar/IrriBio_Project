# app.py
import streamlit as st
import pandas as pd
import os
import random
import datetime

st.set_page_config(page_title="IrriBio - Smart Irrigation", layout="wide")

st.title("🌱 IrriBio - Smart Irrigation System")

file_path = "sensor_data.csv"

# Function to generate new fake sensor data
def generate_sensor_data():
    new_data = {
        "timestamp": [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        "Soil_Moisture": [random.randint(10, 60)],
        "Temperature": [random.randint(25, 40)],
        "Humidity": [random.randint(40, 70)],
        "Microbial_CO2": [random.randint(300, 600)],
        "Irrigation_Needed": [random.choice([0, 1])]
    }
    df_new = pd.DataFrame(new_data)
    df_new.to_csv(file_path, mode="a", header=not os.path.exists(file_path), index=False)
    return df_new


# Button for farmers to generate fresh data
if st.button("🔄 Generate New Sensor Reading"):
    new_row = generate_sensor_data()
    st.success(f"✅ New sensor data recorded at {new_row['timestamp'].iloc[0]}")

# Check if data exists
if not os.path.exists(file_path):
    st.warning("⚠️ No sensor data available yet. Click 'Generate New Sensor Reading' above.")
else:
    df = pd.read_csv(file_path)

    # Get latest sensor row
    latest = df.iloc[-1]

    # Display sensor values in cards
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("💧 Soil Moisture (%)", latest["Soil_Moisture"])
    col2.metric("🌡️ Temperature (°C)", latest["Temperature"])
    col3.metric("💦 Humidity (%)", latest["Humidity"])
    col4.metric("🦠 Microbial CO₂ (ppm)", latest["Microbial_CO2"])

    st.divider()

    # Irrigation recommendation
    if latest["Irrigation_Needed"] == 1 or latest["Soil_Moisture"] < 30:
        st.error("🚨 Irrigation Needed! Please water the field.")
    else:
        st.success("✅ No Irrigation Needed. Soil is healthy.")

    st.divider()

    # Show last few rows
    st.subheader("📊 Recent Sensor History")
    st.dataframe(df.tail(10))

    # Trend chart
    st.line_chart(df[["Soil_Moisture", "Temperature", "Humidity"]])
