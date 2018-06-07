import string

MINIMAL_LENGTH = 10
DIGITS = set(string.digits)
LOWER_CHARS = set(string.ascii_lowercase)
UPPER_CHARS = set(string.ascii_uppercase)


def checkio(password: str) -> bool:
    password_characters = set(password)
    return (
        len(password) >= MINIMAL_LENGTH
        and (not password_characters.isdisjoint(DIGITS))
        and (not password_characters.isdisjoint(LOWER_CHARS))
        and (not password_characters.isdisjoint(UPPER_CHARS))
    )
