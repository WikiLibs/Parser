#!/usr/bin/env python3.6
import xml.etree.ElementTree as ET
from sys import argv as av

from src.getDefine import getDefine

def main():
    defines = []
    root = ET.parse(av[1]).getroot()

    for elem in root.iter('memberdef'):
        if elem.get('kind') == 'define':
            defines = getDefine(elem, defines)

if __name__ == '__main__':
    main()