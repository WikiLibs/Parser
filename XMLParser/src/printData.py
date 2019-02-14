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
