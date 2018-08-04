# -*- coding: utf-8 -*-
import sys

# pylint: disable=E0611
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QMenu
from PyQt5.QtGui import QIcon, QKeySequence

class ExampleMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):

        exitAct = QAction(QIcon("exit.png"), "Exit", self)
        # exitAct.setShortcut(QKeySequence.Quit) # windows not support
        exitAct.setShortcut("Ctrl+Q")
        # exitAct.setShortcut(Qt.CTRL + Qt.Key_Q)
        exitAct.setStatusTip("Exit application")
        exitAct.triggered.connect(self.close)

        emailMenu = QMenu('&Email', self)
        gmailMenu = QAction(QIcon("gmail.png"), '&Gmail', self)
        emailMenu.addAction(gmailMenu)

        viewStatusAct = QAction("View Statusbar", self, checkable=True)
        viewStatusAct.setStatusTip("View Statusbar")
        viewStatusAct.setChecked(True)
        viewStatusAct.triggered.connect(self.toggleMenu)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(viewStatusAct)
        fileMenu.addMenu(emailMenu)
        fileMenu.addAction(exitAct)

        self.statusBar().showMessage("Ready")

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Example Main Window')
        self.show()

    def toggleMenu(self, state):

        if state:
            self.statusBar().show()
        else:
            self.statusBar().hide()
    
    def contextMenuEvent(self, event):

        menu = QMenu(self)

        newAct = menu.addAction("&New")
        openAct = menu.addAction("&Open")
        quitAct = menu.addAction("&Quit")
        action = menu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            self.close()
    
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = ExampleMainWindow()
    sys.exit(app.exec_())