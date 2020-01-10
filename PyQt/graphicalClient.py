import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QLineEdit, QComboBox

WIDTH = 640
HEIGHT = 480

BUTTON_STYLE = """
    .QPushButton {
        border-radius: 4px;
        color: rgb(255, 255, 255);
        background-color: rgb(123, 104, 238);

        padding: 10px;
    }
"""


def say_hello():
    print("Button clicked, Hello!")


class WelcomeWindow(QMainWindow):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QMainWindow.__init__(self)

        self.resize(WIDTH, HEIGHT)
        self.setWindowTitle("Wikilibs - Parser Client")

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        # Create Layout grid
        gridLayout = QGridLayout(self)
        centralWidget.setLayout(gridLayout)

        button = QPushButton("Next")
        button.clicked.connect(self.switch)

        title = QLabel("Welcome to the Wikilibs parser GUI interface !", self)
        title.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        title.setFont(QtGui.QFont('Assets/Fonts/OpenSans-Bold', 14))

        button.setFixedSize(QtCore.QSize(100, 40))
        button.setStyleSheet(BUTTON_STYLE)
        button.move(270, 270)

        imageWrapper = QLabel()
        image = QtGui.QPixmap('Assets/Images/WikiLibs_Logo')
        imageWrapper.setPixmap(image.scaled(100, 100, QtCore.Qt.KeepAspectRatio))

        # Add widgets to Layout Grid
        gridLayout.addWidget(title, 0, 0)
        gridLayout.addWidget(imageWrapper, 1, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        gridLayout.addWidget(button, 2, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

    def switch(self):
        self.switch_window.emit()


class InputInfoWindow(QWidget):
    switch_window = QtCore.pyqtSignal(str, str)

    def __init__(self):
        QMainWindow.__init__(self)

        self.resize(WIDTH, HEIGHT)
        self.setWindowTitle("Wikilibs - Parser Client")

        # Create Layout grid
        gridLayout = QGridLayout(self)

        button = QPushButton("Next")
        button.clicked.connect(self.switch)
        button.setFixedSize(QtCore.QSize(100, 40))
        button.setStyleSheet(BUTTON_STYLE)

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

        self.resize(WIDTH, HEIGHT)
        self.setWindowTitle("Wikilibs - Parser Client")

        # Create Layout grid
        gridLayout = QGridLayout(self)

        button = QPushButton("Start")
        button.clicked.connect(self.switch)
        button.setFixedSize(QtCore.QSize(100, 40))
        button.setStyleSheet(BUTTON_STYLE)

        label1 = QLabel("Library name: " + self.libname)
        label2 = QLabel("Selected language: " + self.liblang)

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
    switch_window = QtCore.pyqtSignal(QLabel)

    def __init__(self, libname, liblang):
        QMainWindow.__init__(self)

        self.resize(WIDTH, HEIGHT)
        self.setWindowTitle("Wikilibs - Parser Client")

        # Create Layout grid
        gridLayout = QGridLayout(self)

        button = QPushButton("Click to continue")
        button.clicked.connect(self.switch)
        button.setFixedSize(QtCore.QSize(150, 40))
        button.setStyleSheet(BUTTON_STYLE)

        label1 = QLabel("Reading all the files...")

        self.title = QLabel("Processing, please wait...", self)
        self.title.setAlignment(QtCore.Qt.AlignHCenter)

        # Add widgets to Layout Grid
        gridLayout.addWidget(self.title, 0, 0)
        gridLayout.addWidget(label1, 2, 0)
        gridLayout.addWidget(button, 3, 0)

    def switch(self):
        self.switch_window.emit(self.title)


class EndWindow(QWidget):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QMainWindow.__init__(self)

        self.resize(WIDTH, HEIGHT)
        self.setWindowTitle("Wikilibs - Parser Client")

        # Create Layout grid
        gridLayout = QGridLayout(self)

        button = QPushButton("Close")
        button.clicked.connect(self.close)
        button.setFixedSize(QtCore.QSize(100, 40))
        button.setStyleSheet(BUTTON_STYLE)

        title = QLabel("Upload was successful!", self)
        title.setAlignment(QtCore.Qt.AlignHCenter)

        # Add widgets to Layout Grid
        gridLayout.addWidget(title, 0, 0)
        gridLayout.addWidget(button, 1, 3)

    def switch(self):
        self.switch_window.emit()


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
        self.summary.switch_window.connect(self.show_ProcessingWindow)
        self.input.close()
        self.summary.show()

    def show_ProcessingWindow(self, libname, liblang):
        self.process = ProcessingWindow(libname, liblang)
        self.process.switch_window.connect(self.show_EndWindow)
        self.summary.close()
        self.process.show()

    def show_EndWindow(self):
        self.end = EndWindow()
        self.process.close()
        self.end.show()


def graphicalClient():
    # Create Qt application
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_WelcomeWindow()

    sys.exit(app.exec_())
