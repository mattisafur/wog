"Score managements"
import input_validation

SCORE_FILE_NAME: str = "Score.txt"


def add_score(difficutly_number: int) -> None:
    """
    Appends a score to the score file.
    If the file does not exist it creates a new file writes the score into it
    """
    points: int = (difficutly_number * 3) + 5

    with open(SCORE_FILE_NAME, "w+", encoding="ascii") as scores_file:
        score_file_value: str = scores_file.read()

        if score_file_value:
            previous_score: int = 0
            try:
                # parse save file
                previous_score = int(score_file_value)
            except ValueError:
                # save file is corrupted, let user choose between clearing the score file or quitting the program
                options: tuple[str, ...] = ("y", "yes", "n", "no")
                default_option: str = "n"

                while True:
                    user_input: str = input(
                        "Score file is corrupted, would you like to clear it? [yes/No]: "
                    )
                    user_selection = (
                        input_validation.validate_str_in_list_case_insensitive(
                            user_input,
                            options,
                            default_option,
                            input_not_in_list_prompt="Invalid input.",
                        )
                    )

                    if user_selection is None:
                        break

                    match user_input.casefold():
                        case "y" | "yes":
                            # clear file and set score to 0
                            scores_file.write("")
                            previous_score = 0
                            break
                        case "n" | "no":
                            print("Quitting.")
                            quit()
        else:
            previous_score: int = 0

        score: int = previous_score + points

        scores_file.seek(0)
        scores_file.write(str(score))
        scores_file.truncate()
