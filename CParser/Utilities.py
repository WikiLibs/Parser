from sys import stderr
from cindex import *
import CustomContainers as CC
import StringOperations as StrOp

OPUS_COMMENT_PARAM = "\\param"

TYPE_PUNC   = "TokenKind.PUNCTUATION"
TYPE_ID     = "TokenKind.IDENTIFIER"
TYPE_COMM   = "TokenKind.COMMENT"
TYPE_KEYW   = "TokenKind.KEYWORD"

PUNC_HASH   = "#"

ID_DEFINE   = "define"

def printErr(*msg, **kwargs):
    print(*msg, file=stderr, **kwargs)

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
        tmpTab = StrOp.removeSpaces(tmpParamTab[i]).split(' ')
        tmpParam = CC.paramClass()
        tmpParam.varName = tmpTab[-1]
        tmpParam.varType = " ".join(tmpTab[:-1])
        tmpParam = getFuncParamDesc(comment, tmpParam, i)
        params.append(tmpParam)
    return params

def getFuncParamDesc(comment, tmpParam, index):
    if OPUS_COMMENT_PARAM in comment:
        paramDesc = StrOp.getIteration(comment, OPUS_COMMENT_PARAM, index)
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
        paramDesc = StrOp.getIteration(comment, OPUS_COMMENT_PARAM, index).split(':')
        if (len(paramDesc) < 2):
            return tmpParam
        tmpParam.varDesc = StrOp.removeUseless(StrOp.removeSpaces(paramDesc[1]))
        tmpParam.varType = " ".join(paramDesc[0].split(' ')[1:])
    return tmpParam

