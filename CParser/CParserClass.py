import CustomContainers as CC
import Utilities as Util
from cindex import *

OPUS_COMMENT_PARAM = "\\param"

class CParser:
    def __init__(self, filename, comments):
        """ object which will parse and do the program """
        self.comments = comments
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
        if self.comments:
            tmpMacro.macroComment = Util.removeUseless(Util.removeSpaces(Util.getComment(self.content, i)))#(self.content[i - 1].tokContent)))
        tmpMacro.macroParams = Util.getMacroParams(self.content, i, tmpMacro.macroComment)
        tmpMacro.macroComment = Util.rerunRemove(tmpMacro.macroComment)
        return tmpMacro

    def parseFunc(self, i):
        tmpFunc = CC.functionClass()
        tmpFunc.funcType = self.content[i].tokContent
        tmpFunc.funcName = self.content[i + 1].tokContent
        if self.comments:
            tmpFunc.funcComment = Util.removeUseless(Util.removeSpaces(Util.getComment(self.content, i)))
        tmpFunc.funcParams = Util.getFuncParams(self.content, i, tmpFunc.funcComment)
        tmpFunc.funcComment = Util.rerunRemove(tmpFunc.funcComment)
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
        self.printFunctions()

    def printMacro(self):
        for macro in self.macros:
            print("def: {}\ncomment: {}\nparams: ".format(macro.macroDef, macro.macroComment))
            for param in macro.macroParams:
                print("  {} ({}): {} ".format(param.varName, param.varType, param.varDesc))
            print()
        print(len(self.macros))

    def printFunctions(self):
        for func in self.functions:
            print("type: {}, name: {}\ncomment: {}\nparams: ".format(func.funcType, func.funcName, func.funcComment))
            for param in func.funcParams:
                print("  {} ({}): {} ".format(param.varName, param.varType, param.varDesc))
            print()
        print(len(self.functions))