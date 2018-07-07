from stockAnalysisTools import numToString
from stockAnalysisTools import getStockData
#######  Main funcion starts here #######

###Input taken from user
print("This program performs analysis for two different stocks or just one across an interval")
choice = input("Choose your option by typeing:\n- 1 \tFor one stock\n- 2 \tFor two stock\n")
if(not("1" == choice or "2" == choice)):
    print("Invaild entry")
    quit()

default = input("Skip the rest of the input prompts by typing default or anything else for custom input\n")

if("default" in default):
    if("1" == choice):
        stockTicker1 = "AAPL"
        startDate = "20050101"
        endDate = "20180705"
        investment1 = 100000
    else:
        stockTicker1 = "AAPL"
        stockTicker2 = "GOOG"
        startDate = "20050101"
        endDate = "20180705"
        investment1 = 50000
        investment2 = 50000
else:
    stockTicker1 = input("Tick of first stock: ")
    if("2" == choice):
        stockTicker2 = input("Tick of second stock: ")

    print("Dates need to be entered in the format of yyyymmdd with no spaces\n\t \
    Example: July 5th, 2018 --> 20180705")
    startDate = input("Ener start date: ")
    endDate = input("Ener start date: ")

    print("Amounts need to be entered without commas or a dollar sign\n\t \
    Example: $100,000 --> 100000")
    if("1" == choice):
        investment1 = input("How much are you investing: ")

    else:
        investment1 = input("How much are you investing in stock 1: ")
        investment2 = input("How much are you investing in stock 2: ")
        investment2 = int(investment2)

    investment1 = int(investment1)

###Code starts here
column_name = 'Adj Close'

mean1,std1,sharpe1, return1 = getStockData(stockTicker1, startDate, endDate, investment1)
if("2" == choice):
    mean2,std2,sharpe2, return2 = getStockData(stockTicker2, startDate, endDate, investment2)
    print("Total Investment Return:", numToString(return1+return2))
    #Not sure how this is suppose to be done
    print("Combined Sharpe:", (sharpe1+sharpe2)/2)
