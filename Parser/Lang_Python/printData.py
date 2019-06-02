def printVariables(variables):
    print("\033[1mVariables:\033[0m\n")

    for elem in variables:
        print("name =", elem.name)
        print("type =", elem.type)
        print("value =", elem.value)
        print("description =", elem.desc)
        print()
    print()


def printFunctions(functions):
    print("\033[1mFunctions:\033[0m\n")

    for elem in functions:
        print("name =", elem.name)
        print("briefDesc =", elem.briefDesc)
        print("detailedDesc =", elem.detailedDesc)
        printVariables(elem.params)
        print("returnType =", elem.returnType)
        print("returnDesc =", elem.returnDesc)
        print("returnValues =", elem.returnValues)
        print()
    print()
