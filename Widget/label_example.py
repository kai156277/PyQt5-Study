# -*- coding=utf-8 -*-
import sys
import os

# pylint: disable=E0611
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette

class Demo(QWidget):
    def __init__(self):
        super().__init__()

        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        # 1. 初始化标签控件
        label1.setText("This is a text label")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>welcome to use Python GUI Application </a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('This is a photo label')

        dirName, fileName = os.path.split(os.path.abspath(__file__))
        relativePixmap = "../images/python.jpg"
        label3.setPixmap(QPixmap(os.path.join(dirName, relativePixmap)))
        # label3.setPixmap(QPixmap("gmail.png"))

        label4.setText("<a href='http://www.cnblogs.com/wangshuo1/'> welcome to visit xinping`s house </a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('This is a hyperlink label')

        #2 在窗口布局中添加控件
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addStretch()
        vbox.addWidget(label2)
        vbox.addStretch()
        vbox.addWidget(label3)
        vbox.addStretch()
        vbox.addWidget(label4)

        #3 允许label1控件访问超链接
        label1.setOpenExternalLinks(True)
        label1.setTextInteractionFlags(Qt.TextSelectableByMouse)

        label4.setOpenExternalLinks(False)
        label4.linkActivated.connect(self.link_clicked)

        label2.linkHovered.connect(self.link_hovered)

        self.setLayout(vbox)
        self.setWindowTitle("QLabel Demo")

    def link_hovered(self):
        print("when mouse hovered label-2")

    def link_clicked(self):
        print("when mouse clicked label-4")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    d = Demo()
    d.show()
    sys.exit(app.exec())