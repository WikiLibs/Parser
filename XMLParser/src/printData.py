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

def printTypedefs(typedefs):
    print("\033[1mTypedefs:\033[0m\n")

    for elem in typedefs:
        print("type =", elem.tdType)
        print("name =", elem.tdName)
        print("brief desc =", elem.briefDesc)
        print("detailed desc =", elem.detailedDesc)
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