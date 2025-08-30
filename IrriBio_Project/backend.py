from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)
file_path = "sensor_data.csv"

@app.route("/latest")
def latest_data():
    if not os.path.exists(file_path):
        return jsonify({"error": "No data found"}), 404
    df = pd.read_csv(file_path)
    latest = df.iloc[-1].to_dict()
    return jsonify(latest)

@app.route("/history")
def history():
    if not os.path.exists(file_path):
        return jsonify({"error": "No data found"}), 404
    df = pd.read_csv(file_path)
    return jsonify(df.tail(20).to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
