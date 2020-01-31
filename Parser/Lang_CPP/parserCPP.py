import xml.etree.ElementTree as ET
from languageInterface import LanguageInterface

class parserCPP(LanguageInterface):
    def getSymbols(self, filename):
        print(filename)
        root = ET.parse(filename).getroot()

        for elem in root.iter('memberdef'):
            kind = elem.get('kind')
            print(kind)

        for elem in root.iter('innerclass'):
            refid = elem.get('refid')
