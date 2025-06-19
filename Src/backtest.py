#Methods to run the moving average backtest and buy and hold equity and returns

#Computes the moving averages: Must input a dataframe with close price and window lengths
def compute_moving_averages(spy, short_len, long_len):
    spy['ma_short'] = spy['Close'].rolling(short_len).sum().div(short_len)
    spy['ma_long'] = spy['Close'].rolling(long_len).sum().div(long_len)
    spy = spy.dropna()
    return spy

#Computes the trading signal: When the strategy says to buy, this method will add a column that tracks position using 0 and 1
def trading_signal(spy):
    spy['Signal'] = (spy['ma_short'] > spy['ma_long']).astype(int)
    spy['Signal'] = spy['Signal'].shift(1).fillna(0)
    return spy

#Computes the returns for buy and hold and strategy, must run the previous two methods before hand
def compute_returns(spy):
    spy['Spy Daily Pct'] = spy['Close'].pct_change().fillna(0)  # new column
    spy['Hold EQ Return'] = (1 + spy['Spy Daily Pct']).cumprod()  # buy and hold eq returns
    spy['Strategy Daily Pct'] = spy['Signal'] * spy['Spy Daily Pct']  # new column, only applies spy daily pct change if position is true
    spy['Strategy EQ Return'] = (1 + spy['Strategy Daily Pct']).cumprod()
    return spy