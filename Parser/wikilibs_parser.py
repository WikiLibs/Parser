#!/usr/bin/env python3.9
import sys
import useful
import PyQt.graphicalClient as gui
import aiClient as aiClient

import Lang_C.parserC as parserC
import Lang_CPP.parserCPP as parserCPP
import Lang_Python.parserPython as parserPython
import Lang_Java.parserJava as parserJava

def getFunctionsLang():
    dispatch = {
        'C': parserC.parserC,
        'CPP': parserCPP.parserCPP,
        'PYTHON3': parserPython.parserPython,
        'JAVA': parserJava.parserJava
    }
    return dispatch


def main():
    args = useful.parserArgs()
    if len(sys.argv) == 1 or useful.graphical is True:
        gui.graphicalClient(args)
        return 0
    useful.getDoxyfileAndRun(args.language)
    client = aiClient.AIClient(useful.apikey, aiClient.APP_ID, aiClient.SEC)
    if useful.upload is True:
        client.GetToken()
        client.CreateLibUUID(args.language, args.library_name)
    dispatch = getFunctionsLang()
    obj = dispatch[args.language](args.language, args.library_name)
    files = obj.getAllParseableFiles()
    for filename in files:
        useful.logInfo('Starting parsing \'' + filename.ogFilename + '\'')
        obj.parseXMLFile(filename.xmlFilename, client)
    useful.deleteFiles()


if __name__ == '__main__':
    main()
