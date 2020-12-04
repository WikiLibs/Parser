class GenericSymbol:
    def __init__(self, typename):
        self.typename = typename
        self.path = "" #Path is always prefixed with langName/libName
        self.importString = ""
        self.prototypes = []
        self.linkedSymbols = []

    def addPrototype(self, proto):
        self.prototypes.append(proto)
        return (self)

    def addMember(self, path):
        self.linkedSymbols.append(path)
        return (self)

class GenericPrototype:
    def __init__(self):
        self.prototype = ""
        self.description = ""
        self.parameters = []
        self.exceptions = []

    def addParameter(self, param):
        self.parameters.append(param)
        return (self)

    def addException(self, ex):
        self.exceptions.append(ex)
        return (self)

class GenericException:
    def __init__(self):
        self.description = ""
        self.linkedSymbol = ""

class GenericParameter:
    def __init__(self):
        self.prototype = ""
        self.description = ""
        self.linkedSymbol = ""


# Start symbol types definitions
def buildPrototype(prototype, description):
    obj = GenericPrototype()
    obj.prototype = prototype
    obj.description = description
    return (obj)

def buildParameter(prototype, description, linkedSymbol=None):
    obj = GenericParameter()
    obj.prototype = prototype
    obj.description = description
    obj.linkedSymbol = linkedSymbol
    return (obj)

def buildSymbol(typename, prototypeObj, path, importString=""):
    sym = GenericSymbol(typename)
    sym.path = path
    sym.importString = importString
    sym.addPrototype(prototypeObj)
    return (sym)

def buildException(linkedSymbol, description=None):
    obj = GenericException()
    obj.description = description
    obj.linkedSymbol = linkedSymbol
    return (obj)

def buildFunction(path, prototypeObj, importString=""):
    return (buildSymbol("function", prototypeObj, path, importString))

def buildVariable(path, prototypeObj, importString=""):
    return (buildSymbol("variable", prototypeObj, path, importString))

def buildDefine(path, prototypeObj, importString=""):
    return (buildSymbol("macro", prototypeObj, path, importString))

def buildClass(path, prototypeObj, importString=""):
    return (buildSymbol("class", prototypeObj, path, importString))

def buildUnion(path, prototypeObj, importString=""):
    return (buildSymbol("union", prototypeObj, path, importString))

def buildTypedef(path, prototypeObj, importString=""):
    return (buildSymbol("typedef", prototypeObj, path, importString))

def buildStruct(path, prototypeObj, importString=""):
    return (buildSymbol("struct", prototypeObj, path, importString))

def buildNamespace(path, prototypeObj, importString=""):
    return (buildSymbol("namespace", prototypeObj, path, importString))
