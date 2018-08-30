import sys, os

#pylint: disable=E0602
sys.path.append(os.getcwd())
from importQt import *

class DialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.setWindowTitle("Dialog Demo")

        self.btn = QPushButton(self)
        self.btn.setText("Dialog")
        self.btn.clicked.connect(self.showDialog)
        layout.addWidget(self.btn)

        self.msgBox = QPushButton(self)
        self.msgBox.setText("Message Box")
        self.msgBox.clicked.connect(self.showMessageBox)
        layout.addWidget(self.msgBox)

        self.setLayout(layout)

    def showMessageBox(self):
        reply = QMessageBox.information(self, "Info", "Info Message",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        print(reply)

    def showDialog(self):
        dialog = QDialog()
        btn = QPushButton("ok", dialog)
        dialog.setWindowTitle("Dialog")
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DialogDemo()
    demo.show()
    sys.exit(app.exec())