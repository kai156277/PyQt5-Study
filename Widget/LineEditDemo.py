import sys

#pylint: disable=E0611
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QFont
from PyQt5.QtCore import Qt

class LineEditDemo(QWidget):
    def __init__(self):
        super().__init__()

        intValidator = QLineEdit()
        doubleValidator = QLineEdit()
        inputMask = QLineEdit()
        text = QLineEdit()
        password = QLineEdit()
        readOnly = QLineEdit("Hello PyQt5")

        intValidator.setValidator(QIntValidator())
        intValidator.setMaxLength(4)
        intValidator.setAlignment(Qt.AlignRight)
        intValidator.setFont(QFont("Arial", 20))

        _double = QDoubleValidator(0.99, 99.99, 2)
        _double.setNotation(QDoubleValidator.StandardNotation)
        doubleValidator.setValidator(_double)
        inputMask.setInputMask('+99_9999_999999')
        text.textChanged.connect(self.textChanged)
        password.setEchoMode(QLineEdit.Password)
        readOnly.setReadOnly(True)

        formLayout = QFormLayout()
        formLayout.addRow("Integer Validator", intValidator)
        formLayout.addRow("Double Validator", doubleValidator)
        formLayout.addRow("Input Mask", inputMask)
        formLayout.addRow("Text Changed", text)
        formLayout.addRow("Password", password)
        formLayout.addRow("ReadOnly", readOnly)

        self.setLayout(formLayout)

    def textChanged(self, text):
        print("Input Text: " + text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = LineEditDemo()
    demo.show()
    sys.exit(app.exec())
