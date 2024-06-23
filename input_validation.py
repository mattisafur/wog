def validate_int_in_range(string: str, min: int, max: int, input_empty_prompt: str | None = None, input_not_number_prompt: str | None = None, input_not_int_prompt: str | None = None, input_not_in_range_prompt: str | None = None) -> int | None:
    # no input (empty)
    if not string:
        if input_empty_prompt is not None:
            print(input_empty_prompt)
        return None

    # input is not a number
    try:
        float(string)
    except ValueError:
        if input_not_number_prompt is not None:
            print(input_not_number_prompt)
        return None

    # input not an int
    try:
        result: int = int(string)
    except ValueError:
        if input_not_int_prompt is not None:
            print(input_not_in_range_prompt)
        return None

    # input not in range
    if not min <= result <= max:
        if input_not_in_range_prompt is not None:
            print(input_not_in_range_prompt)
        return None

    return result


def validate_int(string: str, input_empty_prompt: str | None = None, input_not_number_prompt: str | None = None, input_not_int_prompt: str | None = None):
    # no input (empty)
    if not string:
        if input_empty_prompt is not None:
            print(input_empty_prompt)
        return None

    # input is not a number
    try:
        float(string)
    except ValueError:
        if input_not_number_prompt is not None:
            print(input_not_number_prompt)
        return None

    try:
        result: int = int(string)
    except ValueError:
        if input_not_int_prompt is not None:
            print(input_not_int_prompt)
        return None

    return result


def validate_float(string: str, input_empty_prompt: str | None = None, input_not_float_prompt: str | None = None) -> float | None:
    # no input (empty)
    if not string:
        if input_empty_prompt is not None:
            print(input_empty_prompt)
        return None

    # input is not a float (or any number for that matter)
    try:
        result: float = float(string)
    except ValueError:
        if input_not_float_prompt is not None:
            print(input_not_float_prompt)
        return None

    return result
