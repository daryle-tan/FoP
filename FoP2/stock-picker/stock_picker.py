def stock_picker(prices):
    lowest, lowest_index  = prices[0] , 0
    second_lowest, second_lowest_index = prices[0], 0
    highest, highest_index = 0, 0
    second_highest, second_highest_index = 0, 0
    # [17,3,6,9,15,8,6,1,10]
    for x in range(len(prices)):
    #find the lowest and its index
        for y in range(x+1, len(prices)- 1, 1):
            if prices[x] < prices[y]:
                # also keep track of the second lowest and its index
                if prices[x] < lowest:
                    second_lowest = lowest 
                    second_lowest_index = lowest_index
                    lowest = prices[x]
                    lowest_index = x
                if prices[y] > highest and y > second_lowest_index:
                    second_highest = highest
                    second_highest_index = highest_index
                    highest = prices[y]
                    highest_index = y        
            elif prices[x] > prices[y]:
                if prices[y] < lowest:
                    second_lowest = lowest
                    second_lowest_index = lowest_index
                    lowest = prices[y]
                    lowest_index = y
                if prices[x] > highest and x > lowest_index:
                    second_highest = highest
                    second_highest_index = highest_index
                    highest = prices[x]
                    highest_index = x 

    lowest_difference = 0
    second_lowest_difference = 0

    # if  
    print( 'lowest:', lowest, 'lowestIndex:', lowest_index,  'second Lowest:',second_lowest, 'secondLowestIndex:',second_lowest_index)
    print('highest:',highest, 'highestIndex:',highest_index, 'secondHighest:',second_highest, 'secondHighestIndex:',second_highest_index)
    
    # find the highest after the lowest day and its index
    # find the highest after the second lowest and its index
    # compare which has the highest profit
    # return the list of indices for the buy and sell
    # print(lowest_index, lowest)

       
# print(find_lowest([17,3,6,9,15,8,6,1,10]))
# print(find_highest([17,3,6,9,15,8,6,1,10]))
print(stock_picker([17,3,6,9,15,8,6,1,10])) # => [1,4]
# for a profit of $15 - $3 == $12

# def find_lowest(prices):
#     sorted_prices_asc =  sorted(prices)
#     return sorted_prices_asc[0]

# def find_highest(prices):
#     sorted_prices_desc = sorted(prices, reverse=True)
#     return sorted_prices_desc[0]