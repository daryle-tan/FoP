def maxSubListSum(num_list, num):
    end_index = num
    start_index = 0
    max_sum = 0
    temp_max = 0

    if len(num_list) == 0:
        return None
    
    while end_index <= len(num_list):
        window = num_list[start_index:end_index]
        if len(window) == num:
            for nb in window:
                temp_max += nb
            if temp_max > max_sum:
                max_sum = temp_max
                temp_max = 0
            else:
                temp_max = 0
        end_index += 1
        start_index += 1
    # print(max_sum)   
    return max_sum


# Test Cases
print(maxSubListSum([1, 2, 5, 2, 8, 1, 5], 2)) # 10
# 3, 7, 7, 10, 9, 6
print(maxSubListSum([1, 2, 5, 2, 8, 1, 5], 4)) # 17
# 10, 17, 16, 16, 
print(maxSubListSum([4, 2, 1, 6], 1)) # 6
print(maxSubListSum([4, 2, 1, 6, 2], 4)) # 13
print(maxSubListSum([], 4)) # None