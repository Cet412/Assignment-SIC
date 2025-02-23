import network
import urequests
import time
import dht
from machine import Pin

# Konfigurasi WiFi
SSID = "Infinix NOTE 30"
PASSWORD = "10902493"

# Konfigurasi Ubidots
UBIDOTS_TOKEN = "BBUS-UjHRHwATDTiBaDbqb9ZREBg4FpDOxb"
DEVICE_LABEL = "esp32"
UBIDOTS_URL = f"http://industrial.api.ubidots.com/api/v1.6/devices/{DEVICE_LABEL}/"

# Konfigurasi Flask Server
FLASK_URL = "http://192.168.46.88:5000/receive_data"  # Sesuaikan dengan IP Flask

# Inisialisasi Sensor DHT11
sensor = dht.DHT11(Pin(4))  # DHT11 terhubung ke GPIO4

# Koneksi ke WiFi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        print("Menghubungkan ke WiFi...")
        time.sleep(1)
    print("Terhubung ke WiFi:", wlan.ifconfig())

# Kirim data ke Ubidots
def send_to_ubidots(temp, humidity):
    headers = {
        "Content-Type": "application/json",
        "X-Auth-Token": UBIDOTS_TOKEN
    }
    data = {
        "temperature": {"value": temp},
        "humidity": {"value": humidity}
    }
    response = urequests.post(UBIDOTS_URL, json=data, headers=headers)
    print("Response Ubidots:", response.text)
    response.close()

# Kirim data ke Flask
def send_to_flask(temp, humidity):
    headers = {"Content-Type": "application/json"}
    data = {
        "temperature": temp,
        "humidity": humidity
    }
    try:
        response = urequests.post(FLASK_URL, json=data, headers=headers)
        print("Response Flask:", response.text)
        response.close()
    except Exception as e:
        print("Gagal mengirim data ke Flask:", e)

# Main loop
connect_wifi()
while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        humidity = sensor.humidity()

        print(f"Suhu: {temp}°C | Kelembapan: {humidity}%")

        # Kirim ke Ubidots & Flask
        send_to_ubidots(temp, humidity)
        send_to_flask(temp, humidity)

    except Exception as e:
        print("Error:", e)
    
    time.sleep(10)  # Kirim data setiap 10 detik
