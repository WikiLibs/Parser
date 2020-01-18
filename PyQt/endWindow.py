import graphicalClient as gc

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton


class EndWindow(QWidget):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QMainWindow.__init__(self)

        self.resize(gc.WIDTH, gc.HEIGHT)
        self.setWindowTitle("Wikilibs - Parser Client")

        self.stylesheet = """
            QMainWindow{
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

        button = QPushButton("Close")
        button.clicked.connect(self.close)
        button.setFixedSize(QtCore.QSize(100, 40))

        title = QLabel("Upload was successful!", self)
        title.setAlignment(QtCore.Qt.AlignHCenter)
        title.setFont(QtGui.QFont('Assets/Fonts/OpenSans-Bold', 14))

        # Add widgets to Layout Grid
        self.gridLayout.addWidget(title, 0, 0)
        self.gridLayout.addWidget(button, 1, 3)

    def switch(self):
        self.switch_window.emit()
