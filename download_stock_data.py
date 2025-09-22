#install yfinance
import yfinance as yf

df = yf.download("BTC-USD",start='2025-08-10' , interval ='1d', auto_adjust=False)


df.reset_index().to_csv("BTC_stock_data.csv",index=False)