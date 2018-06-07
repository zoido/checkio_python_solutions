def checkio(text: str) -> bool:
    counter = 0
    for segment in text.split():
        if segment.isalpha():
            counter += 1
        else:
            counter = 0
        if counter >= 3:
            return True
    return False
