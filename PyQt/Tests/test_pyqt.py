import unittest

import sys
import io

import requests
from unittest.mock import patch
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QLineEdit, QComboBox, QFileDialog

import PyQt.graphicalClient as graphicalClient

WIDTH = 640
HEIGHT = 480

class Test_pyqt(unittest.TestCase):
    res = requests
    res.status_code = 600
    res.text = "test"

    res2 = requests
    res2.status_code = 200
    res2.text = "test"

    def MockPyQtResize(itself, arg1, arg2):
        pass

    def MockPyQtSetWindowTitle(itself, arg1):
        pass
