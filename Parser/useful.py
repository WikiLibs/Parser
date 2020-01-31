import sys

import xml.etree.ElementTree as ET
from urllib.request import urlopen
import os
import argparse
import aiClient

verbose = False
upload = True
exceptions = False
graphical = False
apikey = ""
secret = ""

GREEN = "\033[0;32m"
YELLOW = "\u001b[33m"
RED = "\u001b[31m"
BOLD = "\u001b[1m"
RESET = "\u001b[0m"


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
    "CPP": ['.hh', '.cc', '.hxx', '.cxx', '.h', '.hpp', '.cpp'],
    "PYTHON3": ['.py'],
    "JAVA": ['.java']
}

dicoLangDoxy = {
    "C": "C",
    "CPP": "CPP",
    "PYTHON3": "PYTHON",
    "JAVA": "JAVA"
}

class filesClass:
    ogFilename = ""
    xmlFilename = ""


def printVerbose(message):
    global verbose
    if verbose:
        print(message)


def printExceptionVerbose(error):
    global verbose
    if verbose and exceptions:
        print("Exception:", error)


def logInfo(msg, context=None, line=None):
    if context and line:
        print(GREEN + BOLD + "[INFO]" + RESET + " - " + msg + " (" + context + ": " + str(line) + ")")
    else:
        print(GREEN + BOLD + "[INFO]" + RESET + " - " + msg)


def logWarning(msg, context=None, line=None):
    if context and line:
        print(YELLOW + BOLD + "[WARNING]" + RESET + " - " + msg + " (" + context + ": " + str(line) + ")")
    else:
        print(YELLOW + BOLD + "[WARNING]" + RESET + " - " + msg)


def logError(msg, errorCode, context=None, line=None):
    if context and line:
        print(RED + BOLD + "[ERROR]" + RESET + " - " + msg + " (" + context + ": " + str(line) + ")")
    else:
        print(RED + BOLD + "[ERROR]" + RESET + " - " + msg)
    print(BOLD + "[---Exiting program---]" + RESET)
    sys.exit(errorCode)


def getAllFiles(language):
    global dicoLang
    global verbose
    files = []
    root = ET.parse("./xml/index.xml").getroot()
    extentions = dicoLang.get(language)

    printVerbose("These files will be parsed:")
    for child in root:
        if child.get('kind') == 'file':
            filename = child.find('name').text
            for extension in extentions:
                if filename.endswith(extension):
                    tmp = filesClass()
                    tmp.ogFilename = filename
                    tmp.xmlFilename = "./xml/" + child.get('refid') + ".xml"
                    files.append(tmp)
                    printVerbose("\t- " + filename)
    printVerbose("")
    return files


def getDoxyfileAndRun(language):
    url = 'https://wikilibs-parser.azurewebsites.net/doxyfiles/' + dicoLangDoxy[language] + '/Doxyfile'
    if language == "PYTHON3" and os.name == 'nt':
        url += 'Windows'
    with open('./Doxyfile', 'wb') as fd:
        fd.write(urlopen(url).read())

    if language == 'PYTHON3':
        fileName = 'py_filter'
        if os.name == 'nt':
            fileName += 'Windows'
        url = 'https://wikilibs-parser.azurewebsites.net/doxyfiles/' + dicoLangDoxy[language] + '/' + fileName

        if os.name != 'nt':
            with open('./py_filter', 'wb') as fd:
                fd.write(urlopen(url).read())
            os.system('chmod +x py_filter')
        else:
            with open('./py_filter.bat', 'wb') as fd:
                fd.write(urlopen(url).read())

    if os.name == 'nt':
        os.system('doxygen Doxyfile')
    else:
        os.system('doxygen Doxyfile > /dev/null')


def deleteFiles():
    if os.name == 'nt':
        os.system('del /f Doxyfile py_filter.bat')
        os.system('RD /S /Q xml')
    else:
        os.system('rm -rf Doxyfile xml py_filter')


def parserArgs():
    global upload
    global verbose
    global exceptions
    global graphical
    global secret
    global apikey

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

    args.language = args.language.upper()

    if args.verbose:
        verbose = args.verbose
    if args.gui:
        graphical = True
    if args.noUpload:
        upload = False
    if args.exception:
        exceptions = True

    if upload and not(args.apikey):
        logError('Error: cannot push symbols without an API key', 1)
    else:
        apikey = args.apikey

    if dicoLang.get(args.language) is None:
        logError('Error: unsupported language \'{}\''.format(args.language), 1)

    printVerbose('Language = ' + args.language)
    printVerbose('Library name = ' + args.library_name + '\n')

    return args


def callOptimizer():
    global upload
    if upload:
        printVerbose("Calling optimizer")
        aiClient.AIClient.CallOptimizer_ext(apikey)
        printVerbose("Called optimizer")