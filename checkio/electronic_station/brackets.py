LEFT_BRACKETS = "({["
RIGHT_BRACKETS = ")}]"
BRACKETS = LEFT_BRACKETS + RIGHT_BRACKETS

RIGHT_TO_LEFT = dict(zip(RIGHT_BRACKETS, LEFT_BRACKETS))


def checkio(expression: str) -> bool:
    bracket_stack = []
    for char in expression:
        if char in BRACKETS:
            if char in LEFT_BRACKETS:
                bracket_stack.append(char)
            else:
                try:
                    popped_bracket = bracket_stack.pop()
                except IndexError:
                    return False
                if popped_bracket != RIGHT_TO_LEFT[char]:
                    return False
    return len(bracket_stack) == 0
