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
            print("\t-", param)
        print()

def printFunctions(functions):
    print("\033[1mFunctions:\033[0m\n")

    for elem in functions:
        print("name =", elem.name)
        print("return type =", elem.returnType)
        print("brief desc =", elem.briefDesc)
        print("detailed desc =", elem.detailedDesc)
        for param in elem.params:
            print("\t-", param.type, param.name)
        print()