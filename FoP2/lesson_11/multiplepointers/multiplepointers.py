def sumZero(num_list):
    duo_list = []
    left, right = 0, len(num_list) - 1

    while  left < right:
        current_sum = num_list[left] + num_list[right]

        if current_sum == 0:
            return [num_list[left], num_list[right]]
        elif current_sum < 0:
            left += 1
        else:
            right -= 1

    return -1
        


print(sumZero([-3, -2, -1, 0, 1, 2, 3])) # [-3, 3]
print(sumZero([-10, -5, 0, 1, 3, 5, 87, 99])) # [-5, 5]
print(sumZero([-2, 0, 1, 3])) # -1
print(sumZero([1, 2, 3])) # -1