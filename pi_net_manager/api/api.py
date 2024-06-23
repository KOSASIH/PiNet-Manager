from flask import Flask, request, jsonify
from pi_net_manager.core.pi_net_manager import PiNetManager

app = Flask(__name__)

pi_net_manager = PiNetManager()

@app.route("/api/devices", methods=["GET"])
def get_devices():
    devices = pi_net_manager.get_devices()
    return jsonify({"devices": devices})

@app.route("/api/devices/<string:device_id>", methods=["GET"])
def get_device(device_id):
    device = pi_net_manager.get_device(device_id)
    return jsonify({"device": device})

if __name__ == "__main__":
    app.run(debug=True)
