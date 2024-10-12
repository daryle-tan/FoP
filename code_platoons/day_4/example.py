snake_case = 'snake case'
Pascal_Case = 'Pascal Case'

GLOBAL = 'constant'

print(GLOBAL)
# f string

print(f"{Pascal_Case} is the styles")

# morning group coding challenge
def count_x_o(str):
    count_x = 0
    count_y = 0

    for char in str.lower():
        if char == 'x':
            count_x += 1
        elif char == 'y':
            count_y += 1
    return (count_x, count_y)

print(count_x_o("xxxoolkasOxOXX"))