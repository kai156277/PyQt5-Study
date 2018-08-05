import sys

#pylint: disable=E0611
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QPushButton, QMainWindow

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        centerWidget = QWidget()
        grid = QGridLayout()
        grid.setSpacing(10)

        x = 0
        y = 0

        self.text = "x: {0}, y: {1}".format(x, y)
        self.label = QLabel(self.text, self)

        btn1 = QPushButton("Button 1", self)
        btn2 = QPushButton("Button 2", self)
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        grid.addWidget(self.label, 0, 0, Qt.AlignTop)
        grid.addWidget(btn1, 1, 1)
        grid.addWidget(btn2, 2, 2)

        self.setMouseTracking(True)
        centerWidget.setMouseTracking(True)
        
        centerWidget.setLayout(grid)
        self.setCentralWidget(centerWidget)
        self.setWindowTitle('Event handler')
        self.show()
    
    def keyPressEvent(self, event):
        if  event.key() == Qt.Key_Escape:
            self.close()
    
    def mouseMoveEvent(self, event):
        self.label.setText("x: {0}, y: {1}".format(event.x(), event.y()))
        self.statusBar().showMessage("x: {0}, y: {1}".format(event.x(), event.y()))

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())