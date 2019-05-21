import sys

verbose = False
upload = True
exceptions = False

GREEN = "\033[0;32m"
YELLOW = "\u001b[33m"
RED = "\u001b[31m"
BOLD = "\u001b[1m"
RESET = "\u001b[0m"


def printVerbose(message):
    global verbose
    if verbose:
        print(message)


def printExceptionVerbose(error):
    global verbose
    if verbose and exceptions:
        print("Exception:", error)


def logInfo(msg, context=None, line=None):
    if context and line:
        print(GREEN + BOLD + "[INFO]" + RESET + " - " + msg + " (" + context + ": " + str(line) + ")")
    else:
        print(GREEN + BOLD + "[INFO]" + RESET + " - " + msg)


def logWarning(msg, context=None, line=None):
    if context and line:
        print(YELLOW + BOLD + "[WARNING]" + RESET + " - " + msg + " (" + context + ": " + str(line) + ")")
    else:
        print(YELLOW + BOLD + "[WARNING]" + RESET + " - " + msg)


def logError(msg, errorCode, context=None, line=None):
    if context and line:
        print(RED + BOLD + "[ERROR]" + RESET + " - " + msg + " (" + context + ": " + str(line) + ")")
    else:
        print(RED + BOLD + "[ERROR]" + RESET + " - " + msg)
    print(BOLD + "[---Exiting program---]" + RESET)
    sys.exit(errorCode)
