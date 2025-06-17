
#runs the backtest based on moving average strategy and buy and hold and saves the results to the dataframe

def compute_moving_averages(spy, short, long):
    spy['ma_short'] = spy['Close'].rolling(short).sum().div(short)
    spy['ma_long'] = spy['Close'].rolling(long).sum().div(long)
    spy = spy.dropna()
    return spy
def trading_signal(spy):
    spy['Signal'] = (spy['ma_short'] > spy['ma_long']).astype(int)
    spy['Signal'] = spy['Signal'].shift(1).fillna(0)
    return spy
def compute_returns(spy):
    spy['Spy Daily Pct'] = spy['Close'].pct_change().fillna(0)  # new column
    spy['Hold EQ Return'] = (1 + spy['Spy Daily Pct']).cumprod()  # buy and hold eq returns
    spy['Strategy Daily Pct'] = spy['Signal'] * spy['Spy Daily Pct']  # new column, only applies spy daily pct change if position is true
    spy['Strategy EQ Return'] = (1 + spy['Strategy Daily Pct']).cumprod()
    return spy