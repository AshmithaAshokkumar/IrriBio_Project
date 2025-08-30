import React, { useEffect, useState } from "react";

function Dashboard() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/latest")
      .then((res) => res.json())
      .then((data) => setData(data));
  }, []);

  return (
    <div style={{ textAlign: "center", marginTop: "20px" }}>
      <h1>🌱 IrriBio - Smart Irrigation</h1>
      {data ? (
        <>
          <h2>Soil Moisture: {data.Soil_Moisture}%</h2>
          <h2>Temperature: {data.Temperature}°C</h2>
          <h2>Humidity: {data.Humidity}%</h2>
          <h2>Microbial CO₂: {data.Microbial_CO2} ppm</h2>
          <h2 style={{ color: data.Irrigation_Needed ? "red" : "green" }}>
            {data.Irrigation_Needed ? "🚨 Irrigation Needed!" : "✅ No Irrigation Needed"}
          </h2>
        </>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

export default Dashboard;
