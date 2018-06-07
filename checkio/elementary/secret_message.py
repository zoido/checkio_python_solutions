def find_message(message: str) -> str:
    return "".join(c for c in message if c.isupper())
