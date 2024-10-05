def list_max(num_list):
    if len(num_list) == 1:
        return num_list[0]
    max = list_max(num_list[1:])
    return num_list[0] if num_list[0] > num_list[1] else max

print(list_max([3,4,5,7]))
print(list_max([13,22,5,17]))
print(list_max([3,40,55,55]))
