from readCurrency import readCurrency
import pandas as pandas
from pandas_datareader import data as web
import datetime
from datetime import datetime, timedelta
import numpy as np
import quandl as c

c.ApiConfig.api_key = "4oPDSBZ_Yuid-dah3Mg3"

def Volume(stockname):
	N = 365
	yesterday = datetime.today()-timedelta(days=1)
	start = yesterday
	end = datetime.now()
	stock = web.DataReader(stockname,"morningstar",start,end)
	date = end
	return stock


	#if stock.empty==False:
		#stock["20d"] = stock['Volume']
		#todaystock=stock["20d"].tail(1)
		#SMA=todaystock.ix[0,date]

		#return SMA
	#else:
		#return 0
#""""

a=Volume("GOOG")
print(a)
