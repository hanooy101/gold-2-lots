from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Gold Bot 0.03 + 0.02 | Account 474792960 | READY for XAUUSD BUY/SELL"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
