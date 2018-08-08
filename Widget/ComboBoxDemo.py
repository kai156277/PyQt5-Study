import sys

#pylint: disable=E0602
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class ComboBoxDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ComboBox Demo")
        layout = QVBoxLayout()

        self.comboBox = QComboBox()
        self.comboBox.addItem("C")
        self.comboBox.addItems(["C++", "Java", "C#", "Python", "JavaScript"])
        self.comboBox.currentIndexChanged.connect(self.selectionChange)
        layout.addWidget(self.comboBox)

        self.label = QLabel()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def selectionChange(self, index):
        self.label.setText(self.comboBox.currentText())
        print("Items in the list are :")
        for count in range(self.comboBox.count()):
            print('item' + str(count) + "=" + self.comboBox.itemText(count))

        print("Current index", index, "selection change", self.comboBox.currentText())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = ComboBoxDemo()
    demo.show()
    sys.exit(app.exec())

