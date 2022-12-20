import random

def guess(min_num, max_num, allowed_guess):

    target = random.randint(min_num, max_num)

    last_guess = None
    print('Let\'s start our guessing!')
    while allowed_guess > 0:
        user_input = int(input(f'Please make a guess between {min_num} and {max_num}: ' ))
        if user_input == target:
            user_input = input('Congrats! Wanna try again[y/n]? ')
            if user_input.upper() == 'Y':
                start_game()
                return
            else:
                print('See you again!')
                return
        else:
            if user_input > target:
                print('Too Big!')
                if last_guess:
                    if abs(last_guess - target) > abs(user_input - target):
                        print('Warmer')
                    else:
                        print('Colder')
            else:
                print('Too Small!')
                if last_guess:
                    if abs(last_guess - target) > abs(user_input - target):
                        print('Warmer')
                    else:
                        print('Colder')

        last_guess = user_input
        allowed_guess -= 1

    user_input = input(f'You\'ve lost! Correct answer is {target}. Wanna try again[y/n]? ')
    if user_input.upper() == 'Y':
        start_game()
    else:
        print('See you again!')
        return

def start_game():
    input1 = input('Input a min value, a max value, allowed guess allowed, seperated by commas: ')
    min_num, max_num, allowed_guess = input1.split(',')
    guess(int(min_num), int(max_num), int(allowed_guess))

start_game()
'''
















































'''
