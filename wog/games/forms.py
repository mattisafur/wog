from typing import Any, Mapping
from django import forms
from django.core import validators
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList


class DifficultySelectionForm(forms.Form):
    def __init__(self, *args, difficulties: list[tuple[str, str]], **kargs):
        super().__init__(*args, **kargs)

        self.fields["difficulty"] = forms.ChoiceField(
            choices=difficulties, widget=forms.RadioSelect, label="Choose a difficulty"
        )


class GuessGameUserGuessForm(forms.Form):
    def __init__(self, *args, max_value: int, **kargs) -> None:
        super().__init__(*args, **kargs)

        self.fields["user_guess"] = forms.IntegerField(
            label=f"Guess a number between 0 and {max_value}",
            validators=[
                validators.MinValueValidator(0),
                validators.MaxValueValidator(max_value),
            ],
        )
