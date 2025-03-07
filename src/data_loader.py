# Import yfinance library to fetch stock data from yahoo finance
import yfinance as yf

# Import pandas for data manipulation and saving to CSV
import pandas as pd

import os

import time

DATA_DIR = "data/"

CACHE_EXPIRY = 3600 #Cache expiration time in seconds (1 hour)

# Function to fetch stock data
def get_stock_data(ticker, start="2020-01-01", end="2025-01-01"):
  
  csv_path = f"{DATA_DIR}{ticker}.csv"

  # Check if CSV exists and is recent
  if os.path.exists(csv_path):
     
    file_age = time.time() - os.path.getmtime(csv_path)
    
    if file_age < CACHE_EXPIRY:
      
      print(f"Using cached data for {ticker}")

      return pd.read_csv(csv_path, index_col=0, parse_dates=["Date"])

  # Fetch new data if cache is expired or doesn't exist
  print(f"Fetching new data for {ticker}...")

  # Download stock data from yahoo finance using yfinance
  stock = yf.download(ticker, start=start, end=end)

  # save stock data as a CSV file in the "data" directory
  # file will be named after stock ticker (e.g., "AAPL.csv")
  stock.to_csv(f"data/{ticker}.csv") 

  # Return the downloaded stock data as a DataFrame
  return stock

def clean_old_data():

    for file in os.listdir(DATA_DIR):

        file_path = os.path.join(DATA_DIR, file)

        if os.path.isfile(file_path):

            file_age = time.time() - os.path.getmtime(file_path)

            if file_age > CACHE_EXPIRY:
               
               os.remove(file_path)

               print(f"Deleted old cache file: {file}")

# Run cleanup before fetching new data

clean_old_data

# Main execution block to run the script directly
if __name__ == "__main__":

    # Fetch stock data for Apply Inc. ("AAPL")
    df = get_stock_data("AAPL")

    # Print the first five rows of the downloaded stock data
    print(df.head())