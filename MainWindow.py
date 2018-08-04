# -*- coding: utf-8 -*-
import sys

# pylint: disable=E0611
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction
from PyQt5.QtGui import QIcon, QKeySequence

class ExampleMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):

        exitAct = QAction(QIcon("exit.png"), "&Exit", self)
        exitAct.setShortcut(QKeySequence.Quit)
        # exitAct.setShortcut("Ctrl+Q")
        # exitAct.setShortcut(Qt.CTRL + Qt.Key_Q)
        exitAct.setStatusTip("Exit application")
        exitAct.triggered.connect(self.close)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(exitAct)

        self.statusBar().showMessage("Ready")

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Simple menu')
        self.show()
    
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = ExampleMainWindow()
    sys.exit(app.exec_())