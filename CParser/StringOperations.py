
COMMENT_EPUR = [
    "\\param",
    "\\return",
    "\\retval"
]

USELESS = [
    "<code>",
    "</code>",
    "<tt>",
    "</tt>",
    "\\hideinitializer",
    "/*",
    "*/"
]

def getIteration(string, sep, index):
    iter = 0
    i = 0
    while (iter <= index):
        i = string.find(sep, i) + len(sep) + 1
        iter += 1
    
    j = string.find(sep, i)
    if j != -1:
        return string[i:j]
    else:
        return string[i:]

def removeUseless(string):
    for word in USELESS:
        if word in string:
            string = string.replace(word, "")
        string = removeConsecutive(string, "/")
    return string

def removeConsecutive(string, char):
    counter = 0
    newStr = ""
    for i in range(len(string)):
        if string[i] == char:
            counter += 1
            try:
                if newStr[-1] == char:
                    newStr = newStr[:-1]
            except:
                newStr = newStr
            if counter > 1:
                continue
        else:
            counter = 0
        newStr += string[i]
    newStr = removeSpaces(newStr)
    return newStr

def rerunRemove(string):
    for word in COMMENT_EPUR:
        if word in string:
            string = string[:string.find(word) - 1]
    return string


def removeSpaces(string):
    string.split()
    string = " ".join(string.split())
    return string
