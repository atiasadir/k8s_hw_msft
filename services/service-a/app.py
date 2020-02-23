from flask import Flask, render_template, Response
from yahoo_fin import stock_info as si
from classes.MovingAverage import MovingAverage as ma

app = Flask(__name__)
def get_stock_value(stock_name):
    global movingAverageBitcoin
    try:
        value = round(si.get_live_price(stock_name), 2)
        movingAverageBitcoin.next(value)
        return render_template("stock.html",last_minute=str(value), last_10_average=str(movingAverageBitcoin.average()), stock_name=stock_name)
    except Exception as e:
        print(e)
        return render_template("bad-input.html", stock_name=stock_name)

@app.route("/")
def index():
    return render_template("index.html",message="Hello from service A")

@app.route("/serviceA")
def servicea():
    return get_stock_value("gur_evgeny")

@app.route("/ready")
def ready():
    return Response("OK",200)

@app.route("/alive")
def alive():
    return Response("OK",200)

if __name__ == "__main__":
    movingAverageBitcoin = ma(10)
    app.run(host='0.0.0.0')