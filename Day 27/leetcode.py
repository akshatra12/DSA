def maximum_profit(price):
    min_price=price[0]
    max_profit=0
    for i in range(1,len(price)):
        if price[i]<min_price:
            min_price=price[i]
        else:
            profit=price[i]-min_price
            if max_profit<profit:
                 max_profit=profit
    return max_profit
prices = [7,1,5,3,6,4]
print(maximum_profit(prices))
