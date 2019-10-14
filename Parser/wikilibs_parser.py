#!/usr/bin/env python3.6
import xml.etree.ElementTree as ET
from urllib.request import urlopen
import os
import argparse
import useful
import aiClient

import Lang_C_CPP.parserC as parserC
import Lang_Python.parserPython as parserPython
import Lang_Java.parserJava as parserJava


DESCRIPTION = 'This program will parse a library and send it to the WikiLibs API.'
LANGUAGE_HELP = 'sets the language used in the library (please check WikiLibs documentation to check the currently' \
    ' supported languages)'
NAME_HELP = 'sets the name of the library to be send'
VERBOSE_HELP = 'shows more infos in the output'
EXCEPTION_HELP = 'shows parser exception'
GUI_HELP = 'set this option to use the GUI version'
NO_UPLOAD_HELP = 'set this option to disable upload to API (useful for degug)'
API_KEY_HELP = 'set the API Key to use for authenticating with the API server'
SCR_KEY_HELP = 'set the secret Key to use for authenticating with the API server'

dicoLang = {
    "C": ['.h', '.c'],
    "PYTHON": ['.py'],
    "JAVA": ['.java']
}

dicoLangDoxy = {
    "C": "C",
    "PYTHON3": "PYTHON"
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


def getDoxyfileAndRun(language):
    url = 'https://wikilibs-parser.azurewebsites.net/doxyfiles/' + dicoLangDoxy[language] + '/Doxyfile'
    with open('./Doxyfile', 'wb') as fd:
        fd.write(urlopen(url).read())

    if language == 'PYTHON3':
        url = 'https://wikilibs-parser.azurewebsites.net/doxyfiles/' + dicoLangDoxy[language] + '/py_filter'
        with open('./py_filter', 'wb') as fd:
            fd.write(urlopen(url).read())
        os.system('chmod +x py_filter')
    os.system('doxygen Doxyfile > /dev/null')


def deleteFiles():
    os.system('rm -rf Doxyfile xml py_filter')


def parserArgs():
    argParser = argparse.ArgumentParser(description=DESCRIPTION)
    argParser.add_argument('language', help=LANGUAGE_HELP)
    argParser.add_argument('library_name', help=NAME_HELP)
    argParser.add_argument('-v', '--verbose', help=VERBOSE_HELP, action='store_true')
    argParser.add_argument('-e', '--exception', help=EXCEPTION_HELP, action='store_true')
    argParser.add_argument('-g', '--gui', help=GUI_HELP, action='store_true')
    argParser.add_argument('-n', '--noUpload', help=NO_UPLOAD_HELP, action='store_true')
    argParser.add_argument('-k', '--apikey', help=API_KEY_HELP)
    argParser.add_argument('-s', '--secret', help=SCR_KEY_HELP)
    args = argParser.parse_args()

    # args.language = args.language.upper()

    if args.verbose:
        useful.verbose = args.verbose
    if args.gui:
        useful.printVerbose("Launch GUI mode")
    if args.noUpload:
        useful.upload = False
    if args.exception:
        useful.exceptions = True

    if useful.upload and not(args.apikey):
        useful.logError('Error: cannot push symbols without an API key', 1)
    else:
        useful.apikey = args.apikey

    if dicoLang.get(args.language) is None:
        useful.logError('Error: unsupported language \'{}\''.format(args.language), 1)

    useful.printVerbose('Language = ' + args.language)
    useful.printVerbose('Library name = ' + args.library_name + '\n')

    return args


def getFunctionsLang():
    dispatch = {
        'C': parserC.parserC,
        'PYTHON': parserPython.parserPython,
        'JAVA': parserJava.parserJava
    }
    return dispatch


def callOptimizer():
    if useful.upload:
        useful.printVerbose("Calling optimizer")
        aiClient.AIClient.CallOptimizer_ext(useful.apikey)
        useful.printVerbose("Called optimizer")


def main():
    args = parserArgs()
    getDoxyfileAndRun(args.language)

    files = getAllFiles(args.language)
    dispatch = getFunctionsLang()
    for filename in files:
        useful.logInfo('Starting parsing \'' + filename.ogFilename + '\'')
        obj = dispatch[args.language](args.language, args.library_name)
        obj.parseXMLFile(filename.xmlFilename)
    callOptimizer()
    # deleteFiles()


if __name__ == '__main__':
    main()
