import collections
import operator
import string


def checkio(text: str) -> str:
    only_letters = (char.lower() for char in text
                    if char in string.ascii_letters)
    counter = collections.Counter(only_letters)
    most_common = sorted(counter.items(), key=operator.itemgetter(0))
    return sorted(most_common, key=operator.itemgetter(1), reverse=True)[0][0]
