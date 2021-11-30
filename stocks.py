import yfinance as yf 
print ("{:<1} {:>18} {:>18} {:>15} {:>20}".format('Stock','Current Price','Target Price','Discount', 'Recommendation'))
print('--------------------------------------------------------------------------------')
#ENTER ANY NUMBER OF STOCKS YOU WOULD LIKE TO SEE
stocks = ['HOOD', 'F', 'AAPL', 'MSFT', 'AMZN', 'COIN', 'ABNB', 'TSLA', 'SPOT', 'NIO','SQ', 'PFE', 'QCOM']
for stock in stocks:
    stock = yf.Ticker(stock)
    current_price = stock.info['currentPrice']
    current_price = float(current_price)
    target_price = stock.info['targetMeanPrice']
    target_price = float(target_price)
    current_price = round(current_price, 2)
    discount = ((target_price-current_price)/abs(current_price))*100
    discount = round(discount, 2)
    symbol = stock.info['symbol']
    if discount > 50:
        recommendation = 'Strong Buy'
    elif 15 <= discount <= 50:
        recommendation = "Buy"
    elif -15 < discount < 15:
        recommendation = "Hold"
    elif -50 < discount <= -15:
        recommendation = "Sell"
    else:
        recommendation = "Strong Sell"
    print(f"{symbol:<5}{current_price:>16}{target_price:>18}{discount:>18}%{recommendation:>20}")
