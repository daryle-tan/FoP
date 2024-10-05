# def factorial(num):
#     print(num)
#     if num == 0:
#         return 1
#     else:
#         return num * factorial(num-1)
# factorial(5)

def countdown(num):
    if num == 1:
        return str(num) 
    else:
        return str(num)+ " " + countdown(num - 1)
    
print(countdown(5))

def countup(num):
    if num == 1:
        return str(num)
    else:
        return countup(num - 1) + " " + str(num)
    
print(countup(5))

def sum_countup(num):
    if num == 0:
        return 0
    else:
        return num + sum_countup(num - 1)
    
print(sum_countup(5))