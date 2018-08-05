import sys

#pylint: disable=E0611
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()

        x = 0
        y = 0

        self.text = "x: {0}, y: {1}".format(x, y)

        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        self.setMouseTracking(True)
        self.setLayout(grid)
        
        self.setWindowTitle('Event handler')
        self.show()
    
    def keyPressEvent(self, event):
        if  event.key() == Qt.Key_Escape:
            self.close()
    
    def mouseMoveEvent(self, event):
        self.label.setText("x: {0}, y: {1}".format(event.x(), event.y()))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())