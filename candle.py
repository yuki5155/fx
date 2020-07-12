import pandas as pd
import matplotlib.dates as mdates
import pandas_datareader as pdr
import datetime as dt
from datetime import date
from mpl_finance import candlestick_ohlc

import matplotlib.pyplot as plt

def main(stock):
    start = dt.datetime(2019,2,26)
    end = date.today()

    df = pdr.get_data_yahoo(stock, start, end)

    df["50"] = df["Close"].rolling(window=50).mean()
    df = df.tail(200)
    ax = plt.subplot()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
    candlestick_ohlc(ax, zip(mdates.date2num(df.index), df['Open'], df['High'], df['Low'], df['Close']), width=0.4)
  
    ax.plot(mdates.date2num(df.index), df["50"])
    plt.title(stock)
    plt.show()

#yahoofinancialにある番号などを入力
#main("MONA-JPY")

