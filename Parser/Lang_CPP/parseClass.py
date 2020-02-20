import Parser.getters as getters
from Parser.genericClasses import buildPrototype
from Parser.genericClasses import buildParameter
from Parser.genericClasses import buildClass
from classes import variableClass
from Parser.Lang_CPP.parserCPP import kindTable

def parseClass(root):
    #Obtain generic information about the class
    name = root.find("compoundname").text
    path = name.replace("::", "/")
    classProto = cpdef.get("prot") + " "
    cpdef = root.find("compounddef")
    importStr = cpdef.find("includes").text
    isAbstract = cpdef.get("abstract")
    if (isAbstract == "yes"):
        classProto = classProto + "abstract "
    classProto = classProto + "class " + name
    briefDesc = getters.getBriefDesc(root)
    detailedDesc = getters.getDetailedDesc(root)
    description = briefDesc
    if (len(detailedDesc) > 0):
        description = detailedDesc
    templatePars = []
    tlist = cpdef.find("templateparamlist")
    for elem in tlist.iter('param'):
        v = variableClass()
        v.type = elem.get("type")
        v.name = elem.get("declname")
        v.value = elem.get("defval")
        templatePars.append(v)
    if (len(templatePars) > 0):
        prefix = "template <"
        for v in templatePars:
            prefix = prefix + v.type + " " + v.name
            if (tdef != None):
                prefix = prefix + " = " + v.value
            prefix = prefix + ", "
        prefix = prefix[:2]
        classProto = prefix + classProto
        templatePars = getters.getParamDesc(cpdef, templatePars)

    #Build a symbol for the class
    proto = buildPrototype(prototype=classProto, description=description)
    for v in templatePars:
        proto.addParameter(buildParameter(prototype=v.type + " " + v.name, description=v.desc))
    cl = buildClass(path=path, prototypeObj=proto, importString=importStr)
    for elem in root.iter('memberdef'):
        kind = elem.get('kind')
        path = path + "/" + elem.find("name").text
        cl.addMember(path)
        syms = []
        if (kind in kindTable):
            syms = kindTable[kind](elem)
        for s in syms:
            s.path = path
    for elem in root.iter('innerclass'):
        path = elem.text.replace("::", "/")
        cl.addMember(path)
    syms.append(cl)
    return (syms)