# Stocks On Sale
This program compares a stock's average analyst target price with its current trading price.

    import yfinance as yf 
    print ("{:<1} {:>17} {:>16} {:>13} {:>18} {:>11} {:>19}".format('Stock','Current Price','Target Price','Discount','Total Opinions', 'Rating', 'Recommendation'))
    print('---------------------------------------------------------------------------------------------------------')
    #ENTER ANY NUMBER OF STOCKS 
    stocks = ['AMZN', 'TSLA', 'SPOT', 'PYPL', 'SNAP', 'ZM', 'ROKU', 'DKNG', 'TFX', 'TWLO', 'EXAS', 'COUP', 'RBLX']
    for stock in stocks:
        try:
            stock = yf.Ticker(stock)
            current_price = stock.info['currentPrice']
            current_price = float(current_price)
            target_price = stock.info['targetMeanPrice']
            target_price = float(target_price)
            current_price = round(current_price, 2)
            discount = ((target_price-current_price)/abs(current_price))*100
            discount = round(discount, 2)
            symbol = stock.info['symbol']
            num_analysts = stock.info['numberOfAnalystOpinions']
            num_analysts = int(num_analysts)
            rec_mean = stock.info['recommendationMean']
            if discount > 50 and rec_mean < 2:
                recommendation = 'Strong Buy'
            elif discount > 50 and rec_mean >=2:
                recommendation = 'Buy'
            elif 15 <= discount <= 50:
                recommendation = "Buy"
            elif -15 < discount < 15:
                recommendation = "Hold"
            elif -50 < discount <= -15:
                recommendation = "Sell"
            else:
                recommendation = "Strong Sell"
            print(f"{symbol:<5}{current_price:>15}{target_price:>17}{discount:>15}%{num_analysts:>14}{rec_mean:>16}{recommendation:>19}")
        except:
            continue 
