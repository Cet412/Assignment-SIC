Overview

Assignment-SIC is an IoT project that integrates an ESP32-based system with a Flask backend to efficiently collect, transmit, and store environmental and motion sensor data. This system utilizes the DHT11 sensor for temperature and humidity measurements, and the MQ135 sensor for air quality monitoring.

The ESP32 sends real-time data to Ubidots for visualization and analysis, while a Flask-based API ensures seamless data logging in MongoDB Atlas, providing structured storage and easy retrieval.

🔗 Ubidots Dashboard: Click Here

Features:

📡 Real-time data transmission from ESP32 to Ubidots using MQTT/REST API.

🌡 Environmental monitoring with DHT11 (temperature & humidity) and MQ135 (air quality sensor).

📊 Data visualization via Ubidots for easy monitoring.

🗄 Structured data storage in MongoDB Atlas via Flask API.

🛠 Efficient ESP32 programming using MicroPython on VS Code.

Tech Stack:

ESP32 (MicroPython)

DHT11, MQ135

Ubidots (MQTT/REST API)

Flask (Python API Backend)

MongoDB Atlas (Database Storage)

VS Code + Pymakr Plugin
