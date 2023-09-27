import yfinance

hist = yfinance.Ticker("AAPL").history(
    period= "1d",
    interval= "1h",
    start= "2022-01-01",
    end= "2022-01-10",
    prepost= True
)
print(hist.head())