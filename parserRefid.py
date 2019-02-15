#!/usr/bin/env python3.6
import xml.etree.ElementTree as ET
from sys import argv as av



def getRefid(langage, path):
    dicoLang = {}
    dicoLang["langage=C"] = ['.h', '.c']
    dicoLang["langage=Python"] = ['.py']
    parserRefid(dicoLang.get(langage), path)


def parserRefid(extend, path):
    name = []
    root = ET.parse(path).getroot()
    for child in root:
        kind = child.get('kind')
        if kind == 'file':
            for intForName in child.iter('name'):
                for elemExtend in extend :
                    if intForName.text.find(elemExtend) >= 0 : 
                        name.append(child.get('refid') + '.xml')
    for strname in name:
        print(strname)
    return name

# ./pazerRefid opusfile8h.xml
# def main():
#     getRefid("langage=C", av[1])




# if __name__ == '__main__':
#     main()