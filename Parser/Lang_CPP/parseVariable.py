import Parser.getters as getters
from Parser.genericClasses import buildVariable
from Parser.genericClasses import buildPrototype

def parseVariable(root):
    syms = []
    proto = root.prot
    if (root.get("static") == "yes"):
        proto = proto + " static"
    proto = proto + " " + root.find("type").text + " " + root.find("name").text + root.find("argstring").text
    briefDesc = getters.getBriefDesc(root)
    detailedDesc = getters.getDetailedDesc(root)
    desc = briefDesc
    if (len(detailedDesc) > 0):
        desc = detailedDesc
    syms.append(buildVariable("", buildPrototype(proto, desc)))
    return (syms)
