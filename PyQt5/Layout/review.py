# -*- coding: utf-8 -*-

import sys

# pylint: disable=E0611
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, 
                            QTextEdit, QTextEdit, QGridLayout,
                            QApplication )

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(QLabel('Title'), 1, 0)
        grid.addWidget(QLineEdit(), 1, 1)

        grid.addWidget(QLabel('Author'), 2, 0)
        grid.addWidget(QLineEdit(), 2, 1)

        grid.addWidget(QLabel('Review'), 3, 0)
        grid.addWidget(QTextEdit(), 3, 1)

        self.setWindowTitle('Review')
        self.setLayout(grid)
    
def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()