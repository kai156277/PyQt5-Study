import sys
import os

#pylint: disable=E0602
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class PushButtonDemo(QDialog):
    def __init__(self):
        super().__init__()

        vlayout = QVBoxLayout()

        self.btn1 = QPushButton("Button 1")
        self.btn1.setCheckable(True)
        self.btn1.toggle()
        self.btn1.clicked.connect(lambda: self.whichbtn(self.btn1))
        self.btn1.clicked.connect(lambda: self.btnState(self.btn1))
        vlayout.addWidget(self.btn1)

        self.btn2 = QPushButton("image")
        dirName, fileName  = os.path.split(os.path.abspath(__file__))
        relativePixmap = "../images/python.png"
        self.btn2.setIcon(QIcon(QPixmap(os.path.join(dirName, relativePixmap))))
        self.btn2.clicked.connect(lambda: self.whichbtn(self.btn2))
        self.btn2.clicked.connect(lambda: self.btnState(self.btn2))
        vlayout.addWidget(self.btn2)

        self.btn3 = QPushButton("Disabled")
        self.btn3.setEnabled(False)
        vlayout.addWidget(self.btn3)

        self.btn4 = QPushButton("&Download")
        self.btn4.setDefault(True)
        self.btn4.clicked.connect(lambda: self.whichbtn(self.btn4))
        self.btn4.clicked.connect(lambda: self.btnState(self.btn4))
        vlayout.addWidget(self.btn4)

        self.setLayout(vlayout)
        self.setWindowTitle("PushButton Demo")

    def btnState(self, btn):
        if btn.isChecked():
            print("button {0} pressed".format(btn.text()))
        else:
            print("button {0} released".format(btn.text()))

    def whichbtn(self, btn):
        print("cliced button is " + btn.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = PushButtonDemo()
    demo.show()
    sys.exit(app.exec())