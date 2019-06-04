import unittest

import sys
import io

import Parser.Lang_Python.printData as printData
import Parser.classes as classes


class Test_printData(unittest.TestCase):
    def test_printVariables(self):
        '''
        it should not print hello as verbose isn't enabled
        '''
        variables = [classes.variableClass()]
        variables[0].name = 'coolName'
        variables[0].type = 'coolType'
        variables[0].value = 'coolValue'

        capturedOutput = io.StringIO()  # setup an io
        sys.stdout = capturedOutput  # redirect stdout
        printData.printVariables(variables)
        sys.stdout = sys.__stdout__  # reset stdout

        expected = '\033[1mVariables:\033[0m\n\nname = coolName\ntype = coolType\nvalue = coolValue\ndescription = \n\n\n'

        self.assertEqual(capturedOutput.getvalue(), expected, 'Should print the variable')

    def test_printClasses(self):
        '''
        it should not print hello as verbose isn't enabled
        '''
        variables = [classes.variableClass()]
        variables[0].name = 'coolName'
        variables[0].type = 'coolType'
        variables[0].value = 'coolValue'

        classesVar = [classes.classClass()]
        classesVar[0].name = 'coolName'
        classesVar[0].description = 'coolDesc'
        classesVar[0].variables = variables
        classesVar[0].functions = []

        capturedOutput = io.StringIO()  # setup an io
        sys.stdout = capturedOutput  # redirect stdout
        printData.printClasses(classesVar)
        sys.stdout = sys.__stdout__  # reset stdout

        expected = '\033[1mClasses:\033[0m\n\nname = coolName\ndescription = coolDesc\n\t\033[1mVariables:\033[0m\n\nname = coolName\ntype = coolType\nvalue = coolValue\ndescription = \n\n\n'

        self.assertEqual(capturedOutput.getvalue(), expected, 'Should print the variable')

    def test_printFunctions(self):
        functions = [classes.functionClass()]
        functions[0].name = 'pythonFunction'
        variable = classes.variableClass()
        variable.name = "param1"
        variable.type = "param1"
        functions[0].params = [variable]
        functions[0].returnValues = ''

        captureOutput = io.StringIO()
        sys.stdout = captureOutput
        printData.printFunctions(functions)
        sys.stdout = sys.__stdout__

        expected = '\033[1mFunctions:\033[0m\n\nname = pythonFunction\nbriefDesc = \ndetailedDesc = \nreturnType = \nreturnDesc = \nreturnValues = \n\t\033[1mVariables:\033[0m\n\nname = param1\ntype = param1\nvalue = \ndescription = \n\n\n'

        self.assertEqual(captureOutput.getvalue(), expected, 'Should print the variable')
