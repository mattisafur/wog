"WOG application"
import input_validation
from games import currency_roulette_game, guess_game, memory_game
import score

games = [memory_game, guess_game, currency_roulette_game]


def welcome() -> None:
    "Prompts user to enter their name"
    player_name: str = input("Please enter your name: ")
    print(f"Hi {player_name} and welcome to the World of Games: The Epic Journey")
    return


def start_play() -> None:
    """Asks the user what game they want to play, run that game.
    appends the users score into a score file"""
    # game selection
    print("Please choose a game to play:")
    for index, game in enumerate(games):
        print(f"{index + 1}. {game.name} - {game.short_description}")

    while True:
        game_number: str = input("> ")
        parsed_game_number: int | None = input_validation.validate_int_in_range(
            game_number,
            1,
            len(games),
            input_not_number_prompt="Please enter a number",
            input_not_int_prompt="Please enter an integer",
            input_not_in_range_prompt="Input is not a valid option",
        )
        if parsed_game_number is not None:
            break
    game = games[parsed_game_number - 1]

    # difficulty selection
    print("Please select a difficulty:")
    for index, difficulty in enumerate(game.difficulties):
        print(f"{index + 1}. {difficulty}")

    while True:
        difficulty_level: str = input("> ")
        parsed_difficulty_level: int | None = input_validation.validate_int_in_range(
            difficulty_level,
            1,
            len(game.difficulties),
            input_not_number_prompt="Please enter a number",
            input_not_int_prompt="Please enter an integer",
            input_not_in_range_prompt="Input is not a valid option",
        )
        if parsed_difficulty_level is not None:
            break
    difficulty = game.difficulties[parsed_difficulty_level - 1]

    # start selected game
    win: bool = game.play(difficulty)

    if win:
        score.add_score(parsed_difficulty_level)
