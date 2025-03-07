# 📈 AI-Powered Stock Trend Predictor

# 🚀 Overview  

This project is a **machine-learning-based stock trend predictor** that utilizes a **Random Forest regression model** to forecast future stock prices based on historical data. It fetches real-time stock market data from **Yahoo Finance** and presents predictions through a **Flask Web App**.  

# ✨ Features

✅ **Search for company stocks** instead of manually entering stock symbols (e.g., "Apple" instead of "AAPL")  <br>
✅ **Company names now display country information** if available <br> 
✅ **Efficient temporary CSV storage**—data won’t take up unnecessary space on your PC <br> 
✅ Predicts stock closing prices using machine learning (Random Forest) <br>
✅ Fetches real-time stock data from Yahoo Finance (yfinance) <br>
✅ Simple **Flask web interface** for user input <br>
✅ Supports **multiple stock symbols** (Not just AAPL) <br>
✅ Interactive charts to illustrate stock trends (Planned) <br>
✅ JavaScript enhancements for better UI/UX (Planned) <br>
✅**Temporary CSV storage** to manage stock data efficiently (Planned)

# 🏗️ Project structure
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

# 📊 Tech stacks

🔹 Backend: Python (Flask, Pandas, Scikit-learn, yfinance) <br>
🔹 Machine Learning: Random Forest Regression <br>
🔹 Frontend: HTML, CSS (JavaScript Planned) <br>
🔹 Data Visualization: Matplotlib, Seaborn (Planned) <br>

# 📦 Installation and Setup

1️⃣ Clone the repository
   
```
git clone https://github.com/IntrovertBocchi/stock-predictor.git
cd stock-predictor
```

2️⃣ Create a virtual environment

```
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

3️⃣ Install dependencies

```
pip install -r requirements.txt
```

4️⃣ Run the application

```
python app.py
```

5️⃣ Open in your browser

```
http://127.0.0.1:5000/
```

# 🔮 Planned Improvements

✅ Multi-Stock support: Allows user to compare different stock symbols and choose stocks. <br>
✅ Graphs and charts: Intergrate matplotlib and Plotly.js to vvisualize stock trends. <br>
✅ JavaScript & SCSS UI Enhancements – Improve user experience with dynamic updates, animations & a modern design <br>
✅ ~~Temporary CSV storage: Manage stock data more efficiently.~~ Already included in the update :D <br> 

# 🤝 Contributing

Pull requests are welcome! Feel free to suggest improvements or report issues :D

# 📜 License

This project is licensed under **MIT License**
