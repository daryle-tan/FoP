def countUniqueValues(num_list):
    counter = {}
    for num in num_list:
        if num not in counter:
            counter[num] = 1
        else:
            counter[num] += 1
    # print(len(counter))
    return len(counter)


print(countUniqueValues([1, 1, 1, 1, 1, 2])) # 2
print(countUniqueValues([1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 13])) # 7
print(countUniqueValues([-2, -1, -1, 0, 1])) # 4
print(countUniqueValues([])) # 0