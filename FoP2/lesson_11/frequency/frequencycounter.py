def same(list1, list2):
    if len(list1) != len(list2):
            return False
    
    freq_list = {}

    for elem in list1:    
        sq_result = elem * elem
        if sq_result in list2 and elem in freq_list:
            freq_list[elem] += 1
            # print(sq_result)
        elif sq_result in list2 and elem not in freq_list:
            freq_list[elem] = 1
            # print(len(freq_list))
    if len(freq_list) == len(list2):
        return True
    else:
         return False
    


print(same([1, 2, 3], [4, 1, 9])) # true
print(same([1, 2, 3], [1, 9])) # false
print(same([1, 2, 1], [4, 4, 1])) # false (must be same frequency)