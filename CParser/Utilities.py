from sys import stderr

def printErr(*msg, **kwargs):
    print(*msg, file=stderr, **kwargs)

def removeSpaces(string):
    string.split()
    string = " ".join(string.split())
    return string

def removeComments(string):
    i = 0
    string = str(string)
    if string.startswith("//"):
        while (string[i] == '/'):
            string = string[1:]
            i += 1
    elif string.startswith("/*"):
        string = string[2:]
        while (string[i] == '*'):
            string = string[1:]
            i += 1
        string = string[:-2]
        i = len(string) - 1
        while (string[i] == '*'):
            string = string[:-1]
            i -= 1
    return string