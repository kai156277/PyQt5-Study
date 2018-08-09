import sys, os

#pylint: disable=E0602
sys.path.append(os.getcwd())
from importQt import *

class DialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dialog Demo")

        self.btn = QPushButton(self)
        self.btn.setText("Dialog")
        self.btn.clicked.connect(self.showDialog)

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