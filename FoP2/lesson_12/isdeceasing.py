def is_decreasing(num_list):
    list_size = len(num_list)
    if list_size == 2:
       return num_list[0] > num_list[1]
  
    return num_list[0] > num_list[1] and is_decreasing(num_list[1:])

print(is_decreasing([5,4,3,2,1])) # True
print(is_decreasing([5,4,3,6,1])) # False
print(is_decreasing([3,2,1])) # True
