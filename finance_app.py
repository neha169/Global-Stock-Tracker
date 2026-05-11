import streamlit as st
import yfinance as yf
import pandas as pd

st.title("🌍 Global Stock Tracker")

# For Indian stocks, we must use the .NS suffix
stock_options = {
    # --- INDIAN MARKET (NSE) ---
    "Nifty 50 Index": "^NSEI",
    "Reliance Industries": "RELIANCE.NS",
    "TCS (IT Sector)": "TCS.NS",
    "HDFC Bank": "HDFCBANK.NS",
    "SBI (State Bank)": "SBIN.NS",
    "Infosys": "INFY.NS",
    "Zomato": "ETERNAL.NS",
    "Tata Motors - Commercial (TMCV)": "TMCV.NS",
    "Tata Motors - Passenger (TMPV)": "TMPV.NS",
    
    # --- US MARKET (NASDAQ/NYSE) ---
    "Apple": "AAPL",
    "Google (Alphabet)": "GOOGL",
    "Microsoft": "MSFT",
    "Nvidia (AI)": "NVDA",
    "Tesla": "TSLA",
    "Amazon": "AMZN"
}


# Step 2: Use st.selectbox to create the dropdown
selected_name = st.selectbox("Select a Company:", list(stock_options.keys()))

# Step 3: Get the real ticker symbol from your dictionary
ticker = stock_options[selected_name]

# Fetch Data
if ticker:
    data = yf.Ticker(ticker)
    # Get last 1 month of data
    df = data.history(period="1mo")
    
    if not df.empty:
        col1, col2 = st.columns(2)
        
        # Display Current Price
        current_price = df['Close'].iloc[-1]
        prev_price = df['Close'].iloc[0]
        change = ((current_price - prev_price) / prev_price) * 100
        
        col1.metric(label=f"Current {ticker} Price", value=f"${current_price:.2f}", delta=f"{change:.2f}%")
        
        # Display Data Table
        col2.write("Recent Closing Prices")
        col2.dataframe(df[['Close']].tail(5))
        
        # Plotting the Chart
        st.subheader(f"{ticker} Price Trend (Last 30 Days)")
        st.line_chart(df['Close'])
    else:
        st.error("Invalid Ticker. Please try again.")

st.divider()
st.info("Built with Python, YFinance API, and Streamlit.")
