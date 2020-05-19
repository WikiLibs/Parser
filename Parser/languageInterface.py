import useful
import aiClient
from aiClient import AIClient
from jsonRequestCrafter import JSONRequestCrafter
import printingFunctions as printingFunctions


# This class should be the parent of any new language
# wikilibs_parser.py will call parseXMLFile from the child
# The logic should not be modified
# getSymbols() must be implemented by the child class
# Other functions can be modified here, but not overrided by the child
class LanguageInterface:
    def __init__(self, language, library_name):
        self.symbols = []
        self.language = language
        self.lib_name = library_name

    def parseXMLFile(self, filename, apikey):
        """
        This function is called by wikilibs_parser.py
        The child of this class will inherit this function
        It should not be overrided
        """
        self.apikey = apikey
        self.getSymbols(filename)
        if useful.verbose is True:
            self.printParsedData()
        self.uploadToApi()
        self.symbols = []

    def getAllParseableFiles(self):
        """
        This function is called by wikilibs_parser.py
        The child of this class will inherit this function
        It may be overrided by child class if necessary
        """
        return (useful.getAllFiles(self.language))

    def getSymbols(self, filename):
        """
        This function is the only one that should be overrided by the child
        It raises an exception if not overrided
        """
        raise Exception('Not implemented')

    def appendToSymbols(self, symbol_type, symbol):
        """
        This function will append any new symbol to the symbol list based on symbol_type
        It should not be overrided
        """
        for symbol_elem in self.symbols:
            if symbol_elem['symbol_type'] == symbol_type:
                symbol_elem['symbol_list'].append(symbol)
                return

        new_symbol_type = {
            'symbol_type': symbol_type,
            'symbol_list': [symbol]
        }
        self.symbols.append(new_symbol_type)

    def printParsedData(self):
        """
        This function will print out every found symbol
        It should not be overrided
        """
        printingFunctionsDict = {
            'variable': printingFunctions.printVariables,
            'define': printingFunctions.printDefines,
            'struct': printingFunctions.printStructures,
            'union': printingFunctions.printUnions,
            'function': printingFunctions.printFunctions,
            'typedef': printingFunctions.printTypedefs,
            'class': printingFunctions.printClasses
        }

        for symbol in self.symbols:
            if (symbol['symbol_type'] in printingFunctionsDict):
                printingFunctionsDict[symbol['symbol_type']](symbol['symbol_list'])

    def uploadToApi(self):
        """
        This function will upload the symbols to the API
        It should not be overrided
        """
        symbolsToUpload = []
        client = AIClient(self.apikey, aiClient.APP_ID, aiClient.SEC)
        symbolsToUpload.append(('client', client))
        for symbol in self.symbols:
            symbolsToUpload.append((symbol['symbol_type'], symbol['symbol_list']))
        if useful.upload:
            JSONRequestCrafter(self.language, self.lib_name, symbolsToUpload)
