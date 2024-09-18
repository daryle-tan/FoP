import random

correct_num = random.randint(0,30)
tries = 0
is_won = False
print(correct_num)
while is_won == False:
    numGuess = int(input('Guess a number: '))
    if numGuess == correct_num:
        tries += 1
        print(f'You guessed it in {tries} tries')
        is_won = True
    elif numGuess > correct_num:
        tries += 1
        print('Too high - try again')
    else:
        tries += 1
        print('Too low - try again')