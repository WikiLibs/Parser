verbose = False
upload = True
exceptions = False


def printVerbose(message):
    global verbose
    if verbose:
        print(message)


def printExceptionVerbose(error):
    global verbose
    if verbose and exceptions:
        print("Exception:", error)
