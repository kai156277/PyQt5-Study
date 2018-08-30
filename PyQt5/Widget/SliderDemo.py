import sys, os

#pylint: disable=E0602
sys.path.append(os.getcwd())
from importQt import *

class SliderDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Slider Demo")

        layout = QVBoxLayout()
        self.label = QLabel("Hello PyQt5")
        self.label.setFont(QFont("Arial", 20))
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMaximum(50)
        self.slider.setMinimum(10)
        self.slider.setSingleStep(3)
        self.slider.setValue(20)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(5)
        layout.addWidget(self.slider)
        self.slider.valueChanged.connect(self.valueChange)

        self.setLayout(layout)
    
    def valueChange(self):
        print("Current slider value = %s" % self.slider.value())
        size = self.slider.value()
        self.label.setFont(QFont("Arial", size))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = SliderDemo()
    demo.show()
    sys.exit(app.exec())

