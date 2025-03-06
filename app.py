from flask import Flask, render_template, request
import pandas as pd
import yfinance as yf
from src.model import train_model

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        ticker = request.form["ticker"]
        model = train_model(ticker)
        stock = yf.download(ticker, period="1d")
        features = stock[["Open", "High", "Low", "Close", "Volume"]].values[-1].reshape(1, -1)
        prediction = model.predict(features)[0]

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)