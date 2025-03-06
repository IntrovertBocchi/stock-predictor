# Import yfinance library to fetch stock data from yahoo finance
import yfinance as yf

# Import pandas for data manipulation and saving to CSV
import pandas as pd

# Function to fetch stock data
def get_stock_data(ticker, start="2020-01-01", end="2025-01-01"):

      # This function fetches historical stock data for a given ticker symbol 

    # It takes three parameters: ticker (str), start (str), end (str)

    # ticker - this is the stock ticker symbol (i.e AAPL for apple)
    # start - start date for data retrieval (default: "2020-01-01")
    # end - end date for data retrieval (default: "2025-01-01")

    # DataFrame using pandas that contain historical stock data

    # Download stock data from yahoo finance using yfinance
    stock = yf.download(ticker, start=start, end=end)

  
    # save stock data as a CSV file in the "data" directory
    # file will be named after stock ticker (e.g., "AAPL.csv")
    stock.to_csv(f"data/{ticker}.csv") 

    # Return the downloaded stock data as a DataFrame
    return stock

# Main execution block to run the script directly
if __name__ == "__main__":

    # Fetch stock data for Apply Inc. ("AAPL")
    df = get_stock_data("AAPL")

    # Print the first five rows of the downloaded stock data
    print(df.head())