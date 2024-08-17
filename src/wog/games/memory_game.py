"Memory Game"
import random
import time
import keyboard
import input_validation

name: str = "Memory Game"
short_description: str = (
    "A sequence of numbers will appear for 1 second and you have to guess it back."
)
full_description: str = """
A sequence of number will be randomly generated and be shown on the screen for 0.7 seconds.
You must type back the sequence of numbers, one number at a time.
The length of the sequence will depend of the difficulty chosen."""
difficulties: list[str] = ["easy", "easy-medium", "medium", "medium-hard", "hard"]


def play(difficulty: str) -> bool:
    "Starts executing the game"
    sequence_length: int = difficulties.index(difficulty) + 1
    sequence: list[int] = generate_sequence(sequence_length)

    # Print intro
    print(name)
    print("=" * len(name), end="\n\n")
    print(full_description, end="\n\n")
    print(f"Difficulty {difficulty} - {sequence_length} long sequence.", end="\n\n")

    # show ready prompt and wait for user input
    print("Press any key to show the sequence.", end="\r")
    _ = keyboard.read_key(suppress=True)

    # count down from 3
    for sec in range(3, 0, -1):
        print(f"\x1b[2K{sec}", end="\r")
        time.sleep(1)

    # display the sequence for 0.7 seconds
    print(" ".join(str(number) for number in sequence), end="\r")
    time.sleep(0.7)
    print("\x1b[2K")

    user_sequence: list[int] = get_list_from_user(sequence_length)

    return is_list_equal(sequence, user_sequence)


def generate_sequence(length: int) -> list[int]:
    "Generates a <length> long sequence of numbers"
    sequence: list[int] = []
    for _ in range(length):
        sequence.append(random.randint(1, 101))
    return sequence


def get_list_from_user(amount_of_numbers: int) -> list[int]:
    "Retrieves a sequence of numbers from the user"
    user_sequence: list[int] = []

    # get number from user and append it to the sequence
    number_id: int = 1
    while number_id <= amount_of_numbers:
        number: str = input(f"number {number_id} > ")
        parsed_number: int | None = input_validation.validate_int(
            number,
            input_not_number_prompt="please enter a number",
            input_not_int_prompt="please enter positive whole numbers only",
        )
        if parsed_number is not None:
            user_sequence.append(parsed_number)
            number_id += 1
        else:
            continue

    return user_sequence


def is_list_equal(answer: list[int], user_guess: list[int]) -> bool:
    "Checkes if the sequence given by the user is the same as the shown list"
    return user_guess == answer
