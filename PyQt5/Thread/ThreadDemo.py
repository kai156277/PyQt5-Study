# -*- coding: utf-8 -*-
import sys, os, math

#pylint: disable=E0602
sys.path.append(os.getcwd())
from importQt import *

class ThreadDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Thread Demo")
        self.thread = Worker()
        self.listFile =  QListWidget()
        self.btnStart = QPushButton("start")
        self.btnStop = QPushButton("stop")
        layout = QGridLayout(self)
        layout.addWidget(self.listFile, 0, 0, 1, 2)
        layout.addWidget(self.btnStop, 1, 0)
        layout.addWidget(self.btnStart, 1, 1)
        self.btnStart.clicked.connect(self.slotStart)
        self.btnStop.clicked.connect(self.slotStop)
        self.thread.sinOut.connect(self.slotAdd)
        self.btnStop.setEnabled(False)

    def slotAdd(self, file_index):
        self.listFile.addItem(file_index)
        self.listFile.scrollToBottom()

    def slotStart(self):
        self.btnStart.setEnabled(False)
        self.btnStop.setEnabled(True)
        self.thread.startThread()

    def slotStop(self):
        self.btnStart.setEnabled(True)
        self.btnStop.setEnabled(False)
        self.thread.stopThread()


class Worker(QThread):
    sinOut = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.working = True
        self.num = 0

    def __del__(self):
        self.stopThread()

    def startThread(self):
        if self.working == False:
            self.working = True
            self.start()
        else:
            self.start()

    def stopThread(self):
        if self.working == True:
            self.working = False
            self.wait()

    def run(self):
        while self.working == True:
            file_str = "File index {0}".format(self.num)
            self.num += 1
            self.sinOut.emit(file_str)
            self.sleep(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ThreadDemo()
    demo.show()
    sys.exit(app.exec())