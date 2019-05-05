#!/usr/bin/env python3.6
import xml.etree.ElementTree as ET
from urllib.request import urlopen
import os
import argparse
import parserDoxygenXML
import useful
import PySimpleGUI as sg


DESCRIPTION = 'This program will parse a library and send it to the WikiLibs API.'
LANGUAGE_HELP = 'sets the language used in the library (please check WikiLibs documentation to check the currently supported languages)'
NAME_HELP = 'sets the name of the library to be send'
VERBOSE_HELP = 'shows more infos in the output'
GUI_HELP = 'set this option to use the GUI version'

dicoLang = {
    "C": ['.h', '.c'],
    "Python": ['.py']
}


class filesClass:
    ogFilename = ""
    xmlFilename = ""


def getAllFiles(language):
    global dicoLang
    global verbose
    files = []
    root = ET.parse("./xml/index.xml").getroot()
    extentions = dicoLang.get(language)

    useful.printVerbose("These files will be parsed:")
    for child in root:
        if child.get('kind') == 'file':
            filename = child.find('name').text
            for extension in extentions:
                if filename.endswith(extension):
                    tmp = filesClass()
                    tmp.ogFilename = filename
                    tmp.xmlFilename = "./xml/" + child.get('refid') + ".xml"
                    files.append(tmp)
                    useful.printVerbose("\t- " + filename)
    useful.printVerbose("")
    return files


def getDoxyfileAndRun():
    url = 'https://yuristudio.net/Doxyfile'
    with open('./Doxyfile', 'wb') as fd:
        fd.write(urlopen(url).read())
    os.system('doxygen Doxyfile > /dev/null')


def deleteFiles():
    os.system('rm -rf Doxyfile xml')


def parserArgs():
    argParser = argparse.ArgumentParser(description=DESCRIPTION)
    argParser.add_argument('language', help=LANGUAGE_HELP)
    argParser.add_argument('library_name', help=NAME_HELP)
    argParser.add_argument('-v', '--verbose', help=VERBOSE_HELP, action='store_true')
    argParser.add_argument('-g', '--gui', help=VERBOSE_HELP, action='store_true')
    args = argParser.parse_args()

    if args.verbose:
        useful.verbose = args.verbose
    if args.gui:
        event, (args.language, args.library_name,) = sg.Window('WikiLibs Parser').Layout([[sg.Text('Language')], [sg.InputCombo(['C', 'Python'], size=(20, 3))], [sg.Text('Library name')], [sg.InputText('')], [sg.OK(), sg.Cancel()] ]).Read()
    useful.printVerbose("Language = " + args.language)
    useful.printVerbose("Library name = " + args.library_name + "\n")

    return args


def main():

    args = parserArgs()    
    getDoxyfileAndRun()

    files = getAllFiles(args.language)
    for filename in files:
        useful.printVerbose("Starting parsing \'" + filename.ogFilename + "\'")
        parserDoxygenXML.parseXMLFile(filename.xmlFilename, args.language, args.library_name)

    deleteFiles()


if __name__ == '__main__':
    main()
