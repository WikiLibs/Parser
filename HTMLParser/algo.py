#!/usr/bin/python3.6

import sys
import os
import json

class SymbolPath :
    path = ''

class SymbolParam :
    name = ''
    description = ''
    path = ''

class SymboPrototype :
    prototype = ''
    description = ''
    parameters = [] # list of SymbolParams

class SymbolUpdate :

    def __init__(self, name):
        self.name = name
        self.lang = ''
        self.type = ''
        self.prototypes = [] # list of SymbolPrototype
        self.symbols = [] # list of SymbolPath

    def get_JSON(self):
        jsonData = {
            "lang" : self.lang,
            "type" : self.type,
            "prototypes" : self.prototypes,
            "symbols" : self.symbols
        }


S = SymbolUpdate("KEK")
S.get_JSON()
#S.print_me()
