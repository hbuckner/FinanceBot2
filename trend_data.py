import sys
#gets trend data for input for 5 years
import pytrends
import eventlet
from pytrends.request import TrendReq

def get_trend_data(input):
    pytrends = TrendReq(hl='en-US', tz=360)
    kw_list = [input]
    a= pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')
    b =pytrends.interest_over_time()
    return b

#get trend data
#testing
#print(get_trend_data("buy GOOG"))

def read_data_getTrend():
    file = open("nasdaq.txt", "r")
    file2 = open("finish.txt", "w")

    for line in file:
        with eventlet.Timeout(45):
            c=get_trend_data(line)
            b=str(c)
            print(c)
            file2.write(b)

read_data_getTrend()
