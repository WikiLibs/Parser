import unittest

import sys
import io

import requests
import Parser.useful as useful
from unittest.mock import patch
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QLineEdit, QComboBox, QFileDialog

import Parser.jsonClasses as jsClass
import PyQt.graphicalClient as graphicalClient


class Test_pyqt(unittest.TestCase):
    res = requests
    res.status_code = 600
    res.text = "test"

    res2 = requests
    res2.status_code = 200
    res2.text = "test"

    # def MockPyQtResize(itself, arg1, arg2):
    #     pass

    # def MockPyQtSetWindowTitle(itself, arg1):
    #     pass

    # class MockQtApp:
    #     def __init__(self):
    #         pass

    #     def exec_():
    #         pass

    # class MockArgParser:
    #     def __init__(self):
    #         self.verbose = False
    #         self.gui = True
    #         self.noUpload = True
    #         self.exception = False

    # class MockClassController:
    #     def __init__(self):
    #         pass

    #     def show_WelcomeWindow(self, param_arg):
    #         pass

    #     def show_InputInfoWindow(self, param_arg):
    #         pass

    #     def show_SummaryWindow(self, param_arg, libname, liblang, libpath):
    #         pass

    #     def show_ProcessingWindow(self, param_arg, libname, liblang, libpath):
    #         pass

    #     def show_EndWindow(self):
    #         pass

    # class MockClassQtWin:
    #     def __init__(self):
    #         pass

    #     def connect(self, aclass):
    #         pass

    #     def resize(self, width, height):
    #         pass

    #     def setWindowTitle(self, title):
    #         pass

    #     def setCentralWidget(self, widget):
    #         pass

    # class MockClassWelcomeWindow:
    #     def __init__(self, program_param):
    #         self.switch_window = Test_pyqt.MockClassQtWin()
    #         pass

    #     def switch(self):
    #         pass

    #     def show(self):
    #         pass

    #     def close(self):
    #         pass

    # class MockClassInputInfoWindow:
    #     def __init__(self, program_param):
    #         self.switch_window = Test_pyqt.MockClassQtWin()
    #         pass

    #     def switch(self):
    #         pass

    #     def show(self):
    #         pass

    #     def close(self):
    #         pass

    # class MockClassSummaryWindow:
    #     def __init__(self, program_args, libname, liblang, libpath):
    #         self.switch_window = Test_pyqt.MockClassQtWin()
    #         pass

    #     def switch(self):
    #         pass

    #     def show(self):
    #         pass

    #     def close(self):
    #         pass

    # class MockClassProcessingWindow:
    #     def __init__(self, program_args, libname, liblang, libpath):
    #         self.switch_window = Test_pyqt.MockClassQtWin()
    #         pass

    #     def switch(self):
    #         pass

    #     def show(self):
    #         pass

    #     def close(self):
    #         pass

    # class MockClassEndWindow:
    #     def __init__(self):
    #         self.switch_window = Test_pyqt.MockClassQtWin()
    #         pass

    #     def switch(self):
    #         pass

    #     def show(self):
    #         pass

    #     def close(self):
    #         pass

    # @patch('PyQt5.QtWidgets.QApplication', return_value=MockQtApp)
    # @patch('PyQt.graphicalClient.Controller', MockClassController)
    # def test_graphicalClient(self,
    #                          mock_QWin):
    #     args = self.MockArgParser()
    #     graphicalClient.graphicalClient(args)

    # @patch('PyQt.welcomeWindow.WelcomeWindow', MockClassWelcomeWindow)
    # @patch('PyQt.inputsWindow.InputsWindow', MockClassInputInfoWindow)
    # @patch('PyQt.summaryWindow.SummaryWindow', MockClassSummaryWindow)
    # @patch('PyQt.processingWindow.ProcessingWindow', MockClassProcessingWindow)
    # @patch('PyQt.endWindow.EndWindow', MockClassEndWindow)
    # def test_controller(self):
    #     program_args = self.MockArgParser()
    #     controller = graphicalClient.Controller()
    #     controller.show_WelcomeWindow(program_args)
    #     controller.show_InputInfoWindow(program_args)
    #     controller.show_SummaryWindow(program_args, "libname", "liblang", "libpath")
    #     controller.show_ProcessingWindow(program_args, "libname", "liblang", "libpath")
    #     controller.show_EndWindow()
