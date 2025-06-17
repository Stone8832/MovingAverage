import yfinance as yf

#import spy data; data holds date, close, high, low, open, and volume. Date is datetime
def load_spy(start = "2020-06-15"):
     spy = yf.download("SPY", start = start, auto_adjust= True)
     spy = spy.dropna()
     return spy
