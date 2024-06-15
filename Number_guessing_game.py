import random
random_num = random.randint(1, 100)
print('***Welcome to the number guessing game***')

def is_valid(s):
    if s.isdigit() and 1 <= int(s) <= 100:
        return True
    return False

attempts = 0
while True:
    attempts += 1
    num = input('Please enter number from 1 to 100')
    if is_valid(num) == False:
        print('Maybe you can still enter an integer from 1 to 100?')
    else:
        num = int(num)
        if num < random_num:
            print('Your number is lower than your guess, try again.')
        elif num > random_num:
            print('Your number is higher than your guess, try again.')
        elif num == random_num:
            print("You guessed it, congratulations!!!")
            break
print('Number of attempts:', attempts)
print('Thanks for playing the number guessing game. See you...')