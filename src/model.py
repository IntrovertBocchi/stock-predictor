# Data manipulation and handles CSV files
import pandas as pd

# Numerical operations (not used here)
import numpy as np

# Splitting data into training and testing sets
from sklearn.model_selection import train_test_split

# Machine learning model for regression
from sklearn.ensemble import RandomForestRegressor

# Metric to evaluate model performance
from sklearn.metrics import mean_absolute_error

# Function to load stock data and prepare it for training
def load_data(ticker):

    # Read stock data from CSV file
    df = pd.read_csv(

        # File path based on ticker symbol
        f"data/{ticker}.csv", 

        # First column is the index (date)
        index_col=0, 

        # Convert index column to datetime format
        parse_dates=True,

        # Ensure correct date format
        date_format="%Y-%m-%d"
        )

    # Predict next day's closing price
    df["Future"] = df["Close"].shift(-1)  # Shifts the "Close" column up by one row

    # Remove any rows with missing values due to shifting
    df.dropna(inplace=True)

    # Select features (independent variables) for prediction
    X = df[["Open", "High", "Low", "Close", "Volume"]]

    # Target variables (dependent variables) - next day's closing price
    y = df["Future"]

    # Split data into training and testing sets (80% training, 20% testing)
    return train_test_split(X, y, test_size=0.2, random_state=42)

# Function to train machine learning model
def train_model(ticker):

    # load processed stock data and split into training and testing sets
    X_train, X_test, y_train, y_test = load_data(ticker)

    # Initialize a Random Forest Regressor model with 100 trees
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    
    # Train the model using training data
    model.fit(X_train, y_train)

    # Make predictions on the test set
    preds = model.predict(X_test)

    # Calculate and print Mean Absolute Error (MAE) to evaluate model performance
    error = mean_absolute_error(y_test, preds)

    # Lower MAE indicates better predictions
    print(f"Model MAE: {error:.2f}")

    # Return the trained model
    return model

# Main script execution
if __name__ == "__main__":

    # Train the model using Apple's stock data
    model = train_model("AAPL")