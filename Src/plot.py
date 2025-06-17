import matplotlib.pyplot as plt

def plot_moving_averages(spy):
    spy[['Close', 'ma_short', 'ma_long']].plot(title='SPY Price Chart and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')

def plot_equity(spy):
    spy[['Hold EQ Return', 'Strategy EQ Return']].plot(title='SPY Trading Strategy Equity Comparison')
    plt.xlabel('Date')
    plt.ylabel('Equity')