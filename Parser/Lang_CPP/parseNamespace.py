from Lang_CPP.parseFile import parseFile
from Lang_CPP.parseVariable import parseVariable
from Lang_CPP.parseFunction import parseFunction
from Lang_CPP.parseTypedef import parseTypedef

#Python wants code duplication at all costs then it gets it
kindTable = {
    "file": parseFile,
    "variable": parseVariable,
    "function": parseFunction,
    "typedef": parseTypedef
}

def parseNamespace(root):
    syms = []
    cpdef = root.find("compounddef")
    name = cpdef.find("compoundname").text
    path = name.replace("::", "/")
    for elem in root.iter('memberdef'):
        kind = elem.get('kind')
        pp3b = path + "/" + elem.find("name").text
        syms1 = []
        if (kind in kindTable):
            syms1 = kindTable[kind](elem)
        for s in syms1:
            s.path = pp3b
            syms.append(s)
    return (syms)
        
