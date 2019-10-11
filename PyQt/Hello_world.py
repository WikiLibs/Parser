import sys
import time
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QLineEdit, QComboBox
from PyQt5.QtCore import QSize

WIDTH = 640
HEIGHT = 480

def say_hello():
    print("Button clicked, Hello!")

class WelcomeWindow(QMainWindow):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QMainWindow.__init__(self)

        # self.setMinimumSize(QSize(WIDTH, HEIGHT))
        self.setWindowTitle("Wikilibs - Parser Client")

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        # Create Layout grid
        gridLayout = QGridLayout(self)
        centralWidget.setLayout(gridLayout)

        button = QPushButton("Next")
        button.clicked.connect(self.switch)

        title = QLabel("Welcome to Wikilibs' parser GUI interface", self)
        title.setAlignment(QtCore.Qt.AlignHCenter)

        # Add widgets to Layout Grid
        gridLayout.addWidget(title, 0, 0)
        gridLayout.addWidget(button, 1, 0)

    def switch(self):
        self.switch_window.emit()


class InputInfoWindow(QWidget):
    switch_window = QtCore.pyqtSignal(str, str)

    def __init__(self):
        QMainWindow.__init__(self)

        # self.setMinimumSize(QSize(WIDTH, HEIGHT))
        self.setWindowTitle("Wikilibs - Parser Client!!")

        # Create Layout grid
        gridLayout = QGridLayout(self)

        button = QPushButton("Next")
        button.clicked.connect(self.switch)

        label1 = QLabel("Library language")
        self.line_edit = QLineEdit()
        label2 = QLabel("Library name")
        self.combo_box = QComboBox()
        self.combo_box.addItems(["C", "PYTHON"])

        title = QLabel("Please input the following information", self)
        title.setAlignment(QtCore.Qt.AlignHCenter)

        # Add widgets to Layout Grid
        gridLayout.addWidget(title, 0, 0)
        gridLayout.addWidget(label1, 1, 0)
        gridLayout.addWidget(self.line_edit, 1, 1)
        gridLayout.addWidget(label2, 2, 0)
        gridLayout.addWidget(self.combo_box, 2, 1)
        gridLayout.addWidget(button, 3, 3)

    def switch(self):
        self.switch_window.emit(self.line_edit.text(), self.combo_box.currentText())


class SummaryWindow(QWidget):
    switch_window = QtCore.pyqtSignal(str, str)

    def __init__(self, libname, liblang):
        QMainWindow.__init__(self)

        self.libname = libname
        self.liblang = liblang
        # self.setMinimumSize(QSize(WIDTH, HEIGHT))
        self.setWindowTitle("Wikilibs - Parser Client3")

        # Create Layout grid
        gridLayout = QGridLayout(self)

        button = QPushButton("Start")
        button.clicked.connect(self.switch)

        label1 = QLabel("Library name : {" + self.libname + "}")
        label2 = QLabel("Selected language : {" + self.liblang + "}")

        title = QLabel("Summary", self)
        title.setAlignment(QtCore.Qt.AlignHCenter)

        # Add widgets to Layout Grid
        gridLayout.addWidget(title, 0, 0)
        gridLayout.addWidget(label1, 2, 0)
        gridLayout.addWidget(label2, 1, 0)
        gridLayout.addWidget(button, 3, 0)

    def switch(self):
        self.switch_window.emit(self.libname, self.liblang)

class ProcessingWindow(QWidget):
    switch_window = QtCore.pyqtSignal(str, str)

    def __init__(self, libname, liblang):
        QMainWindow.__init__(self)

        # self.setMinimumSize(QSize(WIDTH, HEIGHT))
        self.setWindowTitle("Wikilibs - Parser Client3")

        # Create Layout grid
        gridLayout = QGridLayout(self)

        label1 = QLabel("Reading all the files ...")

        title = QLabel("Processing, please wait...", self)
        title.setAlignment(QtCore.Qt.AlignHCenter)

        # Add widgets to Layout Grid
        gridLayout.addWidget(title, 0, 0)
        gridLayout.addWidget(label1, 2, 0)

        self.switch_window.emit()


class EndWindow(QWidget):

    def __init__(self, libname, liblang):
        QMainWindow.__init__(self)

        # self.setMinimumSize(QSize(WIDTH, HEIGHT))
        self.setWindowTitle("Wikilibs - Parser Client3")

        # Create Layout grid
        gridLayout = QGridLayout(self)

        button = QPushButton("Start")
        button.clicked.connect(self.close)

        title = QLabel("Upload was successful!", self)
        title.setAlignment(QtCore.Qt.AlignHCenter)

        # Add widgets to Layout Grid
        gridLayout.addWidget(title, 0, 0)
        gridLayout.addWidget(button, 1, 3)


class Controller:
    def __init__(self):
        pass

    def show_WelcomeWindow(self):
        self.welcome = WelcomeWindow()
        self.welcome.switch_window.connect(self.show_InputInfoWindow)
        self.welcome.show()

    def show_InputInfoWindow(self):
        self.input = InputInfoWindow()
        self.input.switch_window.connect(self.show_SummaryWindow)
        self.welcome.close()
        self.input.show()

    def show_SummaryWindow(self, libname, liblang):
        self.summary = SummaryWindow(libname, liblang)
        self.input.switch_window.connect(self.show_ProcessingWindow)
        self.input.close()
        self.summary.show()

    def show_ProcessingWindow(self, libname, liblang):
        self.process = ProcessingWindow(libname, liblang)
        self.summary.switch_window.connect(self.show_EndWindow)
        self.summary.close()
        self.process.show()

    def show_EndWindow(self):
        self.end = EndWindow()
        self.process.close()
        self.end.show()

if __name__ == "__main__":

    # Create Qt application
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_WelcomeWindow()

    sys.exit(app.exec_())
