import re


def epurStr(string):
    return re.sub(' +', ' ', string.strip()).strip().replace('\n', '').replace('\r', '').replace('\t', '')


def removePointerSpace(string):
    tmp = [m.start() for m in re.finditer(r'\*', string)]
    for index in tmp:
        if string[index - 1] == ' ':
            string = string[:index - 1] + string[index:]
    return string
