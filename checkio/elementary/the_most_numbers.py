def checkio(*args):
    if not args:
        return 0
    return max(args) - min(args)
