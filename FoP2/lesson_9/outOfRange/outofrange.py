class OutOfRangeError(Exception):
    pass


def name_the_number(user_input):
    try:
        user_input = int(input('Enter an integer(1,2,3):  '))
        if user_input == 1:
            print("one")
        elif user_input == 2:
            print("two")
        elif user_input == 3:
            print("two")
        else:
            raise OutOfRangeError
    except OutOfRangeError:
        print('That value is out of range!')
    except ValueError:
        print("please enter a valid integer")
# try:
#     name_the_number()
# except ValueError:
#     print("please enter a valid integer")

print(name_the_number(input))