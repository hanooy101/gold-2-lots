from flask import Flask, request, jsonify
app = Flask(__name__)
ACCOUNT = 474792960
SERVER = "Exness-MT5Trial15"
LOTS = [0.03, 0.02]
SYMBOL = "XAUUSD"
last_signal = {"status": "READY", "side": None}
@app.route('/')
def home():
    return f"<h2>Gold Bot LIVE</h2><p>Account: {ACCOUNT}</p><p>Lots: {LOTS}</p><p>Status: {last_signal['status']}</p>"
@app.route('/signal', methods=['POST'])
def signal():
    global last_signal
    data = request.get_json() or {}
    side = data.get('side','BUY').upper()
    last_signal = {"status": f"Signal {side} received", "side": side}
    return jsonify({"result":"ok","side":side,"lots":LOTS})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
