import math
import random


def get_valid_number(minimum_number, maximum_number, prompt):
    is_valid_input = False
    while not is_valid_input:
        lower_bound = int(input(f'Write the {prompt} number: '))

        if minimum_number <= lower_bound < maximum_number:
            is_valid_input = True
        else:
            print('Your input is not valid, it must be greater than 0. Try again.')
    
    return lower_bound


lower_bound = get_valid_number(0, math.inf)
upper_bound = get_valid_number(lower_bound + 1, math.inf)
trials_number = get_valid_number(1, upper_bound - lower_bound)

secret_number = random.randint(lower_bound, upper_bound)


user_win = False
for i in range(trials_number):
    user_guest = int(input('Write the number: '))

    if user_guest > secret_number:
        print('Too high')
    elif user_guest < secret_number:
        print('Too low')
    else:
        user_win = True
        break

if user_win:
    print('You win')
else:
    print('You lose')
