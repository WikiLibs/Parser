#!/usr/bin/env python3.6
import xml.etree.ElementTree as ET
import argparse
import parserDoxygenXML
import useful

DESCRIPTION = 'This program will parse a library and send it to the WikiLibs API.'
LANGUAGE_HELP = 'sets the language used in the library (please check WikiLibs documentation to check the currently supported languages)'
NAME_HELP = 'sets the name of the library to be send'
VERBOSE_HELP = 'shows more infos in the output'

dicoLang = {
    "C" : [ '.h', '.c' ],
    "Python" : [ '.py' ]
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


def main():
    argParser = argparse.ArgumentParser(description=DESCRIPTION)
    argParser.add_argument('language', help=LANGUAGE_HELP)
    argParser.add_argument('library_name', help=NAME_HELP)
    argParser.add_argument('-v', '--verbose', help=VERBOSE_HELP, action='store_true')
    args = argParser.parse_args()

    if args.verbose:
        useful.verbose = args.verbose
    useful.printVerbose("Language = " + args.language)
    useful.printVerbose("Library name = " + args.library_name + "\n")

    files = getAllFiles(args.language)
    for filename in files:
        useful.printVerbose("Starting parsing \'" + filename.ogFilename + "\'")
        parserDoxygenXML.parseXMLFile(filename.xmlFilename)

if __name__ == '__main__':
    main()