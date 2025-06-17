import numpy as np

#Computes the metrics of the strategies
def calc_cagr(equity):
    ending_value = equity.iloc[-1]
    days = len(equity)
    annual_factor = 252 / days
    return (ending_value ** annual_factor) - 1

#Calculate Annualized volatility: Measure of how volatile an investment is over a year
def calc_av(returns):
    daily_variance = returns.std()
    return daily_variance * np.sqrt(252)

#Calculate Sharpe Ratio: Return per unit of risk "How much extra return did I get for each percent of volatility I endured". Note, we assume zero risk free rate
def calc_sharpe(cagr, vol):
    return cagr / vol if vol != 0 else np.nan

#Calculate Maximum drawdown: The worst peak-to- trough decline our equity curve experienced
def calc_drawdown(equity):
    peak = equity.cummax() #returns a series with the max up until that point
    drawdown = (equity - peak) / peak
    return drawdown.min()