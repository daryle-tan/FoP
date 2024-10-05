def bubbleSortCount(num_list):
    comparisons = 0
    exchanges = 0

    for x in range(len(num_list)):
        for y in range(len(num_list)-x-1):
            comparisons += 1
            if num_list[y] > num_list[y+1]:
                num_list[y], num_list[y+1] = num_list[y+1], num_list[y]
                exchanges += 1
    # print(comparisons, exchanges)
    return (comparisons, exchanges)

print(bubbleSortCount([1, 2, 3, 5, 4, 6, 7])) # (21, 1)
print(bubbleSortCount([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) # (45, 45)
print(bubbleSortCount([2, 1, 0, 5, 4])) # (10, 4)