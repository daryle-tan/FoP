def count_letters(string):
    counted = dict()
    formatted_string = string.upper()
    for letter in formatted_string:
        if letter not in counted and letter.isalpha():
            counted[letter] = 1
        elif letter in counted and letter.isalpha():
             counted[letter] += 1   
    print(counted)
    return counted

print(count_letters("AaBb"))