import sys
# pylint: disable = E0611
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QToolTip, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon, QFont

class HelloWorld(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')
        self.setGeometry(100, 100, 200, 100)
        self.setWindowTitle("PyQt5")
        self.setWindowIcon(QIcon('google.png'))

        label = QLabel('Label', self)
        label.setToolTip('This is a <b>QLabel</b> widget')
        label.setText("Hello World!")
        label.move(50, 20)

        button = QPushButton('&Quit', self) # &Quit 的写法 绑定Alt+Q的快捷键到button上
        button.clicked.connect(self.close)
        button.setToolTip('Quit this App!')
        button.resize(button.sizeHint())
        button.move(50, 50)

        self.show()
    
    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", 
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    hello = HelloWorld()
    sys.exit(app.exec_())