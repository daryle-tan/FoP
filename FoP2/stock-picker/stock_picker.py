def stock_picker(prices):
    lowest_price, lowest_index  = prices[0] , 0
    highest, highest_index = 0, 0
    max_profit = 0
    best_buy_index = 0
    best_sell_index = 0
    # [17,3,6,9,15,8,6,1,10]
    for i in range(1, len(prices)):
    #find the lowest and its index 
        current_price = prices[i]
        potential_profit = current_price - lowest_price

        if potential_profit > max_profit:
            max_profit = potential_profit
            best_buy_index = lowest_index
            best_sell_index = i

        if current_price < lowest_price:
            lowest_price = current_price
            lowest_index = i
      
    print( best_buy_index,best_sell_index )
    return [best_buy_index, best_sell_index]

print(stock_picker([17,3,6,9,15,8,6,1,10])) # => [1,4]
