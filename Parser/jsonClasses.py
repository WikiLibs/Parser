#!/usr/bin/python3.6
import json


class SymbolPath:
    __path = ''

    def __init__(self, name):
        self.__path = ''

    def setPath(self, path):
        self.__path = path

    def getPath(self):
        return (self.__path)


class SymbolParam:
    __prototype = ''
    __description = ''
    __path = ''

    def __init__(self, name):
        self.__prototype = ''
        self.__description = ''
        self.__path = ''

    def setPrototype(self, prototype):
        self.__prototype = prototype

    def setDescription(self, description):
        self.__description = description

    def setPath(self, path):
        self.__path = path

    def getPath(self):
        return (self.__path)

    def get_JSON(self):
        jsonData = {
            "prototype": self.__prototype,
            "description": self.__description,
            "ref": self.__path
        }
        if jsonData['description'] == '':
            del jsonData['description']
        if jsonData['ref'] == '':
            del jsonData['ref']
        string = json.dumps(jsonData, indent=4)
        return string

class SymbolException:
    __description = ''
    __path = ''

    def __init__(self, name):
        self.__description = ''
        self.__path = ''

    def setDescription(self, description):
        self.__description = description

    def setPath(self, path):
        self.__path = path

    def getPath(self):
        return (self.__path)

    def get_JSON(self):
        jsonData = {
            "description": self.__description,
            "ref": self.__path
        }
        if jsonData['description'] == '':
            del jsonData['description']
        string = json.dumps(jsonData, indent=4)
        return string

class SymbolPrototype:
    __prototype = ''
    __description = ''
    __parameters = []  # list of SymbolParams
    __exceptions = []  # list of SymbolExceptions

    def __init__(self, name):
        self.__prototype = ''
        self.__description = ''
        self.__parameters = []

    def setPrototype(self, prototype):
        self.__prototype = prototype

    def setDescription(self, description):
        self.__description = description

    def appendParameters(self, parameter):
        self.__parameters.append(parameter)

    def appendExceptions(self, exception):
        self.__exceptions.append(exception)

    def get_JSON(self):
        jsonData = {
            "prototype": self.__prototype,
            "description": self.__description,
            "parameters": [json.loads(self.__parameters[i].get_JSON()) for i in range(0, len(self.__parameters))],
            "exceptions": [json.loads(self.__parameters[i].get_JSON()) for i in range(0, len(self.__parameters))]
        }
        if len(jsonData['exceptions']) == 0:
            del jsonData['exceptions']
        if jsonData['description'] == '':
            del jsonData['description']
        string = json.dumps(jsonData, indent=4)
        return string

class SymbolUpdate:
    __name = ''
    __path = ''
    __lang = ''
    __type = ''
    __prototypes = []  # list of SymbolPrototype
    __symbols = []  # list of SymbolPath
    __importString = ""

    def __init__(self, name):
        self.__name = name
        self.__path = ''
        self.__lang = ''
        self.__type = ''
        self.__import = ''
        self.__prototypes = []
        self.__symbols = []

    def setLang(self, lang):
        self.__lang = lang

    def setPath(self, path):
        self.__path = path

    def setType(self, _type):
        self.__type = _type

    def setImport(self, _import):
        self.__import = _import

    def appendPrototypes(self, prototype):
        self.__prototypes.append(prototype)

    def appendSymbols(self, symbol):
        self.__symbols.append(symbol)

    def getPath(self):
        return (self.__path)

    def get_JSON(self):
        jsonData = {
            "lang": self.__lang,
            "path": self.__path,
            "type": self.__type,
            "import": self.__import,
            "prototypes": [json.loads(self.__prototypes[i].get_JSON()) for i in range(0, len(self.__prototypes))],
            "symbols": self.__symbols
        }
        string = json.dumps(jsonData, indent=4)
        return string
