'''
 Writing programming interview questions hasn't made me rich. Maybe trading Apple stocks will.

Suppose we could access yesterday's stock prices as a list, where:

    The indices are the time in minutes past trade opening time, which was 9:30am local time.
    The values are the price in dollars of Apple stock at that time.

So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.
'''


def get_max_profit(stock_prices_yesterday):

    if len(stock_prices_yesterday) < 2:
        return False
    min_price = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1]-stock_prices_yesterday[0]

    for index, current_price in enumerate(stock_prices_yesterday):
        if index == 0:
            continue
        # ensure min_price is the lowest price we've seen so far
        potential_profit = current_price - min_price
        min_price = min(min_price, current_price)
        # update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)
    return max_profit
stock_prices_yesterday = [10, 7, 5, 8]
print get_max_profit(stock_prices_yesterday)