import random


DIFFICULTIES: list[tuple[str, int]] = [
    ("easy", 1),
    ("easy-medium", 2),
    ("medium", 3),
    ("medium-hard", 4),
    ("hard", 5),
]


def generate_number(max_number: int) -> int:
    return random.randint(0, max_number)


def get_form_difficulties() -> list[tuple[str, str]]:
    form_difficulties: list[tuple[str, str]] = []
    for difficulty_name, difficulty_value in DIFFICULTIES:
        form_difficulties.append(
            (
                difficulty_name,
                f"{difficulty_name} - number generated between 0 and {difficulty_value}",
            )
        )
    return form_difficulties
