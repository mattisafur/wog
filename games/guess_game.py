import random
import input_validation

name = 'Guess Game'
short_description = 'Guess a number and see if you chose like the computer.'
full_description = '''A random number, 0 or higher will be selected by the game. you must guess that number.
The range of number the game will choose from depends on the difficulty level selected.'''
difficulties = [
    'easy',
    'easy-medium',
    'medium',
    'medium-hard',
    'hard'
]


def play(difficulty: str) -> bool:
    difficulty_level = difficulties.index(difficulty) + 1

    # print intro
    print(name)
    print('='*len(name), end='\n\n')
    print(full_description, end='\n\n')
    print(f'Difficulty {difficulty} - number chosen between 0 and {difficulty_level}')

    number = generate_number(difficulty_level)
    guess = get_guess_from_user(difficulty_level)

    return compare_results(guess, number)


def generate_number(max_number: int) -> int:
    return random.randint(0, max_number)


def get_guess_from_user(max_number: int) -> int:
    while True:
        guess = input(f'please enter a number between 0 and {max_number}: ')
        guess = input_validation.validate_int_in_range(guess, 0, max_number, input_not_number_prompt='Please enter a number',input_not_int_prompt='Please enter an integer', input_not_in_range_prompt='Input is not in the specified range')
        if guess is not None:
            break
    return guess


def compare_results(user_guess: int, number: int) -> bool:
    return user_guess == number
