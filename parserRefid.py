#!/usr/bin/env python3.6
import xml.etree.ElementTree as ET
from sys import argv as av



def parserRefid(path, extend):
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
#     extend = ['.h', '.c']
#     parserRefid(av[1], extend)




# if __name__ == '__main__':
#     main()