import sys

#pylint: disable=E0611
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton

class TextEditDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Text Edit Demo")
        self.textEdit = QTextEdit()
        self.btn1 = QPushButton("show plain text")
        self.btn2 = QPushButton("show html text")
        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)

        self.setLayout(layout)
        self.btn1.clicked.connect(self.btn1_clicked)
        self.btn2.clicked.connect(self.btn2_clicked)

    def btn1_clicked(self):
        self.textEdit.setPlainText("Hello PyQt5!")

    def btn2_clicked(self):
        self.textEdit.setHtml("<font color = 'red' size = '6'>Hello PyQt5!</font>")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = TextEditDemo()
    demo.show()
    sys.exit(app.exec())
