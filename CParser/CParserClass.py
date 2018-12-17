import CustomContainers as CC
import Utilities as Util
from cindex import *

OPUS_COMMENT_PARAM = "\\param"

class CParser:
    def __init__(self, filename):
        """ object which will parse and do the program """
        self.readFile(filename)
        self.initClang()
        self.parse()

    def readFile(self, filename):
        """ reads conf file """
        myfile = open(filename, "r")
        self.file = ""
        for line in myfile:
            line = line.replace("\n", "")
            if len(line) > 0:
                self.file += line
        myfile.close()

    def initClang(self):
        index = Index.create()
        tokens = index.parse('tmp.cpp', args=['std=c++11'], unsaved_files=[('tmp.cpp', self.file)], options=0)
        self.content = []
        for token in tokens.get_tokens(extent=tokens.cursor.extent):
            tmp = CC.tokenClass()
            tmp.tokType = str(token.kind)
            tmp.tokContent = str(token.spelling)
            tmp.tokRef = token
            self.content.append(tmp)

    def parseMacro(self, i):
        tmpMacro = CC.macroClass()
        tmpMacro.macroDef = self.content[i + 2].tokContent
        tmpMacro.macroComment = Util.removeUseless(Util.removeSpaces(Util.getComment(self.content, i)))#(self.content[i - 1].tokContent)))
        tmpMacro.macroParams = Util.getParams(self.content, i, tmpMacro.macroComment)
        tmpMacro.macroComment = Util.rerunRemove(tmpMacro.macroComment)
        return tmpMacro

    def parseFunc(self, i):
        tmpFunc = CC.functionClass()
        tmpFunc.funcType = self.content[i].tokContent
        tmpFunc.funcName = self.content[i + 1].tokContent
        tmpFunc.funcComment = Util.removeUseless(Util.removeSpaces(Util.getComment(self.content, i)))
        #tmpFunc.funcParams = Util.getParams(self.content, i, tmpFunc.funcComment)
        tmpFunc.funcComment = Util.rerunRemove(tmpFunc.funcComment)
        #print("{} {} {}\n".format(tmpFunc.funcType, tmpFunc.funcName, tmpFunc.funcComment))
        return tmpFunc

    def parse(self):
        self.macros = [] 
        self.functions = []
        for i in range (len(self.content)):
            if Util.isMacro(self.content, i):
                self.macros.append(self.parseMacro(i))
            elif Util.isFunction(self.content, i):
                self.functions.append(self.parseFunc(i))
        #self.printMacro()

    '''def parseMacroGetComment(self, line):
        line -= 1
        if self.file[line].endswith("*/"):
            tmpStr = self.file[line]
            line -= 1
            while (self.file[line + 1].startswith("/*") == False):
                tmpStr = self.file[line] + tmpStr
                line -= 1
            tmpStr = Util.removeComments(Util.removeSpaces(tmpStr))
            if OPUS_COMMENT_PARAM in tmpStr:
                tmpStr = Util.opusRemoveUseless(tmpStr)
        else:
            return ""
        return tmpStr

    def parseMacroGetDefinition(self, line):
        tmpStr = self.file[line]
        if self.file[line].endswith("\\"):
            tmpStr = tmpStr[:-1]
            tmpStr += self.file[line + 1]
        tmpStr = Util.removeSpaces(tmpStr)[len("#define "):].split(" ")[0]
        return tmpStr

    def parseMacroGetParams(self, tmpMacro):
        tmpParam = CC.paramClass()
        tmpStr = tmpMacro.definition
        params = []
        if ("(" in tmpStr):
            i = tmpStr.find('(') + 1
            j = tmpStr.find(')')
            paramsStr = Util.removeSpaces(tmpStr[i:j]).split(",")
            for i in range(len(paramsStr)):
                tmpParam.varName = paramsStr[i]
                tmpParam = Util.getParamDesc(tmpMacro, tmpParam, i)
                params.append(tmpParam)
        return params

    def paramMacroRerunComment(self, comment):
        if OPUS_COMMENT_PARAM in comment:
            comment = comment[:comment.find(OPUS_COMMENT_PARAM) - 1]
        return comment

    def parseSave(self):
        self.macros = []
        for i in range(len(self.file)):
            if self.file[i].startswith("#define"):
                tmpMacro = CC.defineClass()
                tmpMacro.definition = self.parseMacroGetDefinition(i)
                tmpMacro.comment = self.parseMacroGetComment(i)
                tmpMacro.params = self.parseMacroGetParams(tmpMacro)
                tmpMacro.comment = self.paramMacroRerunComment(tmpMacro.comment)
                self.macros.append(tmpMacro)
            elif "(" in self.file[i] and "#" not in self.file[i] and "/*" not in self.file[i]:
                print ("function: {}".format(self.file[i]))'''
                

    '''def printFile(self):
        for line in self.file:
            print(line)'''

    def printMacro(self):
        for macro in self.macros:
            print("def: {}\ncomment: {}\nparams: ".format(macro.macroDef, macro.macroComment))
            for param in macro.macroParams:
                print("  {} ({}): {} ".format(param.varName, param.varType, param.varDesc))
            print()
        print(len(self.macros))