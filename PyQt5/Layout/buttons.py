# -*- coding: utf-8 -*-
import sys
# pylint: disable=E0611
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QLabel

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        okBtn = QPushButton("Ok")
        cancelBtn = QPushButton("Cancel")
        textLabel = QLabel("Box Layout")

        hBoxLayout = QHBoxLayout()
        hBoxLayout.addStretch()
        hBoxLayout.addWidget(okBtn)
        hBoxLayout.addWidget(cancelBtn)

        vBoxLayout = QVBoxLayout()
        vBoxLayout.addWidget(textLabel)
        vBoxLayout.addLayout(hBoxLayout)

        self.setLayout(vBoxLayout)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle("Box Layout")


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = Example()
   ex.show()
   sys.exit(app.exec_())