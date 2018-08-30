import sys

#pylint: disable=E0602
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CheckBoxDemo(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        self.checkBox1 = QCheckBox("CheckBox1")
        self.checkBox1.setChecked(True)
        self.checkBox1.stateChanged.connect(lambda : self.btnState(self.checkBox1))
        layout.addWidget(self.checkBox1)

        self.checkBox2 = QCheckBox("CheckBox2")
        self.checkBox2.setChecked(False)
        self.checkBox2.stateChanged.connect(lambda : self.btnState(self.checkBox2))
        layout.addWidget(self.checkBox2)
    
        self.checkBox3 = QCheckBox("CheckBox3")
        self.checkBox3.setTristate(True)
        self.checkBox3.setCheckState(Qt.PartiallyChecked)
        self.checkBox3.stateChanged.connect(lambda : self.btnState(self.checkBox3))
        layout.addWidget(self.checkBox3)

        self.setLayout(layout)
        self.setWindowTitle("CheckBox Demo")

    def btnState(self, btn):
        chk1 = self.checkBox1.text() + ", isChecked = " \
             + str(self.checkBox1.isCheckable()) + ", checkState = " \
             + str(self.checkBox1.checkState()) + "\n"

        chk2 = self.checkBox2.text() + ", isChecked = "  \
             + str(self.checkBox2.isCheckable()) + ", checkState = " \
             + str(self.checkBox2.checkState()) + "\n"

        chk3 = self.checkBox3.text() + ", isChecked = " \
             + str(self.checkBox3.isCheckable()) + ", checkState = " \
             + str(self.checkBox3.checkState()) + "\n"

        print(chk1 + chk2 + chk3)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = CheckBoxDemo()
    demo.show()
    sys.exit(app.exec())