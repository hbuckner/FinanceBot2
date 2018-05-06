from readCurrency import readCurrency
c=readCurrency().currencyGet("NASDAQ.txt")
import pandas as pandas
from pandas_datareader import data as web
import datetime
from datetime import datetime, timedelta
from simpleMovingAverage import simpleMovingAverage
from volume import Volume
from rtstock.stock import Stock

smalist=[]


#SMA = SimpleMovingAverage.simpleMovingAverage(x)

for x in c:
	print()
	yahoo= Stock('GOOG')
	yahoo.get_latest_price()
	print(google)
	#print (currentprice)

	#SMA = simpleMovingAverage(x)
	#volume = Volume(x)
	#if(volume>500000):
		#smalist.append([x,SMA,volume])
	#print(SMA)
	#print volume

#with open('SMA.txt','w') as f:
	#for item in smalist:
		#print (item,  end="", file=f)
	#f.close()
