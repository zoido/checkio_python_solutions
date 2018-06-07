def checkio(str_number: str, base: int) -> int:
    try:
        return int(str_number, base)
    except ValueError:
        return -1
