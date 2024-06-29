def print_if_exist(prompt: str | None) -> None:
    if prompt is not None:
        print(prompt)


def validate_int_in_range(string: str, min: int, max: int, input_empty_prompt: str | None = None, input_not_number_prompt: str | None = None, input_not_int_prompt: str | None = None, input_not_in_range_prompt: str | None = None) -> int | None:
    # no input (empty)
    if not string:
        print_if_exist(input_empty_prompt)
        return None

    # input is not a number
    try:
        float(string)
    except ValueError:
        print_if_exist(input_not_number_prompt)
        return None

    # input not an int
    try:
        result: int = int(string)
    except ValueError:
        print_if_exist(input_not_int_prompt)
        return None

    # input not in range
    if not min <= result <= max:
        print_if_exist(input_not_in_range_prompt)
        return None

    return result


def validate_int(string: str, input_empty_prompt: str | None = None, input_not_number_prompt: str | None = None, input_not_int_prompt: str | None = None):
    # no input (empty)
    if not string:
        print_if_exist(input_empty_prompt)
        return None

    # input is not a number
    try:
        float(string)
    except ValueError:
        print_if_exist(input_not_number_prompt)
        return None

    try:
        result: int = int(string)
    except ValueError:
        print_if_exist(input_not_int_prompt)
        return None

    return result


def validate_float(string: str, input_empty_prompt: str | None = None, input_not_float_prompt: str | None = None) -> float | None:
    # no input (empty)
    if not string:
        print_if_exist(input_empty_prompt)
        return None

    # input is not a float (or any number for that matter)
    try:
        result: float = float(string)
    except ValueError:
        print_if_exist(input_not_float_prompt)
        return None

    return result


def validate_str_in_list_case_insensitive(string: str, options: tuple[str, ...], default_value: str | None = None, input_not_in_list_prompt: str | None = None) -> str | None:
    options_case_insensitive: tuple[str, ...] = tuple(
        option.casefold() for option in options)

    if default_value is not None:
        # default option is not in
        if default_value.casefold() not in options_case_insensitive:
            raise ValueError('Default option not in list of options')

        # no input (empty)
        if not string:
            return default_value

    # input is not an option
    if string.casefold() not in options_case_insensitive:
        print_if_exist(input_not_in_list_prompt)
        return None

    return string
