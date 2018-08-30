#!/usr/bin/python3
# -*- coding: utf-8 -*-

#pylint: disable=E0611
from PyQt5.QtWidgets import QApplication, QTextEdit, QMainWindow, QFileDialog, QTabWidget, QLineEdit, QFontDialog
from PyQt5.QtCore import QDir, QFile, QTextStream, QSettings
from PyQt5.QtGui import QFont
from UI_readWriteFile import Ui_MainWindow
import sys, os
from optparse import OptionParser

quiet = False
def stdout(msg):
    global quiet
    if not quiet:
        print(msg)

class ReadAndWriteTextFiles(QMainWindow, Ui_MainWindow):

    def openFile(self, file):
        if not os.path.exists(file):
            return
        with open(file, "r") as openfile:
            textEdit = QTextEdit()
            msg = "open file: {0}".format(file)
            self.settings.setValue("openfile", file)
            self.fileNames.append(file)
            self.statusbar.setVisible(True)
            self.tabWidget.addTab(textEdit, os.path.basename(file))
            self.tabWidget.setCurrentWidget(textEdit)

            for readline in openfile.readlines():
                textEdit.textCursor().insertText(readline)

            self.showFileName.setText(msg)
            self.statusbar.showMessage(msg, 5000)

    def newFile(self, file):
        textEdit = QTextEdit()
        msg = "new file: {0}".format(file)
        self.fileNames.append(file)
        self.statusbar.setVisible(True)
        self.tabWidget.addTab(textEdit, os.path.basename(file))
        self.tabWidget.setCurrentWidget(textEdit)
        self.showFileName.setText(msg)
        self.statusbar.showMessage(msg, 5000)

    def saveFile(self, file):
        with open(file, "w") as savefile:
            self.settings.setValue("savefile", file)
            saveStr = self.tabWidget.currentWidget().toPlainText()
            savefile.write(saveStr)
            self.showFileName.setText("open file: {0}".format(file))
            self.statusbar.showMessage("save file: {0}".format(file), 5000)
            self.tabWidget.setTabText(self.tabWidget.currentIndex(), os.path.basename(file))

    def closeFile(self, index):
        self.tabWidget.removeTab(index)

    def __init__(self, parent=None):
        super(ReadAndWriteTextFiles, self).__init__(parent)
        self.setupUi(self)

        # add statusbar
        self.showFileName = QLineEdit()
        self.showFileName.setReadOnly(True)
        self.statusbar.addPermanentWidget(self.showFileName)
        self.statusbar.setVisible(False)

        self.actionOpenFile.triggered.connect(
            lambda: self.openFile(QFileDialog.getOpenFileName(self, "Open File", self.settings.value("openfile"), "text files(*)")[0])
        )
        self.actionNewFile.triggered.connect(
            lambda: self.newFile(os.path.join(os.getcwd(), "Untitled"))
        )
        self.actionSave.triggered.connect(
            lambda: self.saveFile(self.fileNames[self.tabWidget.currentIndex()])
        )
        self.actionSaveAs.triggered.connect(
            lambda: self.saveFile(QFileDialog.getSaveFileName(self, "Save File", self.settings.value("savefile"), "text files(*)")[0])
        )
        self.actionCloseFile.triggered.connect(
            lambda: self.closeFile(self.tabWidget.currentIndex())
        )
        self.actionQuit.triggered.connect(
            lambda: self.close()
        )
        # self.actionSettings.triggered.connect(self.__slot_settings)
        self.actionSettings.setVisible(False)

        self.tabWidget.currentChanged.connect(
            lambda index: self.showFileName.setText(self.fileNames[index])
        )
        self.fileNames = list()
        self.settings = QSettings(QApplication.applicationName() + ".ini", QSettings.IniFormat)

        if not self.settings.contains("openfile"):
            self.settings.setValue("openfile", QDir.homePath())

        if not self.settings.contains("savefile"):
            self.settings.setValue("savefile", QDir.homePath())


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-o", "--open_file",
                      type="string", dest="openfile",
                      help="打开文件")
    parser.add_option("-n", "--new_file",
                      type="string", dest="newfile",
                      help="新建文件")
    parser.add_option("-q", "--quiet",
                      action="store_true", dest="verbose",
                      help="安静模式", default=False)
    (options, args) = parser.parse_args()
    quiet = options.verbose
    if not options.verbose:
        print("open file:", options.openfile)
        print("new file:", options.newfile)
        print("quiet:", options.verbose)

    if options.openfile and options.newfile:
        parser.error("options -n and -o are mutually exclusive")

    app = QApplication(sys.argv)
    read_writefile = ReadAndWriteTextFiles()
    read_writefile.show()
    if options.openfile:
        read_writefile.openFile(options.openfile)

    if options.newfile:
        read_writefile.newFile(options.newfile)

    sys.exit(app.exec())
