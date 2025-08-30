# sensor_generator.py
import pandas as pd
import random
import datetime
import os

# Generate fake sensor data
new_data = {
    "timestamp": [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
    "Soil_Moisture": [random.randint(10, 60)],
    "Temperature": [random.randint(25, 40)],
    "Humidity": [random.randint(40, 70)],
    "Microbial_CO2": [random.randint(300, 600)],
    "Irrigation_Needed": [random.choice([0, 1])]
}

df_new = pd.DataFrame(new_data)

# Append new row into sensor_data.csv
file_path = "sensor_data.csv"
df_new.to_csv(file_path, mode="a", header=not os.path.exists(file_path), index=False)

print("✅ New sensor row added:", df_new.to_dict(orient="records")[0])
