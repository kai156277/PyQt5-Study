import sys
# pylint: disable = E0611
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon

class HelloWorld(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    
    def initUI(self):
        b = QLabel(self)
        b.setText("Hello World!")
        self.setGeometry(100, 100, 200, 50)
        b.move(50, 20)
        self.setWindowTitle("PyQt5")
        self.setWindowIcon(QIcon('google.png'))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    hello = HelloWorld()
    sys.exit(app.exec_())