import unittest
from unittest.mock import patch
import sys
import io

import Parser.printingFunctions as printingFunctions
import classes as classes


class Test_PrintingFunctions(unittest.TestCase):
    def test_printVariables(self):
        '''
        it should print the variables
        '''
        capturedOutput = io.StringIO()  # setup an io
        sys.stdout = capturedOutput  # redirect stdout

        tmp = classes.variableClass()
        tmp.name = 'name'
        tmp.type = 'type'
        tmp.value = 'value'
        tmp.desc = 'desc'
        variables = [tmp]

        printingFunctions.printVariables(variables)
        sys.stdout = sys.__stdout__  # reset stdout
        self.assertEqual(capturedOutput.getvalue(), '\033[1mVariables:\033[0m\n\n'
                                                    'name = name\n'
                                                    'type = type\n'
                                                    'value = value\n'
                                                    'description = desc\n\n\n')

    def test_printDefines(self):
        '''
        it should print the defines
        '''
        capturedOutput = io.StringIO()  # setup an io
        sys.stdout = capturedOutput  # redirect stdout

        tmpVar = classes.variableClass()
        tmpVar.name = 'name'
        tmpVar.desc = 'desc'
        tmpDef = classes.defineClass()
        tmpDef.name = 'name'
        tmpDef.include = 'import'
        tmpDef.initializer = 'init'
        tmpDef.params = [tmpVar]
        tmpDef.briefDesc = 'desc brief'
        tmpDef.detailedDesc = 'desc detail'
        defines = [tmpDef]

        printingFunctions.printDefines(defines)
        sys.stdout = sys.__stdout__  # reset stdout
        self.assertEqual(capturedOutput.getvalue(), '\033[1mMacros:\033[0m\n\n'
                                                    'name = name\n'
                                                    'import = import\n'
                                                    'initializer = init\n'
                                                    'brief desc = desc brief\n'
                                                    'detailed desc = desc detail\n'
                                                    '\t- name ( desc )\n\n')

    def test_printStructures(self):
        '''
        it should print the structures
        '''
        capturedOutput = io.StringIO()  # setup an io
        sys.stdout = capturedOutput  # redirect stdout

        tmpVar = classes.variableClass()
        tmpVar.name = 'name'
        tmpVar.desc = 'desc'
        tmpVar.type = 'type'
        tmpStruct = classes.structClass()
        tmpStruct.name = 'name'
        tmpStruct.include = 'import'
        tmpStruct.members = [tmpVar]
        tmpStruct.briefDesc = 'desc brief'
        tmpStruct.detailedDesc = 'desc detail'
        structures = [tmpStruct]

        printingFunctions.printStructures(structures)
        sys.stdout = sys.__stdout__  # reset stdout
        self.assertEqual(capturedOutput.getvalue(), '\033[1mStructures:\033[0m\n\n'
                                                    'name = name\n'
                                                    'import = import\n'
                                                    'brief desc = desc brief\n'
                                                    'detailed desc = desc detail\n'
                                                    '\t- type name ( desc )\n\n\n')

    def test_printUnions(self):
        '''
        it should print the unions
        '''
        capturedOutput = io.StringIO()  # setup an io
        sys.stdout = capturedOutput  # redirect stdout

        tmpVar = classes.variableClass()
        tmpVar.name = 'name'
        tmpVar.desc = 'desc'
        tmpVar.type = 'type'
        tmpUnion = classes.unionClass()
        tmpUnion.name = 'name'
        tmpUnion.include = 'import'
        tmpUnion.members = [tmpVar]
        tmpUnion.briefDesc = 'desc brief'
        tmpUnion.detailedDesc = 'desc detail'
        unions = [tmpUnion]

        printingFunctions.printUnions(unions)
        sys.stdout = sys.__stdout__  # reset stdout
        self.assertEqual(capturedOutput.getvalue(), '\033[1mUnions:\033[0m\n\n'
                                                    'name = name\n'
                                                    'import = import\n'
                                                    'brief desc = desc brief\n'
                                                    'detailed desc = desc detail\n'
                                                    '\t- type name ( desc )\n\n')

    def test_printTypedefs(self):
        '''
        it should print the typedefs
        '''
        capturedOutput = io.StringIO()  # setup an io
        sys.stdout = capturedOutput  # redirect stdout

        tmpTypedef = classes.typedefClass()
        tmpTypedef.tdName = 'name'
        tmpTypedef.tdType = 'type'
        tmpTypedef.include = 'import'
        tmpTypedef.briefDesc = 'desc brief'
        tmpTypedef.detailedDesc = 'desc detail'
        typedefs = [tmpTypedef]

        printingFunctions.printTypedefs(typedefs)
        sys.stdout = sys.__stdout__  # reset stdout
        self.assertEqual(capturedOutput.getvalue(), '\033[1mTypedefs:\033[0m\n\n'
                                                    'type = type\n'
                                                    'name = name\n'
                                                    'import = import\n'
                                                    'brief desc = desc brief\n'
                                                    'detailed desc = desc detail\n\n')

    def test_printFunctions(self):
        '''
        it should print the functions
        '''
        capturedOutput = io.StringIO()  # setup an io
        sys.stdout = capturedOutput  # redirect stdout

        tmpVar = classes.variableClass()
        tmpVar.name = 'name'
        tmpVar.desc = 'desc'
        tmpVar.type = 'type'
        tmpFunction = classes.functionClass()
        tmpFunction.name = 'name'
        tmpFunction.include = 'import'
        tmpFunction.briefDesc = 'desc brief'
        tmpFunction.detailedDesc = 'desc detail'
        tmpFunction.params = [tmpVar]
        tmpFunction.returnType = 'type'
        tmpFunction.returnDesc = 'desc'
        tmpVar.value = 'val'
        tmpVar.desc = 'desc'
        tmpFunction.returnValues = [tmpVar]
        functions = [tmpFunction]

        printingFunctions.printFunctions(functions)
        sys.stdout = sys.__stdout__  # reset stdout
        self.assertEqual(capturedOutput.getvalue(), '\033[1mFunctions:\033[0m\n\n'
                                                    'name = name\n'
                                                    'import = import\n'
                                                    'brief desc = desc brief\n'
                                                    'detailed desc = desc detail\n'
                                                    'parameters :\n'
                                                    '\t- type name ( desc )\n'
                                                    'return type = type\n'
                                                    'return = desc\n'
                                                    'return values :\n'
                                                    '\t- val ( desc )\n\n')

    @patch('printingFunctions.printVariables')
    @patch('printingFunctions.printFunctions')
    def test_printClasses(self,
                          mock_printFunctions,
                          mock_printVariables):
        capturedOutput = io.StringIO()  # setup an io
        sys.stdout = capturedOutput  # redirect stdout

        tmpClass = classes.classClass()
        tmpClass.name = 'name'
        tmpClass.include = 'import'
        tmpClass.description = 'description'
        classesTab = [tmpClass]

        printingFunctions.printClasses(classesTab)
        sys.stdout = sys.__stdout__  # reset stdout
        self.assertEqual(capturedOutput.getvalue(), '\033[1mClasses:\033[0m\n\n'
                                                    'name = name\n'
                                                    'import = import\n'
                                                    'description = description\n'
                                                    '\t\033[1mVariables:\033[0m\n\n\n'
                                                    '\t\033[1mFunctions:\033[0m\n\n')
