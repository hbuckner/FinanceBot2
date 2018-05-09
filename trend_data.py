import sys
#gets trend data for input for 5 years
import pytrends
import eventlet
from pytrends.request import TrendReq
import time as t

def get_trend_data(input):
    pytrends = TrendReq(hl='en-US', tz=360)
    kw_list = [input]
    a= pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')
    b =pytrends.interest_over_time()
    return b

#get trend data
#testing
#print(get_trend_data("buy GOOG"))
#read_data_getTrend: gets trend data and outputs to file
def read_data_getTrend(seconds):
    file = open("nasdaq.txt", "r")
    file2 = open("finish.txt", "w")
    for line in file:
                c=get_trend_data("buy "+line)

                b=str(c)
                print(b)
                file2.write(b)
                t.sleep(seconds)
    print("finished!")
read_data_getTrend(10)
