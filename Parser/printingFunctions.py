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
        print("import =", elem.include)
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
        print("import =", elem.include)
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
        print("import =", elem.include)
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
        print("import =", elem.include)
        print("brief desc =", elem.briefDesc)
        print("detailed desc =", elem.detailedDesc)
        print()


def printFunctions(functions):
    print("\033[1mFunctions:\033[0m\n")

    for elem in functions:
        print("name =", elem.name)
        print("import =", elem.include)
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
        print("import =", elem.include)
        print("description =", elem.description)
        print("\t", end="")
        printVariables(elem.variables)
        print("\t", end="")
        printFunctions(elem.functions)


def printGeneric(syms):
    print("\033[1mGeneric:\033[0m\n")

    for elem in syms:
        print("name =", elem.typename)
        print("path =", elem.path)
        print("import =", elem.importString)
        for proto in elem.prototypes:
            print("\tprototype=", proto.prototype)
            print("\tdescription=", proto.description)
            for param in proto.parameters:
                print("\t\tparameters=", param.prototype)
                print("\t\tdescription=", param.description)
                print("\t\tlinkedSym=", param.linkedSymbol)
            for ex in proto.exceptions:
                print("\t\texception:")
                print("\t\t\tdescription=", ex.description)
                print("\t\t\tlinkedSym=", ex.linkedSymbol)
        for sym in elem.linkedSymbols:
            print("\tlinkedSymbol=", sym)
        print("")
