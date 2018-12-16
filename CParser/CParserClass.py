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

    def parseDefine(self):
        self.defines = []
        for i in range(len(self.file)):
            if self.file[i].startswith("#define"):
                tmpDefine = CC.defineClass()
                tmpDefine.definition = self.file[i]
                if self.file[i].endswith("\\"):
                    tmpDefine.definition = tmpDefine.definition[:-1]
                    i += 1
                    tmpDefine.definition += self.file[i]
                tmpDefine.definition = Util.removeSpaces(tmpDefine.definition)
                tmpDefine.definition = tmpDefine.definition[len("#define "):]
                self.defines.append(tmpDefine)
                print(tmpDefine.definition)
        #print(len(self.defines))

    def printFile(self):
        for line in self.file:
            print(line)