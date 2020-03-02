import getters as getters
from genericClasses import buildPrototype
from genericClasses import buildParameter
from genericClasses import buildClass
from classes import variableClass
from Lang_CPP.parseFile import parseFile
from Lang_CPP.parseVariable import parseVariable
from Lang_CPP.parseFunction import parseFunction

#Python wants code duplication at all costs then it gets it
kindTable = {
    "file": parseFile,
    "variable": parseVariable,
    "function": parseFunction
}

def parseClass(root):
    #Obtain generic information about the class
    cpdef = root.find("compounddef")
    name = cpdef.find("compoundname").text
    path = name.replace("::", "/")
    classProto = cpdef.get("prot") + " "
    importStr = cpdef.find("location").get("file")
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
    if (tlist != None):
        for elem in tlist.iter('param'):
            v = variableClass()
            v.type = elem.find("type")
            if (elem.find("declname") == None): #Found bug in Doxygen
                print("A terrible error has occured in Doxygen: template is corrupted, attempting restore...")
                txt = v.type.text
                vals = txt.split(" ")
                if (len(vals) < 2):
                    print("Unable to restore corrupted template!")
                    continue
                v.type = vals[0]
                v.name = vals[1]
                print("Successfully restored corrupted template!")
            else:
                if (v.type.find("ref") != None):
                    v.ref = v.type.find("ref").get("refid")
                    v.type = v.type.find("ref").text
                else:
                    v.type = v.type.text
                v.name = elem.find("declname").text
                if (elem.find("defval") != None):
                    v.value = elem.find("defval").text
            templatePars.append(v)
    if (len(templatePars) > 0):
        prefix = "template <"
        for v in templatePars:
            prefix = prefix + v.type + " " + v.name
            if (v.value != None):
                prefix = prefix + " = " + v.value
            prefix = prefix + ", "
        prefix = prefix[:2]
        prefix = prefix + ">"
        classProto = prefix + classProto
        templatePars = getters.getParamDesc(cpdef, templatePars)

    #Build a symbol for the class
    proto = buildPrototype(prototype=classProto, description=description)
    for v in templatePars:
        proto.addParameter(buildParameter(prototype=v.type + " " + v.name, description=v.desc))
    cl = buildClass(path=path, prototypeObj=proto, importString=importStr)
    syms = []
    for elem in root.iter('memberdef'):
        kind = elem.get('kind')
        path = path + "/" + elem.find("name").text
        cl.addMember(path)
        syms1 = []
        if (kind in kindTable):
            syms1 = kindTable[kind](elem)
        for s in syms1:
            s.path = path
            syms.append(s)
    for elem in root.iter('innerclass'):
        path = elem.text.replace("::", "/")
        cl.addMember(path)
    syms.append(cl)
    return (syms)