def binarySearch(num_list, target):
    start, end = 0 , len(num_list) - 1

    while start <= end:
        mid = (start + end) // 2
        if num_list[mid] == target:
            return mid
        elif num_list[mid] > target:
            end = mid - 1
            # print(end)
        else:
            start = mid + 1       
    # print( num_list[mid], end)
    return -1


# Test Cases
print(binarySearch([5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 40, 44, 64, 79, 84, 86, 95, 96, 98, 99], 10)) # 2
print(binarySearch([5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 40, 44, 64, 79, 84, 86, 95, 96, 98, 99], 95)) # 16
print(binarySearch([5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 40, 44, 64, 79, 84, 86, 95, 96, 98, 99], 100)) # -1