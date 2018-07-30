# Market Analysis

The scripts below were all developed using Jupyter Notebook

### trading_1
This script is used to test stock trading strategies involving Bollinger Bands. The rolling mean and std used to form the bands have a 30 day window. The results are plotted using matplotlib and the sharpe ration is computed to evaluate the strategies.

* The first includes only buying longs, which is means buying a stock by if the price of the stock is 2 std below the rolling mean.

* The second includes buying longs and short selling, which means selling a stock is the price of the stock is 2 std above the rolling mean.

The strategies are tested using only market data from Apple(AAPL) and Google(GOOG) 
Below are links for more info on short selling:
https://www.investopedia.com/university/shortselling/shortselling1.asp

### trading_2
This script is used to find the optimum portfolio distribution between: Apple(AAPL), Google(GOOG), Microsoft(MSFT), Amazon(AMZN)

* The trading stategy is the same as the first strategy used in trading_1, only buying longs. 
* All possible distributions of the 4 stocks are tested to see which is the best by their sharpe ratio
* A scatter plot is made to plot the sharpe of every stategy in coordinate form (std, mean)
  * Interestingly, the best trading strategies lie on the top curve of the surface that is created by the scatter plot.
