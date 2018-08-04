import sys
# pylint: disable = E0611
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QToolTip
from PyQt5.QtGui import QIcon, QFont

class HelloWorld(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        b = QLabel('Label', self)
        b.setToolTip('This is a <b>QLabel</b> widget')
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