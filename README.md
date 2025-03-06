# 📈 AI-Powered Stock Trend Predictor

# Overview  

This project is a **machine-learning based stock trend predictor** that utilizes a **Random Forest regression** to forecast future stock prices based on historical data. The model is trained on real stock market data and is accessible using a **Flask Web App**, allowing users to input stock symbols and receive a predicted closing price.

# Features

Predicts stock closing prices using machine learning (Random Forest)
Fetches real-time stock data from Yahoo Finance (yfinance)
Simple **Flask web interface** for user input
Supports **multiple stock symbols** (Not just AAPL)
Interactive charts to illustrate stock trends (Planned)
JavaScript enhancements for better UI/UX (Planned)
**Temporary CSV storage** to manage stock data efficiently (Planned)

# Project structure
```
├── data/           # Stores stock data CSVs
├── models/         # Trained ML models
├── src/            # Source code
│   ├── data_loader.py  # Fetches stock data
│   ├── model.py        # ML model training & prediction
├── static/         # CSS, JavaScript (Planned)
├── templates/      # HTML files for Flask
│   ├── index.html      # Web UI
├── app.py          # Flask web app
├── requirements.txt # Dependencies
├── README.md       # Project documentation
```

# Tech stacks

Backend: Python (Flask, Pandas, Scikit-learn, yfinance)
Machine Learning: Random Forest Regression
Frontend: HTML, CSS (JavaScript Planned)
Data Visualization: Matplotlib, Seaborn (Planned)

# Installation and Setup

1. Clone the repository
   
```
git clone https://github.com/IntrovertBocchi/stock-predictor.git
cd stock-predictor
```

2. Create a virtual environment

```
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

4. Install dependencies

```
pip install -r requirements.txt
```

6. Run the application

```
python app.py
```

8. Open in your browser

```
http://127.0.0.1:5000/
```

# Planned Improvements

Multi-Stock support: Allows user to compare different stock symbols and choose stocks.
Graphs and charts: Intergrate matplotlib and Plotly.js to vvisualize stock trends
Javascript enhancements: Improve UI with dynamic updates and animations
Temporary CSV storage: Manage stock data more efficiently 

# Contributing

Pull requests are welcome! Feel free to suggest improvements or report issues :D

# License

This project is licensed under **MIT License**
