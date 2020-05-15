import getters as getters
from genericClasses import buildVariable
from genericClasses import buildPrototype
from useful import logError

def parseVariable(root):
    syms = []
    proto = root.get("prot")
    if (root.get("static") == "yes"):
        proto = proto + " static"
    t = root.find("type")
    tname = ""
    if (t.find("ref") != None):
        tname = t.find("ref").text
        #TODO: Demangler
    else:
        tname = root.find("type").text
    tt = root.find("argsstring").text
    if (tt == None):
        logError("A terrible error in Python XML has been detected: XML lib returned None when the node exists")
        tt = ""
    proto = proto + " " + tname + " " + root.find("name").text + tt
    briefDesc = getters.getBriefDesc(root)
    detailedDesc = getters.getDetailedDesc(root)
    desc = briefDesc
    if (len(detailedDesc) > 0):
        desc = detailedDesc
    syms.append(buildVariable("", buildPrototype(proto, desc)))
    return (syms)
