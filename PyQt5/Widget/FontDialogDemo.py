# -*- coding: utf-8 -*-
import sys, os

#pylint: disable=E0602
sys.path.append(os.getcwd())
from importQt import *

class FontDialogDemo(QWidget):
	def __init__(self, parent=None):
		super(FontDialogDemo, self).__init__(parent)
		layout = QVBoxLayout()
		self.fontButton  = QPushButton("choose font")
		self.fontButton .clicked.connect(self.getFont)
		layout.addWidget(self.fontButton )
		self.fontLineEdit  = QLabel("Hello,测试字体例子")
		layout.addWidget(self.fontLineEdit )
		self.setLayout(layout)
		self.setWindowTitle("Font Dialog 例子")

	def getFont(self):
		font, ok = QFontDialog.getFont()
		if ok:
			self.fontLineEdit .setFont(font)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = FontDialogDemo()
	demo.show()
	sys.exit(app.exec_())
