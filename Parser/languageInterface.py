import useful


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

    def parseXMLFile(self, filename):
        """
        This function is called by wikilibs_parser.py
        The child of this class will inherit this function
        It should not be overrided
        """
        self.getSymbols(filename)
        if useful.verbose is True:
            self.printParsedData()
        self.uploadToApi()

    def getSymbols(self):
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
        printingFunctions = {
            'variable': printVariables,
            'define': printDefines,
            'struct': printStructures,
            'union': printUnions,
            'function': printFunctions,
            'typedef': printTypedefs,
            'class': printClasses
        }

        for symbol in self.symbols:
            printingFunctions[symbol['symbol_type']](symbol['symbol_list'])

    def uploadToApi(self):
        """
        This function will upload the symbols to the API
        It should not be overrided
        """
        print('TO DO uploadToApi (languageInterface.py)')


def printVariables(variables):
    print("\033[1mVariables:\033[0m\n")

    for elem in variables:
        print("name =", elem.name)
        print("type =", elem.type)
        print("value =", elem.value)
        print("description =", elem.desc)
        print()
    print()


def printDefines(defines):
    print("\033[1mMacros:\033[0m\n")

    for elem in defines:
        print("name =", elem.name)
        print("initializer =", elem.initializer)
        print("brief desc =", elem.briefDesc)
        print("detailed desc =", elem.detailedDesc)
        for param in elem.params:
            print("\t-", param.name, "(", param.desc, ")")
        print()


def printStructures(structures):
    print("\033[1mStructures:\033[0m\n")

    for elem in structures:
        print("name =", elem.name)
        print("brief desc =", elem.briefDesc)
        print("detailed desc =", elem.detailedDesc)
        for memb in elem.members:
            print("\t-", memb.type, memb.name, "(", memb.desc, ")")
        print()
    print()


def printUnions(unions):
    print("\033[1mUnions:\033[0m\n")

    for elem in unions:
        print("name =", elem.name)
        print("brief desc =", elem.briefDesc)
        print("detailed desc =", elem.detailedDesc)
        for memb in elem.members:
            print("\t-", memb.type, memb.name, "(", memb.desc, ")")
        print()


def printTypedefs(typedefs):
    print("\033[1mTypedefs:\033[0m\n")

    for elem in typedefs:
        print("type =", elem.tdType)
        print("name =", elem.tdName)
        print("brief desc =", elem.briefDesc)
        print("detailed desc =", elem.detailedDesc)
        print()


def printFunctions(functions):
    print("\033[1mFunctions:\033[0m\n")

    for elem in functions:
        print("name =", elem.name)
        print("brief desc =", elem.briefDesc)
        print("detailed desc =", elem.detailedDesc)
        print("parameters :")
        for param in elem.params:
            print("\t-", param.type, param.name, "(", param.desc, ")")
        print("return type =", elem.returnType)
        print("return =", elem.returnDesc)
        print("return values :")
        for val in elem.returnValues:
            print("\t-", val.value, "(", val.desc, ")")
        print()


def printClasses(classes):
    print("\033[1mClasses:\033[0m\n")

    for elem in classes:
        print("name =", elem.name)
        print("description =", elem.description)
        print("\t", end="")
        printVariables(elem.variables)
        print("\t", end="")
        printFunctions(elem.functions)
