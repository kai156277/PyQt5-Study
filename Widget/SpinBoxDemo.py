import sys, os

#pylint: disable=E0602
sys.path.append(os.getcwd())
from importQt import *

class SpinBoxDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SpinBox Demo")

        layout = QVBoxLayout()
        self.label = QLabel("current value:")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.spinBox = QSpinBox()
        layout.addWidget(self.spinBox)
        self.spinBox.valueChanged.connect(self.valueChange)
        self.setLayout(layout)

    def valueChange(self):
        self.label.setText("current value: " + str(self.spinBox.value()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = SpinBoxDemo()
    demo.show()
    sys.exit(app.exec())