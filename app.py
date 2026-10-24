from flask import Flask
import requests
app = Flask(__name__)

@app.route('/')
def home():
    try:
        price = requests.get("https://api.gold-api.com/price/XAU", timeout=5).json()['price']
    except:
        price = 2645.0
    
    if price > 2650:
        box = f"<div style='background:green;color:white;padding:50px;font-size:40px;border-radius:20px'>🚀 BUY NOW<br>{price}<br>0.03 + 0.02 لوت</div>"
    elif price < 2630:
        box = f"<div style='background:red;color:white;padding:50px;font-size:40px;border-radius:20px'>🔻 SELL NOW<br>{price}<br>0.03 + 0.02 لوت</div>"
    else:
        box = f"<div style='background:#333;color:white;padding:50px;font-size:30px;border-radius:20px'>انتظار كسر<br>{price}<br>READY</div>"
    
    return f"<html><head><meta http-equiv='refresh' content='20'><meta name='viewport' content='width=device-width, initial-scale=1'></head><body style='text-align:center;font-family:Arial;padding:20px'><h3>Account 474792960</h3>{box}<p>يتحدث كل 20 ثانية</p></body></html>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)