import sys

"""@package docstring
Documentation for this module.

More details.
"""

def raiseException1():
    """Documentation for a function.

    @throws Exception
    """
    x = 10
    if x > 5:
        raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

def assertError1():
    """Documentation for a function.

    @throws AssertionError
    """
    assert ('linux' in sys.platform), "This code runs on Linux only."

def tryExcept1():
    """Documentation for a function.

    @throws AssertionError
    """
    try:
        assertError1()
    except AssertionError as error:
        print(error)
        print('The linux_interaction() function was not executed')

def tryExcept2():
    """Documentation for a function.

    @throws FileNotFoundError
    """
    try:
        with open('file.log_non_existant') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)

def tryExcept3():
    """Documentation for a function.

    @throws FileNotFoundError
    @throws AssertionError
    """
    try:
        assertError1()
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except AssertionError as error:
        print(error)
        print('Linux linux_interaction() function was not executed')

def elseClause1():
    """Documentation for a function.

    @throws FileNotFoundError
    @throws AssertionError
    """
    try:
        assertError1()
    except AssertionError as error:
        print(error)
    else:
        print('Executing the else clause.')

def finallyClause1():
    """Documentation for a function.

    @throws FileNotFoundError
    @throws AssertionError
    """
    try:
        assertError1()
    except AssertionError as error:
        print(error)
    else:
        try:
            with open('file.log') as file:
                read_data = file.read()
        except FileNotFoundError as fnf_error:
            print(fnf_error)
    finally:
        print('Cleaning up, irrespective of any exceptions.')

class MyCustomError(Exception):
    """Documentation for a class.

    Herit from Exception
    @throws Exception
    """
    def __init__(self, *args):
        """Documentation for a function.

        Constructor
        """
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        """Documentation for a function.

        @return string that triggers Exception
        """
        print('calling str')
        if self.message:
            return 'MyCustomError, {0} '.format(self.message)
        else:
            return 'MyCustomError has been raised'


# raise MyCustomError
raise MyCustomError('We have a problem')
