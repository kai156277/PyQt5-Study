import sys

#pylint disable=E0611
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout

class InputMaskDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Input Mask Demo")

        formlayout = QFormLayout()
        IPLineEdit = QLineEdit()
        MACLineEdit = QLineEdit()
        DateLineEdit = QLineEdit()
        LicenseLineEdit = QLineEdit()

        IPLineEdit.setInputMask("000.000.000.000;_")
        MACLineEdit.setInputMask("HH:HH:HH:HH:HH:HH;_")
        DateLineEdit.setInputMask("0000-00-00")
        LicenseLineEdit.setInputMask(">AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#")

        formlayout.addRow("IP Mask", IPLineEdit)
        formlayout.addRow("Mac Mask", MACLineEdit)
        formlayout.addRow("Date Mask", DateLineEdit)
        formlayout.addRow("License Mask", LicenseLineEdit)

        self.setLayout(formlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = InputMaskDemo()
    demo.show()
    sys.exit(app.exec())
