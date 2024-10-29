# Given a set of characters generate all possible passwords from them. This means we should generate all possible permutations of words using the given characters, with repetitions and also up to a given length. E.g., all_passwords(['c', 'a', 't']) = ['c', 'a', 't', 'ca', 'at', 'ct', 'ac', 'ta', 'tc', 'cat', 'cta', 'act', 'atc', 'tac', 'tca']
def all_passwords(lst):
    all_possible_pw = []
    
    def generate(generated_pw):
        if generated_pw:
            all_possible_pw.append(generated_pw)

        if len(generated_pw) == len(lst):
            return
        
        for char in lst:
            generate(generated_pw + char)

    generate("")

    # return list of all possible passwords
    return all_possible_pw

print(all_passwords(['c', 'a', 't']) ) # ['c', 'a', 't', 'ca', 'at', 'ct', 'ac', 'ta', 'tc', 'cat', 'cta', 'act', 'atc', 'tac', 'tca']

# Given a number, find the sum of all of its digits. E.g. sum_digits(1234) = 10
def sum_digits(num):
    if num < 10:
        return num
    
    remaining_digit = num % 10
    # print(num)
    return remaining_digit + sum_digits(num//10)

print(sum_digits(1234)) # = 10


# Given a string, find the index of the first number. E.g. idx_first_num("str1ng") = 3
def idx_first_num(input_str):
    char_split = list(input_str)
    
    for char in char_split:
        try:
            char_int = int(char)
            return char_split.index(char)
        except ValueError:
            print("Not an integer")
           
    return idx_first_num(input_str[1:])

print(idx_first_num("str1ng")) #3