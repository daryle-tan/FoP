def bubbleSort(num_list):
  
    for i in range(len(num_list)):
        for j in range(0, len(num_list)-i-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
           
    return num_list

# Test Cases
print(bubbleSort([5, 3, 10, 6, 1])) # [1, 3, 5, 6, 10]
print(bubbleSort([100, 98, 101, 10])) # [10, 98, 100, 101]
print(bubbleSort([2, 1, 0, 5, 4])) # [0, 1, 2, 4, 5]