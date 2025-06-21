import matplotlib.pyplot as plt
#These methods are used to plot the data such as the moving average, strategy equity vs buy and hold equity, and sharpe ratio heatmap

#Method to plot the stock price chart and the calculated moving averages
def plot_moving_averages(spy):
    spy[['Close', 'ma_short', 'ma_long']].plot(title='SPY Price Chart and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')

#Method to plot the strategy EQ compared to stock EQ
def plot_equity(spy):
    spy[['Hold EQ Return', 'Strategy EQ Return']].plot(title='SPY Trading Strategy Equity Comparison')
    plt.xlabel('Date')
    plt.ylabel('Equity')

#Creates the heatmap for multiple sharpe ratios for testing window lengths, input must be a dataframe
def plot_sharpe_heatmap(sharpe_df):
    # Create the heatmap
    result_matrix = sharpe_df.pivot(columns='short', index='long', values='sharpe').fillna(0)
    plt.imshow(result_matrix, origin='lower', aspect='auto')
    plt.colorbar(label='Sharpe Ratio')
    plt.xticks(range(len(result_matrix.columns)), result_matrix.columns)
    plt.yticks(range(len(result_matrix.index)), result_matrix.index)
    plt.xlabel("Short Window")
    plt.ylabel("Long Window")
    plt.title("Smaller Window Sharpe Ratio Test")

#Method to plot the strategy EQ only
def plot_equity_only(spy):
    spy['Strategy EQ Return'].plot(title='SPY Trading Strategy Equity')
    plt.xlabel('Date')
    plt.ylabel('Equity')
