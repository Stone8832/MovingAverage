import yfinance as yf
#Methods to import stock data

#import spy data; data holds date, close, high, low, open, and volume. Date is datetime
def load_spy(start = "2020-06-15"):
     spy = yf.download("SPY", start = start, auto_adjust= True)
     spy = spy.dropna()
     return spy
#Loads a stock of your choice, must provide ticker simple and start date
def load_stock(ticker, start):
     df= yf.download(ticker, start=start, auto_adjust=True)
     df = df.dropna()
     return df
