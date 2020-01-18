import graphicalClient as gc

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton


class SummaryWindow(QWidget):
    switch_window = QtCore.pyqtSignal(object, str, str, str)

    def __init__(self, param_arg, libname, liblang, libpath):
        QMainWindow.__init__(self)

        self.param_arg = param_arg
        self.libname = libname
        self.liblang = liblang
        self.libpath = libpath

        self.resize(gc.WIDTH, gc.HEIGHT)
        self.setWindowTitle("Wikilibs - Parser Client")

        self.stylesheet = """
            QWidget{
                background-color: #FFFFFF
            }

            QLabel{
                color: #202020;
            }

            QPushButton{
                background-color: #7B68EE;
                color: #FFFFFF;
                border-radius: 4px;
                padding: 10px;
            }
        """
        self.setStyleSheet(self.stylesheet)

        # Create Layout grid
        self.gridLayout = QGridLayout(self)

        button = QPushButton("Start")
        button.clicked.connect(self.switch)
        button.setFixedSize(QtCore.QSize(100, 40))

        label1 = QLabel("Library name: " + self.libname)
        label2 = QLabel("Selected language: " + self.liblang)
        label3 = QLabel("Selected path: " + self.libpath)

        title = QLabel("Summary", self)
        title.setAlignment(QtCore.Qt.AlignHCenter)
        title.setFont(QtGui.QFont('Assets/Fonts/OpenSans-Bold', 14))

        # Add widgets to Layout Grid
        self.gridLayout.addWidget(title, 0, 0)
        self.gridLayout.addWidget(label2, 4, 0)
        self.gridLayout.addWidget(label1, 5, 0)
        self.gridLayout.addWidget(label3, 6, 0)
        self.gridLayout.addWidget(button, 8, 1)

    def switch(self):
        self.switch_window.emit(self.param_arg, self.libname, self.liblang, self.libpath)
