def multiply(num1, num2):
    if num2 == 0:
        return 0
    return num1 + multiply(num1, num2 - 1)
    

print(multiply(7,4))