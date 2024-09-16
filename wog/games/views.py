from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .forms import DifficultySelectionForm, GuessGameUserGuessForm
from .games import guessing_game as guessing_game_module


def guessing_game(request: HttpRequest) -> HttpResponse:
    difficulty: str | None = request.session.get("difficulty")

    if difficulty is None:
        difficulties: list[tuple[str, str]] = (
            guessing_game_module.get_form_difficulties()
        )
        if request.method == "POST":
            # add difficulty from form to session
            form = DifficultySelectionForm(request.POST, difficulties=difficulties)
            if form.is_valid():
                request.session["difficulty"] = form.cleaned_data["difficulty"]
        else:
            # prompt user to select a difficulty
            form = DifficultySelectionForm(difficulties=difficulties)
            return render(
                request,
                "guessing-game.html",
                {"difficulty_selected": False, "form": form},
            )

    # get max value from difficulty
    max_value: int = 0
    for name, number in guessing_game_module.DIFFICULTIES:
        if name == difficulty:
            max_value = number

    if request.method == "POST":
        form_prefix: str | None = request.POST["form-prefix"]
        match form_prefix:
            case "guess-form":
                # user guess form -> check if user won and render result page
                form = GuessGameUserGuessForm(
                    request.POST, max_value=max_value
                )  # TODO check if need to pass request
                if form.is_valid():
                    if form.cleaned_data.get("user_guess") == request.session.get(
                        "generate_number"
                    ):
                        return render(
                            request,
                            "guessing-game.html",
                            {
                                "difficulty_selected": True,
                                "guess_submitted": True,
                                "user_won": True,
                            },
                        )
                    else:
                        return render(
                            request,
                            "guessing-game.html",
                            {
                                "difficulty_selected": True,
                                "guess_submitted": True,
                                "user_won": False,
                            },
                        )
            case None:
                # replay form -> check which option user chose and follow through
                if "play-again" in request.POST:
                    pass
                elif "select-difficulty" in request.POST:
                    redirect("guessing_game")
                elif "go-home" in request.POST:
                    # TODO redirect to home
                    pass
            case _:
                raise ValueError("invalid form prefix")

    # generate random number based on difficulty
    request.session["generated_number"] = guessing_game_module.generate_number(
        max_value
    )

    # render game
    form = GuessGameUserGuessForm(prefix="guess-form", max_value=max_value)
    return render(
        request,
        "guessing-game.html",
        {"difficulty_selected": True, "guess_submitted": False, "form": form},
    )

    # # get difficulty
    # if difficulty not selected:
    #     if request is post:
    #         # set difficulty
    #         # maybe? redirect to same view
    #     else:
    #         # render difficulty selection

    # if request is post:
    #     if post is valid:
    #         get post id
    #         match post id:
    #             case game submission:
    #                 # get user guess
    #                 # check if user won
    #                 # render win page
    #             case replay option:
    #                 match selection:
    #                     case play again:
    #                         # pass
    #                     case select difficulty:
    #                         # remove difficulty from session
    #                         # reload
    #                     case go home:
    #                         # redirect to home

    # # render game
