import xml.etree.ElementTree as ET
from languageInterface import LanguageInterface
from Parser.useful import filesClass
from Parser.Lang_CPP.parseFile import parseFile
from Parser.Lang_CPP.parseClass import parseClass

kindTable = {
    "file": parseFile,
    "class": parseClass
}

class parserCPP(LanguageInterface):
    def getAllParseableFiles(self):
        files = []
        root = ET.parse("./xml/index.xml").getroot()

        for child in root.iter("compound"):
            if (child.get('kind') != 'dir'):
                tmp = filesClass()
                tmp.ogFilename = child.find('name').text
                tmp.xmlFilename = "./xml/" + child.get('refid') + ".xml"
                files.append(tmp)
        return (files)

    def getSymbols(self, filename):
        root = ET.parse(filename).getroot()

        cpdef = root.find("compounddef")
        kind = cpdef.get("kind")

        syms = []
        if (kind in kindTable):
            syms = kindTable[kind](root)

        for s in syms:
            self.appendToSymbols("generic", s)
