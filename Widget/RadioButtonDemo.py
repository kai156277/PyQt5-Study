import sys

#pylint: disable=E0602
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class RadioDemo(QWidget):
    def __init__(self):
        super().__init__()
        hlayout = QHBoxLayout()

        self.btn1 = QRadioButton("Button 1")
        self.btn1.setChecked(True)
        self.btn1.toggled.connect(lambda : self.btnState(self.btn1))
        hlayout.addWidget(self.btn1)

        self.btn2 = QRadioButton("Button 2")
        self.btn2.toggled.connect(lambda : self.btnState(self.btn2))
        hlayout.addWidget(self.btn2)

        self.setLayout(hlayout)
        self.setWindowTitle("RadioButton Demo")
    
    def btnState(self, btn):
        if btn.text() == "Button 1":
            if btn.isChecked():
                print(btn.text() + " is selected")
            else:
                print(btn.text() + " is deselected")
        
        if btn.text() == "Button 2":
            if btn.isChecked():
                print(btn.text() + " is selected")
            else:
                print(btn.text() + " is deselected")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = RadioDemo()
    demo.show()
    sys.exit(app.exec())

