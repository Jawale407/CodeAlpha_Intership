# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400,
    "AMZN": 180
}

print("===== STOCK PORTFOLIO TRACKER =====")

print("\nAvailable Stocks:")

for stock in stock_prices:
    print(stock, "-", stock_prices[stock])