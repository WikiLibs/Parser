from sys import stderr
from cindex import *
import CustomContainers as CC

OPUS_COMMENT_PARAM = "\\param"

TYPE_PUNC   = "TokenKind.PUNCTUATION"
TYPE_ID     = "TokenKind.IDENTIFIER"
TYPE_COMM   = "TokenKind.COMMENT"
TYPE_KEYW   = "TokenKind.KEYWORD"

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
        #if (content[index].tokType == TYPE_ID or content[index].tokType == TYPE_KEYW) and content[index + 1].tokType == TYPE_ID and content[index + 2].tokContent == '(' and content[index - 1].tokContent != PUNC_HASH:
        if (content[index].tokType == TYPE_ID or content[index].tokType == TYPE_KEYW) and content[index - 1].tokContent != PUNC_HASH: 
            while content[index + 1].tokType == TYPE_PUNC and (content[index + 1].tokContent == "*" or content[index + 1].tokContent == "&"):
                index += 1
            if content[index + 1].tokType == TYPE_ID and content[index + 2].tokContent == '(':
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
    i = 0
    while (iter <= index):
        i = string.find(sep, i) + len(sep) + 1
        iter += 1
    
    j = string.find(sep, i)
    if j != -1:
        return string[i:j]
    else:
        return string[i:]

def getMacroParams(content, index, comment):
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
        tmpParam = getMacroParamDesc(comment, tmpParam, i)
        params.append(tmpParam)
    return params

def getFuncParams(content, index, comment):
    params = []
    tmpStr = ""
    i = 0
    while content[index + i].tokContent != '(':
        i += 1
    i += 1
    while content[index + i].tokContent != ')':
        if (content[index + i].tokType == "TokenKind.LITERAL"):
            return []
        tmpStr += " " + content[index + i].tokContent
        i+= 1
    tmpParamTab = tmpStr.split(',')
    for i in range(len(tmpParamTab)):
        tmpTab = removeSpaces(tmpParamTab[i]).split(' ')
        tmpParam = CC.paramClass()
        tmpParam.varName = tmpTab[-1]
        tmpParam.varType = " ".join(tmpTab[:-1])
        tmpParam = getFuncParamDesc(comment, tmpParam, i)
        params.append(tmpParam)
    return params

def getFuncParamDesc(comment, tmpParam, index):
    if OPUS_COMMENT_PARAM in comment:
        paramDesc = getIteration(comment, OPUS_COMMENT_PARAM, index)
        '''if "\\return" in paramDesc:
            paramDesc = paramDesc[:paramDesc.find("\\return")]'''
        paramDesc = paramDesc[:paramDesc.find("\\return")] if ("\\return" in paramDesc) else paramDesc
        paramDesc = paramDesc[:paramDesc.find("\\retval")] if ("\\retval" in paramDesc) else paramDesc
        paramDesc = paramDesc[len("out] "):] if paramDesc.startswith("out] ") else paramDesc
        paramDesc = paramDesc[len("in] "):] if paramDesc.startswith("in] ") else paramDesc
        tmpParam.varDesc = paramDesc
    return tmpParam

def getMacroParamDesc(comment, tmpParam, index):
    if OPUS_COMMENT_PARAM in comment:        #if opus headers
        paramDesc = getIteration(comment, OPUS_COMMENT_PARAM, index).split(':')
        if (len(paramDesc) < 2):
            return tmpParam
        tmpParam.varDesc = removeUseless(removeSpaces(paramDesc[1]))
        tmpParam.varType = " ".join(paramDesc[0].split(' ')[1:])
    return tmpParam

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
    if OPUS_COMMENT_PARAM in string:
        string = string[:string.find(OPUS_COMMENT_PARAM) - 1]
    return string