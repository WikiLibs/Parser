import Parser.getters as getters

def parseClass(root):
    name = root.find("compoundname").text
    path = name.replace("::", "/")
    classProto = cpdef.get("prot") + " "
    cpdef = root.find("compounddef")
    isAbstract = cpdef.get("abstract")
    if (isAbstract == "yes"):
        classProto = classProto + "abstract "
    classProto = classProto + "class " + name
    briefDesc = getters.getBriefDesc(root)
    detailedDesc = getters.getDetailedDesc(root)
    description = briefDesc
    if (len(detailedDesc) > 0):
        description = detailedDesc
    # TODO : INSERT HERE > retrieve parameters from template parameter list
    #params = getters.getParamDesc(root, )
    # TODO : INSERT HERE > Add parameters to some prototype parameter list
    # TODO : INSERT HERE > Parse class members


    #for elem in root.iter('memberdef'):
    #    kind = elem.get('kind')
    #    print(kind)

    #for elem in root.iter('innerclass'):
    #    refid = elem.get('refid')