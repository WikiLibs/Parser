#!/usr/bin/env python3.6
import useful
#import graphicalClient as gui

import Lang_C_CPP.parserC as parserC
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
    if useful.graphical:
        #gui.graphicalClient(args)
        return 0
    useful.getDoxyfileAndRun(args.language)

    files = useful.getAllFiles(args.language)
    dispatch = getFunctionsLang()
    for filename in files:
        useful.logInfo('Starting parsing \'' + filename.ogFilename + '\'')
        obj = dispatch[args.language](args.language, args.library_name)
        obj.parseXMLFile(filename.xmlFilename)
    useful.callOptimizer()
    useful.deleteFiles()


if __name__ == '__main__':
    main()
