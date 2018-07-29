import numpy as np
import pandas as pd
from copy import deepcopy

import matplotlib.pyplot as plt


stockName = "AAPL"
column_name = 'Adj Close'

#The block below prints the data from the csv, and should be simple enough to feed to a DataFrame

#csv data converted to a list and then a numpy array
import csv
with open('AAPL.csv') as csvfile:
    csvreader = list(csv.reader(csvfile, delimiter=','))

    data = np.asarray(csvreader)

#Data from list now converted to a pandas DataFrame
finDF = pd.DataFrame(data = data[1:,1:], index = data[1:,0], columns = data[0,1:])

#Series for Adj Close converted to float for the math needed later on
finDF[column_name] = pd.to_numeric(finDF[column_name], downcast = 'float')
adjSer = finDF[column_name]

mean = adjSer.mean()
std = adjSer.std()
print("#"*60)
print("Mean of " + stockName + "'s" + column_name + ":", mean)
print("Standard Deviation of " + stockName + "'s" + column_name + ":", std)
print("#"*60)

#Orginal Data plotted
fig = plt.figure()
dateList = adjSer.index.values.tolist()

#List of window values we will use
win = [3,4,5,6]

#Deciding the format of the subplots
numSubPlt = len(win)
if numSubPlt % 2:
    even = 1
else:
    even = 0

if numSubPlt/2 == 0:
    x = 1
    y = 1
else:
    x = 2
    y = numSubPlt/2 + even

x = str(x)
y = str(int(y))

#Instantiated subplots
subPlotList = [fig.add_subplot(int(x+y+str(i+1))) for i in range(len(win))]
print(subPlotList)

#the loop with iterate through different window sizes
count = 0
for i in win:
    print("Rolling Mean and Standard Deviation with window of size:", i)
    rollingMean = deepcopy(adjSer)
    rollingStd =  deepcopy(adjSer)

    rollingMean = rollingMean.rolling(window=i,center=False).mean()
    rollingStd  = rollingStd.rolling(window=i,center=False).std()
    print("Rolling Mean:")
    print(rollingMean)
    print("Rolling Std:")
    print(rollingStd)

    upperband = [val + (2*rollingStd[i]) for val, i in zip(rollingMean.tolist(), range(len(rollingMean.tolist())))]
    lowerband = [val - (2*rollingStd[i]) for val, i in zip(rollingMean.tolist(), range(len(rollingMean.tolist())))]

    #This makes the x-axis very messy looking, but I couldn't find a cleaner way
    subPlotList[count].plot(dateList, adjSer.tolist())
    subPlotList[count].plot(dateList, rollingMean.tolist())
    subPlotList[count].plot(dateList, upperband)
    subPlotList[count].plot(dateList, lowerband)
    #Add new plot to legend
    # legendList.append(["Normal", "Window of size "+str(i)])
    print("#"*60)
    count += 1
    # print(count)

# plt.legend(legendList)
plt.legend(["Normal", "Rolling Mean", "Upper Band", "Lower Band"])
plt.show()

# #The code bellow isn't returning usable data or return errors
#
# # import csv
# # import urllib.request
# #
# # downloaded_data  = urllib.request.urlopen('https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=1528210863&period2=1530802863&interval=1d&events=history&crumb=5evLqOGb3q3')
# # csv_data = csv.reader(downloaded_data, delimiter=',')
# # print(csv_data)
# # #
# # for row in csv_data:
# #     print(row)
# import requests
# r = requests.get('https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=1528210863&period2=1530802863&interval=1d&events=history&crumb=5evLqOGb3q3')
# # print(r)
# data = r.json()
# print(data)
