from flask import Flask, render_template, Response
import os
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",message="Hello from service B")

@app.route("/serviceB")
def serviceb():
    return render_template("index.html",message="Hello from service B")

@app.route("/ready")
def ready():
    return Response("OK", 200)

@app.route("/alive")
def alive():
    return Response("OK", 200)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 5000)
