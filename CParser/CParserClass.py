import CustomContainers as CC
import Utilities as Util

class CParser:
    def __init__(self, filename):
        """ object which will parse and do the program """
        self.file = self.readFile(filename)
        self.parseDefine()

    def readFile(self, filename):
        """ reads conf file """
        myfile = open(filename, "r")
        content = []
        for line in myfile:
            line = line.replace("\n", "")
            if len(line) > 0:
                content.append(line)
        myfile.close()
        return content

    def parseDefineGetComment(self, line):
        line -= 1
        if self.file[line].endswith("*/"):
            tmpStr = self.file[line]
            line -= 1
            while (self.file[line + 1].startswith("/*") == False):
                tmpStr = self.file[line] + tmpStr
                line -= 1
            tmpStr = Util.removeSpaces(tmpStr)
            tmpStr = Util.removeComments(tmpStr)
        else:
            return ""
        return tmpStr

    def parseDefineGetDefinition(self, line):
        tmpStr = self.file[line]
        if self.file[line].endswith("\\"):
            tmpStr = tmpStr[:-1]
            tmpStr += self.file[line + 1]
        tmpStr = Util.removeSpaces(tmpStr)[len("#define "):].split(" ")[0]
        return tmpStr

    def parseDefine(self):
        self.defines = []
        for i in range(len(self.file)):
            if self.file[i].startswith("#define"):
                tmpDefine = CC.defineClass()
                tmpDefine.definition = self.parseDefineGetDefinition(i)
                tmpDefine.comment = self.parseDefineGetComment(i)
                self.defines.append(tmpDefine)

    def printFile(self):
        for line in self.file:
            print(line)