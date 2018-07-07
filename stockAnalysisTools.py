import numpy as np
import pandas as pd
from copy import deepcopy
import sys
#yqd is an open-source script I'm using as a Yahoo Finance API
from yqd import load_yahoo_quote

import matplotlib.pyplot as plt

def numToString(num):
    divisor = 1000

    decimal = str(float(num)-int(num))
    nonDec = int(num)
    s = str(nonDec)
    numDigits = len(s)
    # print(numDigits)

    listofsubsec = list()
    for i in range((numDigits//3)):
        listofsubsec.append(s[numDigits - ((i+1)*3): numDigits - ((i)*3)])

    # print(listofsubsec)
    if(numDigits%3 != 0):
        listofsubsec.append(s[0:numDigits%3])
    # print(listofsubsec)

    s = ""
    for sub in listofsubsec:
        s =  "," + sub + s

    return s[1:] + decimal[1:]

#returns mean, std, Sharpe, value_of_investment
def getStockData(stockTicker, startDate, endDate, investment):
    #This loop is necessary, since load_yahoo_quote will have HTTP 401 errors occasionally
    count = 0
    bool = True
    while(bool):
        try:
            quote_data = load_yahoo_quote(stockTicker, startDate, endDate)
            bool = False
            break
        except:
            bool = True
            count += 1
            if(count == 50):
                print("HTTP error exitting program")
                quit()


    data = [quote.rsplit(',') for quote in quote_data]
    data.pop()
    data = np.asarray(data)

    #Data from list now converted to a pandas DataFrame
    finDF = pd.DataFrame(data = data[1:,1:], index = data[1:,0], columns = data[0,1:])

    #Series for Adj Close converted to float for the math needed later on
    finDF[column_name] = pd.to_numeric(finDF[column_name], downcast = 'float')
    adjSeries = finDF[column_name]

    print(stockTicker+" price first day "+str(adjSeries[0]))
    print(stockTicker+" price last day  "+str(adjSeries[len(adjSeries)-1]))

    value_of_investment = investment*(adjSeries[len(adjSeries)-1]/adjSeries[0])

    print("Value of investment on " + stockTicker +":", numToString(value_of_investment))

    relative_val_series = deepcopy(adjSeries)

    for i in range(len(adjSeries)-1, 0, -1):
        relative_val_series[i] = (relative_val_series[i]/relative_val_series[i-1]) - 1

    relative_val_series[0] = np.nan

    mean = relative_val_series.mean()
    std = relative_val_series.std()
    print("#"*60)
    print("These calculations are from", startDate, "to", endDate)
    print("Relative mean of stock price change for " + stockTicker +" is:", mean)
    print("Relative std of stock price change for " + stockTicker +" is:", std)
    print("Sharpe Ratio is:", (mean/std))
    print("#"*60)

    return mean, std, mean/std, value_of_investment
