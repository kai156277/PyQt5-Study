import sys

#pylint: disable=E0611
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp

class ValidatorDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Validator Demo")

        formlayout = QFormLayout()
        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        regExpLineEdit = QLineEdit()

        formlayout.addRow("Int Validator:", intLineEdit)
        formlayout.addRow("Double Validator:", doubleLineEdit)
        formlayout.addRow("RegExp Validator:", regExpLineEdit)

        intLineEdit.setPlaceholderText("Int Type")
        doubleLineEdit.setPlaceholderText("Double Type")
        regExpLineEdit.setPlaceholderText("Letters and numbers")

        intValidator = QIntValidator(1, 99, self)

        doubleValidator = QDoubleValidator(-360, 360, 2, self)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)

        regExp = QRegExp("[a-zA-Z0-9]+$")
        regExpValidator = QRegExpValidator(regExp, self)

        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        regExpLineEdit.setValidator(regExpValidator)

        self.setLayout(formlayout)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ValidatorDemo()
    demo.show()
    sys.exit(app.exec_())

