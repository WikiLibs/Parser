import CustomContainers as CC
import Utilities as Util
import StringOperations as StrOp
import CheckType as CT

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
        comment = False
        for line in myfile:
            line = line.replace("\n", "")
            if "//" in line and comment == False and "://" not in line:
                line = "/*" + line
                comment = True
            elif "//" not in line and comment:
                self.file = self.file + "*/"
                comment = False
            if len(line) > 0:
                self.file += line + " "
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
            tmpMacro.macroComment = StrOp.removeUseless(StrOp.removeSpaces(Util.getComment(self.content, i)))#(self.content[i - 1].tokContent)))
        tmpMacro.macroParams = Util.getMacroParams(self.content, i, tmpMacro.macroComment)
        tmpMacro.macroComment = StrOp.rerunRemove(tmpMacro.macroComment)
        return tmpMacro

    def parseFunc(self, i):
        tmpFunc = CC.functionClass()
        tmpFunc.funcType = self.content[i].tokContent
        if self.content[i + 1].tokType == Util.TYPE_PUNC:
            tmpFunc.funcType += " "
        while self.content[i + 1].tokType == Util.TYPE_PUNC:
            tmpFunc.funcType += self.content[i + 1].tokContent
            i += 1
        tmpFunc.funcName = self.content[i + 1].tokContent
        if self.comments:
            tmpFunc.funcComment = StrOp.removeUseless(StrOp.removeSpaces(Util.getComment(self.content, i)))
        tmpFunc.funcParams = Util.getFuncParams(self.content, i, tmpFunc.funcComment)
        tmpFunc.funcComment = StrOp.rerunRemove(tmpFunc.funcComment)
        return tmpFunc

    def parseTypedef(self, i):
        tmpTypedef = CC.typedefClass()
        if self.content[i + 1].tokContent == "struct":
            tmpTypedef = Util.getTypedefStruct(self.content, i)
        else:
            tmpTypedef = Util.getTypedefOther(self.content, i)
        if self.comments:
            tmpTypedef.tdComment = StrOp.rerunRemove(StrOp.removeUseless(StrOp.removeSpaces(Util.getComment(self.content, i))))
        return tmpTypedef
    
    def parse(self):
        self.macros = [] 
        self.functions = []
        self.typedefs = []
        self.structs = []
        for i in range (len(self.content)):
            #print(self.content[i].tokType, self.content[i].tokContent)
            if CT.isMacro(self.content, i):
                self.macros.append(self.parseMacro(i))
            elif CT.isFunction(self.content, i):
                self.functions.append(self.parseFunc(i))
            elif CT.isTypedef(self.content, i):
                self.typedefs.append(self.parseTypedef(i))
            elif CT.isStruct(self.content, i):
                self.structs.append(Util.getStruct(self.content, i, self.comments))
        #self.printMacro()
        #self.printFunctions()
        #self.printTypedefs()
        self.printStructs()

    def printMacro(self):
        for macro in self.macros:
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
    
    def printTypedefs(self):
        for td in self.typedefs:
            print (td.tdLeft, td.tdRight, "\ncomment:", td.tdComment)
            print()
        print(len(self.typedefs))

    def printStructs(self):
        for struct in self.structs:
            print ("name:", struct.structName, ", desc:", struct.structComment)
            for param in struct.structContents:
                print("\ttype:", param.varType, ", name:", param.varName, ", comment:", param.varDesc)