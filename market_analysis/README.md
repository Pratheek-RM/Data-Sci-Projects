# Data-Sci-Projects

### trading_1
This script is used to test stock trading strategies involving Bollinger Bands. The rolling mean and std used to form the bands have a 30 day window. The results are plotted using matplotlib and the sharpe ration is computed to evaluate the strategies.

* The first includes only buying longs, which is means buying a stock by if the price of the stock is 2 std below the rolling mean.

* The second includes buying longs and short selling, which means selling a stock is the price of the stock is 2 std above the rolling mean.

The strategies are tested using only market data from Apple(AAPL) and Microsoft(MSFT) 
Below are links for more info on short selling:
https://www.investopedia.com/university/shortselling/shortselling1.asp
