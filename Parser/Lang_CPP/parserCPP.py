import xml.etree.ElementTree as ET
from languageInterface import LanguageInterface
from Parser.useful import filesClass

class parserCPP(LanguageInterface):
    def getAllParseableFiles(self):
        files = []
        root = ET.parse("./xml/index.xml").getroot()

        for child in root.iter("compound"):
            if (child.get('kind') != 'file' and child.get('kind') != 'dir'):
                tmp = filesClass()
                tmp.ogFilename = child.find('name').text
                tmp.xmlFilename = "./xml/" + child.get('refid') + ".xml"
                files.append(tmp)
        return (files)

    def getSymbols(self, filename):
        print(filename)
        root = ET.parse(filename).getroot()

        for elem in root.iter('memberdef'):
            kind = elem.get('kind')
            print(kind)

        for elem in root.iter('innerclass'):
            refid = elem.get('refid')
