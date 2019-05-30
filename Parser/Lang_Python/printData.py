def printVariables(variables):
    print("\033[1mVariables:\033[0m\n")

    for elem in variables:
        print("name =", elem.name)
        print("type =", elem.type)
        print("value =", elem.value)
        print("description =", elem.desc)
        print()
    print()
