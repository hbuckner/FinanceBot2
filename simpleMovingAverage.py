from readCurrency import readCurrency
import pandas as pandas
from pandas_datareader import data as web
import datetime
from datetime import datetime, timedelta
import numpy as np
##import fix_yahoo_finance as yf
#yf.pdr_override()
from rtstock.stock import Stock
#c=readCurrency().currencyGet("NASDAQ.txt")

def simpleMovingAverage(stockname):
	N = 200
	start = datetime.now() - timedelta(days=N)
	yesterday = datetime.today()-timedelta(days=1)
	end = yesterday

#searches list and calculates the average.
	stock = web.DataReader(stockname,"morningstar",start,end)
	#print(stock)
	if stock.empty==False:
		SMA=stock["Close"].mean()
		return SMA

print (simpleMovingAverage("GOOG"))
