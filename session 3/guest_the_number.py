import math
import random


def get_valid_number(minimum_number, maximum_number, prompt):
    is_valid_input = False
    while not is_valid_input:
        
        # SOLUCION 1
        # user_input = input(f'Write the {prompt} number: ')
        # if user_input.isdigit():
        #     lower_bound = int(user_input)
        # else:
        #     print(f'Your input is not valid, is must be a numeric value.')
        #     continue

        # SOLUCION 2
        try:
            lower_bound = int(input(f'Write the {prompt} number: '))
        except ValueError:
            print(f'Your input is not valid, is must be a numeric value.')
            continue

        if minimum_number <= lower_bound < maximum_number:
            is_valid_input = True
        else:
            print(f'Your input is not valid, it must be greater than {minimum_number} and menor que {maximum_number}. Try again.')
    
    return lower_bound


def get_user_input():
    lower_bound = get_valid_number(0, math.inf, "lower")
    upper_bound = get_valid_number(lower_bound + 1, math.inf, "upper")
    trials_number = get_valid_number(1, upper_bound - lower_bound, "trials")

    user_name = input('Please write your name: ')

    return lower_bound, upper_bound, trials_number, user_name


def execute_game(lower_bound, upper_bound, trials_number, user_name):
    secret_number = random.randint(lower_bound, upper_bound)

    user_win = False
    for i in range(trials_number):
        user_guest = get_valid_number(lower_bound, upper_bound, "guess")

        if user_guest > secret_number:
            print('Too high')
        elif user_guest < secret_number:
            print('Too low')
        else:
            user_win = True
            break

    if user_win:
        print(f'{user_name.capitalize()} you have won')
    else:
        print(f'{user_name.capitalize()} you are a loser')


def show_information():
    print('#' * 100)
    print('# Welcome to the best game ever')
    print('# The goal is to guess a secret number')
    print('# First you will be prompt to choose the interval for the secret number, and then the number of trials')
    print('#' * 100)


def main():
    # Show information about the game to the user
    show_information()

    # Get user input
    lower_bound, upper_bound, trials_number = get_user_input()

    # execute the game
    execute_game(lower_bound, upper_bound, trials_number)


try:
    main()
except KeyboardInterrupt:
    print('\nHasta luego, espero que vuelvas pronto!')
