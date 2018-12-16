from sys import stderr

def printErr(*msg, **kwargs):
    print(*msg, file=stderr, **kwargs)

def removeSpaces(string):
    string.split()
    string = " ".join(string.split())
    return string