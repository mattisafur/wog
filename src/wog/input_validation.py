"Funvtion for validating input"
def print_if_exist(prompt: str | None) -> None:
    "Receives a string or None and prints the input if it is a string"
    if prompt is not None:
        print(prompt)


def validate_int_in_range(
    string: str,
    lower_limit: int,
    upper_limit: int,
    input_empty_prompt: str | None = None,
    input_not_number_prompt: str | None = None,
    input_not_int_prompt: str | None = None,
    input_not_in_range_prompt: str | None = None,
) -> int | None:
    """
    Checkes if a value in a string is an integer and is in a specified range.
    reutrns the integer if passes, prints a prompt if fails check
    """
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
    if not lower_limit <= result <= upper_limit:
        print_if_exist(input_not_in_range_prompt)
        return None

    return result


def validate_int(
    string: str,
    input_empty_prompt: str | None = None,
    input_not_number_prompt: str | None = None,
    input_not_int_prompt: str | None = None,
) -> int | None:
    """
    Checkes if a value in a string is an integer.
    Returns the integer if passes, prints a prompt if fails check
    """
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


def validate_float(
    string: str,
    input_empty_prompt: str | None = None,
    input_not_float_prompt: str | None = None,
) -> float | None:
    """Checks if a value in a asting is a float.
    Returns the float if passes, prints a prompt if fails check
    """
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


def validate_str_in_list_case_insensitive(
    string: str,
    options: tuple[str, ...],
    default_value: str | None = None,
    input_not_in_list_prompt: str | None = None,
) -> str | None:
    """Checkes if a sting is in a specified list of strings.
    The check is case insensitive.
    Returns the string is passes, prints a prompt if fails check
    """
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
