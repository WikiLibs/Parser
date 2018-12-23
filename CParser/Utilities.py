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
    saveindex = index
    while content[index].tokType != TYPE_COMM:
        index -= 1
    if saveindex - index > 2:
        return ""
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

def getTypedefStruct(content, index):
    tmpTypedef = CC.typedefClass()
    tmpTypedef.tdLeft = content[index + 1].tokContent + " " + content[index + 2].tokContent
    tmpTypedef.tdRight = content[index + 3].tokContent
    return tmpTypedef

def getTypedefOther(content, index):
    tmpTypedef = CC.typedefClass()
    tmpStr = ""
    i = index + 1
    while content[i].tokContent != ';':
        tmpStr += content[i].tokContent + " "
        i += 1
    tmpTypedef.tdLeft = tmpStr
    return tmpTypedef

def getStruct(content, index, checkComment):
    tmpStruct = CC.structClass()
    tmpStruct.structName = content[index + 1].tokContent
    tmpStruct.structContents = []
    if checkComment:
        tmpStruct.structComment = StrOp.rerunRemove(StrOp.removeUseless(StrOp.removeSpaces(getComment(content, index))))
    index += 3
    while content[index].tokContent != '}':
        tmpParam = CC.paramClass()
        if content[index].tokType == TYPE_COMM and checkComment:
            tmpParam.varDesc = StrOp.rerunRemove(StrOp.removeUseless(StrOp.removeSpaces(content[index].tokContent)))
            index += 1
        tmpStr = ""
        while content[index].tokContent != ';':
            tmpStr += content[index].tokContent + " "
            index += 1
        tmpTab = StrOp.removeSpaces(tmpStr).split(" ")
        tmpParam.varName = tmpTab[-1]
        tmpParam.varType = " ".join(tmpTab[:-1])
        tmpStruct.structContents.append(tmpParam)
        index += 1
    return tmpStruct