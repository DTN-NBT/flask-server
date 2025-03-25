from flask import Flask, request, jsonify

app = Flask(__name__)

connected_devices = []

@app.route('/register_device', methods=['POST'])
def register_device():
    data = request.json
    connected_devices.append(data)
    print("✅ New device registered:", data)
    return jsonify({'status': 'ok', 'message': 'Device registered successfully'})

@app.route('/devices', methods=['GET'])
def get_devices():
    return jsonify(connected_devices)

@app.route("/")
def home():
    return "🌍 Flask Server is Live!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)

