from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Koneksi ke MongoDB Atlas
MONGO_URI = "mongodb+srv://cettaanantamaulana:C1090_N2493@cettaan.6it1n.mongodb.net/?retryWrites=true&w=majority&tls=true&tlsAllowInvalidCertificates=true"

# Inisialisasi koneksi ke MongoDB
client = MongoClient(MONGO_URI)

# Pilih database dan koleksi
db = client["Tim_Odyssey"]
collection = db["Info"]

# Endpoint untuk menerima data dari ESP32
@app.route('/receive_data', methods=['POST'])
def receive_data():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400

        # Simpan data ke MongoDB
        result = collection.insert_one(data)
        return jsonify({"message": "Data stored successfully", "id": str(result.inserted_id)}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
