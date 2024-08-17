"Currency Roulette Game"
import os
import random
import currencyapicom
import input_validation

name: str = 'Currency Roulette'
short_description: str = 'Try and guess the value of a random amount of USD in ILS'
full_description: str = '''An amount in USD between 1 and 100 will be chosen at random.
You must enter an amount in shekels equal to the given amount.
The error margin allowed in your answer depends on the difficulty level selected.'''
difficulties: list[str] = ["easy", "easy-medium", "medium", "medium-hard", "hard"]


def play(difficulty: str) -> bool:
    "Starts executing the game"
    error_margin: int = 10 - (difficulties.index(difficulty) + 1)
    if error_margin < 0:
        raise ValueError("Difficulty value too high, negative error margin.")
    amount: int = random.randint(1, 100)

    # print intro
    print(name)
    print("=" * len(name), end="\n\n")
    print(full_description, end="\n\n")
    print(f"Difficuly {difficulty} - margin of {error_margin} ILS.", end="\n\n")

    print(f"The amount to convert is: {amount} USD", end="\n\n")

    answer_range: tuple[float, float] = get_money_interval(amount, error_margin)
    guess: float = get_guess_from_user()

    return compare_results(guess, answer_range)


def get_money_interval(number: int, error_margin: int) -> tuple[float, float]:
    "Calculates the range of correct answers using the actual answer and an error magrin"
    exchange_rates = currencyapicom.Client(get_api_credentials()).latest()
    ils_exchange_rate: float = (exchange_rates.get("data", {}).get("ILS", {}).get("value"))
    converted_number: float = number * ils_exchange_rate

    return (converted_number - error_margin, converted_number + error_margin)


def get_guess_from_user() -> float:
    "Retrieves guess the user"
    while True:
        guess: str = input("Enter your guess: ")
        parsed_guess: float | None = input_validation.validate_float(guess)
        if parsed_guess is not None:
            return parsed_guess


def compare_results(user_input: float, answer_range: tuple[float, float]) -> bool:
    "Checkes if the user's input is in range"
    return answer_range[0] <= user_input <= answer_range[1]


def get_api_credentials() -> str:
    "Retrieves API credentials for the exchnage rate API"
    api_key: str | None = os.getenv("CURRENCY_API_KEY")
    if api_key is None:
        raise ValueError("Environment variable CURRENCY_API_KEY is not defined")
    return api_key
