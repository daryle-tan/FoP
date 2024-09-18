def hailstone(num):
    count = 0
    while num > 1:
        if num == 1:
            return 0
        elif num % 2 ==0:
            num = num / 2
            count += 1
        elif num % 2 != 0:
            num = (num * 3) + 1
            count += 1
    return count

print(hailstone(10))