import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from movingaverage_size_test_method import moving_average_size
from plot import plot_sharpe_heatmap

#This script is to test out even smaller rolling window sizes because the last test hinted at greater success with tighter window sizes

#Define our smaller windows
short = range(3,31, 3)
long = range(10, 121, 5)

#Run the moving average for loop function that returns a dataframe with the sharpe ratio for each window pair
result = moving_average_size(short, long)
result_df = pd.DataFrame(result)

#Create the heatmap
plot_sharpe_heatmap(result_df)
plt.show()

#73/210 has a greater sharpe than buy and hold; roughly 34.76%
print(len(result_df['sharpe']))
print(len(result_df['sharpe'].loc[result_df['sharpe'] > 0.781]))

#We now have 8 above 1
print(len(result_df['sharpe'].loc[result_df['sharpe'] > 1]))