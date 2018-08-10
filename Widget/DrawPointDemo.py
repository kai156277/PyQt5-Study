import sys, os, math

#pylint: disable=E0602
sys.path.append(os.getcwd())
from importQt import *

class DrawPointDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 200)
        self.setWindowTitle("draw Point in window")

    def paintEvent(self, event):
        painter = QPainter(self)
        self.drawPoints(painter)
    
    def drawPoints(self, painter):
        painter.setPen(Qt.red)
        size = self.size()

        for i in range(1000):
            x = 100 * ( -1 + 2.0 * i / 1000.0) + size.width() / 2.0
            y = (-50 * math.sin((x - size.width() / 2.0) * math.pi / 50.0)
              + size.height() / 2.0)
            painter.drawPoint(x, y)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DrawPointDemo()
    demo.show()
    sys.exit(app.exec())
