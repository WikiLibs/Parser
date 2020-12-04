import getters as getters
from genericClasses import buildPrototype
from genericClasses import buildTypedef

def parseTypedef(root):
    syms = []
    proto = root.get("prot") + " "
    proto = proto + root.find("definition").text
    syms.append(buildTypedef(path="", prototypeObj=buildPrototype(prototype=proto, description=getters.getDetailedDesc(root))))
    return (syms)
