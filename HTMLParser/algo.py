#!/usr/bin/python3.6

import sys
import os

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
    lang = ''
    type = ''
    prototypes = [] # list of SymbolPrototype
    symbols = [] # list of SymbolPath

    def __init__(self, name):
        self.name = name

    def get_JSON(self):
        print(self.name)


S = SymbolUpdate("KEK")
S.print_me()
