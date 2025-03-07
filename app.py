from flask import Flask, render_template, request, jsonify
import yfinance as yf
from src.model import train_model
import requests

app = Flask(__name__)

YAHOO_FINANCE_API = "https://query2.finance.yahoo.com/v1/finance/search"

# Function to search for a stock symbol by name
def get_stock_symbol(query):

    try:
        
        ticker = yf.Ticker(query)
        stock_info = ticker.info

        #If a valid symbol exists, return it
        symbol = stock_info.get("symbol", None)
        if symbol:
            return symbol
        
    except Exception as e:
        print(f"error retrieving stock symbol: {e}")

    return None #return none if not found    

def get_stock_country(symbol):
    
    try:
        
        ticker = yf.Ticker(symbol)
        stock_info = ticker.info
        
        return stock_info.get("country", "Unknown")  # Get country, default to "Unknown"
    
    except Exception as e:
        
        print(f"Error retrieving stock country: {e}")
        
        return "Unknown"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    query = request.args.get("query", "")
    
    if not query:

        return jsonify([])
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    params = {"q": query, "lang": "en-US", "region": "US"}
    
    try:
        response = requests.get(YAHOO_FINANCE_API, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()

    except requests.RequestException as e:
         return jsonify({"error": str(e)})
    
    stocks = [
        {"symbol": item["symbol"], "name": item["shortname"], "region": get_stock_country(item["symbol"])}
        for item in data.get("quotes", [])
        if "symbol" in item and "shortname" in item
    ]

    return jsonify(stocks)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    tickers = data.get("tickers", [])

    predictions = []
    for ticker in tickers:
        
        ticker_symbol = get_stock_symbol(ticker) # Convert name to symbol

        if not ticker_symbol:
            predictions.append({"ticker": ticker, "error": "Symbol not found"})
            continue

        try:

            stock=yf.download(ticker_symbol, period="1d")
            price = float(stock["Close"].iloc[-1].item()) if not stock.empty else None
            predictions.append({"ticker": ticker_symbol, "prediction": price})
            
        except Exception as e:

            predictions.append({"ticker": ticker, "error": str(e)})

    return jsonify({"predictions": predictions})

if __name__ == "__main__":
    app.run(debug=True)
