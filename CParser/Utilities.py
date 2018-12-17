from sys import stderr
from cindex import *
import CustomContainers as CC

OPUS_COMMENT_PARAM = "\\param"

TYPE_PUNC   = "TokenKind.PUNCTUATION"
TYPE_ID     = "TokenKind.IDENTIFIER"
TYPE_COMM   = "TokenKind.COMMENT"

PUNC_HASH   = "#"

ID_DEFINE   = "define"

USELESS = [
    "<code>",
    "</code>",
    "<tt>",
    "</tt>",
    "\\hideinitializer",
    "/*",
    "*/"
]

def printErr(*msg, **kwargs):
    print(*msg, file=stderr, **kwargs)

def removeSpaces(string):
    string.split()
    string = " ".join(string.split())
    return string

def isMacro(content, index):
    if (content[index].tokType == TYPE_PUNC and content[index].tokContent == PUNC_HASH) and (content[index + 1].tokType == TYPE_ID and content[index + 1].tokContent == ID_DEFINE):
        if content[index + 3].tokContent == "(":
            return True

    return False

def isFunction(content, index):
    try:
        if content[index].tokType == TYPE_ID and content[index + 1].tokType == TYPE_ID and content[index + 2].tokContent == '(' and content[index - 1].tokContent != PUNC_HASH:
            return True
    except:
        return False
    return False

def getComment(content, index):
    i = 0
    while content[index].tokType != TYPE_COMM:
        index -= 1
    string = str(content[index].tokContent)
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

def getIteration(string, sep, index):
    iter = 0
    i = string.find(sep)
    while iter <= index:
        if (string[i:].startswith(sep)):
            iter += 1
        i += 1
    j = string[i:].find(sep)
    i = i + len(sep)
    if j != -1:
        return string[i:j]
    return string[i:]

def getParams(content, index, comment):
    params = []
    tmpStr = ""
    i = 0
    while content[index + i].tokContent != '(':
        i += 1
    i += 1
    while content[index + i].tokContent != ')':
        if (content[index + i].tokType == "TokenKind.LITERAL"):
            return []
        tmpStr += content[index + i].tokContent
        i+= 1
    tmpParamTab = tmpStr.split(',')
    for i in range(len(tmpParamTab)):
        tmpParam = CC.paramClass()
        tmpParam.varName = tmpParamTab[i]
        tmpParam = getParamDesc(comment, tmpParam, i)
        params.append(tmpParam)
    return params


def getParamDesc(comment, tmpParam, index):
    if OPUS_COMMENT_PARAM in comment:        #if opus headers
        paramDesc = getIteration(comment, OPUS_COMMENT_PARAM, index).split(':')
        tmpParam.varDesc = removeUseless(removeSpaces(paramDesc[1]))
        tmpParam.varType = " ".join(paramDesc[0].split(' ')[1:])
    return tmpParam

def removeUseless(string):
    for word in USELESS:
        if word in string:
            string = string.replace(word, "")
    return string

def rerunRemove(string):
    if OPUS_COMMENT_PARAM in string:
        string = string[:string.find(OPUS_COMMENT_PARAM) - 1]
    return string
