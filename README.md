# 🌍 Global Stock Tracker

A real-time stock market tracking application built with **Streamlit** and **YFinance**. Monitor Indian and US market stocks with live price updates, trend analysis, and interactive visualizations.

---

## ✨ Features

- 📊 **Real-Time Stock Data** - Fetch live stock prices using Yahoo Finance API
- 🇮🇳 **Indian Market Support** - Access NSE (National Stock Exchange) stocks with `.NS` suffix
- 🇺🇸 **US Market Support** - Track NASDAQ and NYSE stocks
- 📈 **Price Trend Charts** - Visualize 30-day price trends with interactive line charts
- 💹 **Price Change Indicators** - View percentage change with color-coded metrics
- 📋 **Recent Price History** - Display last 5 closing prices in a data table
- 🎯 **Easy Stock Selection** - Dropdown menu for quick stock selection

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/neha169/Global-Stock-Tracker.git
   cd Global-Stock-Tracker
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 📦 Requirements

Create a `requirements.txt` file with:

```
streamlit==1.28.1
yfinance==0.2.32
pandas==2.0.3
```

Or install directly:
```bash
pip install streamlit yfinance pandas
```

---

## 🎮 Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

### How to Use

1. **Select a Stock** - Use the dropdown menu to choose from available companies
2. **View Current Price** - See the latest closing price and percentage change
3. **Check Recent Prices** - Review the last 5 closing prices in table format
4. **Analyze Trends** - View a 30-day price trend chart

---

## 📊 Supported Stocks

### 🇮🇳 Indian Market (NSE)

| Company | Ticker |
|---------|--------|
| Nifty 50 Index | ^NSEI |
| Reliance Industries | RELIANCE.NS |
| TCS (IT Sector) | TCS.NS |
| HDFC Bank | HDFCBANK.NS |
| SBI (State Bank) | SBIN.NS |
| Infosys | INFY.NS |
| Zomato | ETERNAL.NS |
| Tata Motors - Commercial | TMCV.NS |
| Tata Motors - Passenger | TMPV.NS |

### 🇺🇸 US Market (NASDAQ/NYSE)

| Company | Ticker |
|---------|--------|
| Apple | AAPL |
| Google (Alphabet) | GOOGL |
| Microsoft | MSFT |
| Nvidia (AI) | NVDA |
| Tesla | TSLA |
| Amazon | AMZN |

---

## 🛠️ Technologies Used

- **Streamlit** - Fast web app framework for data visualization
- **YFinance** - Free Yahoo Finance API for stock data
- **Pandas** - Data manipulation and analysis
- **Python** - Core programming language

---

## 📝 Example Workflow

1. Launch the app
2. Select "Apple" from the dropdown
3. View current AAPL price and 30-day percentage change
4. Check recent closing prices in the table
5. Analyze the price trend from the interactive chart
6. Select another stock to compare

---

## ���� Customization

### Add More Stocks

Edit the `stock_options` dictionary in the code:

```python
stock_options = {
    "Your Company": "TICKER.NS",  # For Indian stocks
    "US Company": "TICKER",        # For US stocks
}
```

### Modify Time Period

Change the data history period:
```python
df = data.history(period="3mo")  # 3 months instead of 1
```

---

## ⚠️ Notes

- **Indian Stocks**: Must use `.NS` suffix (e.g., `RELIANCE.NS`)
- **US Stocks**: Use standard ticker symbols (e.g., `AAPL`)
- **Data Availability**: Requires internet connection to fetch live data
- **Market Hours**: Real-time data reflects market trading hours

---

## 🌐 Live Demo

**Try it now:** https://global-stock-tracker-9osft3xtgmf94oknjywyfx.streamlit.app/

---

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- Add more stocks to the tracking list
- Improve the UI/UX
- Add new features (alerts, comparisons, etc.)
- Fix bugs or optimize code

---

## 📄 License

This project is open source and available under the MIT License.

---

## 💡 Future Enhancements

- 📱 Price alerts and notifications
- 📊 Portfolio comparison tool
- 💰 Historical data export
- 🔔 Email/SMS alerts
- 📈 Technical indicators (RSI, MACD, etc.)

---

## 🙋 Support

For issues or questions, please open a GitHub issue or contact the maintainer.

---

**Built with ❤️ using Python, YFinance API, and Streamlit.**
