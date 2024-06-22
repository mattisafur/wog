import input_validation
from games import currency_roulette_game, guess_game, memory_game

games = [
    memory_game,
    guess_game,
    currency_roulette_game
]


def welcome() -> None:
    player_name = input('Please enter your name: ')
    print(f'Hi {player_name} and welcome to the World of Games: The Epic Journey')
    return


def start_play() -> None:
    # game selection
    print('Please choose a game to play:')
    for index, game in enumerate(games):
        print(f'{index + 1}. {game.name} - {game.short_description}')

    while True:
        game_number = input('> ')
        game_number = input_validation.validate_int_in_range(game_number, 1, len(
            games), input_not_number_prompt='Please enter a number', input_not_int_prompt='Please enter an integer', input_not_in_range_prompt='Input is not a valid option')
        if game_number is not None:
            break
    game = games[game_number - 1]

    # difficulty selection
    print('Please select a difficulty:')
    for index, difficulty in enumerate(game.difficulties):
        print(f'{index + 1}. {difficulty}')

    while True:
        difficulty_level = input('> ')
        difficulty_level = input_validation.validate_int_in_range(difficulty_level, 1, len(
            game.difficulties), input_not_number_prompt='Please enter a number', input_not_int_prompt='Please enter an integer', input_not_in_range_prompt='Input is not a valid option')
        if difficulty_level is not None:
            break
    difficulty = game.difficulties[difficulty_level - 1]

    # start selected game
    game.play(difficulty)
