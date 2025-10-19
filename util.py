from enum import Enum


class ValidOptions(Enum):
    top = 'a'
    bottom = 's'


class PlayAgainOptions(Enum):
    positive = 'y'
    negative = 'n'


def get_valid_user_input(sentence: str, valid_options: Enum) -> str:
    valid_values = [option.value for option in valid_options]
    while True:
        user_response = str(input(f"{sentence}")).strip().lower()
        if user_response in valid_values:
            return user_response
        else:
            print("Invalid input")
