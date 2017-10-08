def checkio(number: int) -> str:
    result = []
    if (number % 3) == 0:
        result.append("Fizz")
    if (number % 5) == 0:
        result.append("Buzz")

    if not result:
        result.append(str(number))

    return " ".join(result)
