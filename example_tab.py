# -*- coding: utf-8 -*-
# author: CasinoHe
# Purpose: the dialog of example tab

from PyQt6.QtWidgets import QWidget, QFileDialog, QMessageBox
from ui import example_tab_ui

class ExampleTab(QWidget):
    '''
    ExampleTab is a widget that provide convinient way to select example file
    '''
    def __init__(self, callback, parent=None):
        super(ExampleTab, self).__init__(parent)

        # init ui
        self.ui = example_tab_ui.Ui_TabWidget()
        self.ui.setupUi(self)
        self.open_example_callback = callback
        self.initUI()

    def initUI(self):

        # connect singals and slots
        self.ui.pushButtonOpenExample.clicked.connect(self.clickOpenExampleFile)
        self.ui.pushButtonRefresh.clicked.connect(self.clickRefreshExample)

        # disable refresh button first, because there is no file selected
        self.ui.pushButtonRefresh.setEnabled(False)
        
    def clickOpenExampleFile(self):
        filepath = QFileDialog.getOpenFileName(self, "Open Example File", "./", "Python Files (*.py);;All Files (*)")
        # if user select a file, then set the file path to lineEdit
        if len(filepath[0]) <= 0:
            return

        # set file path to lineEdit
        self.ui.lineEditExample.setText(filepath[0])

        # enable refresh button
        self.ui.pushButtonRefresh.setEnabled(True)

        # read file content to plainTextEdit and refresh it
        with open(filepath[0], "r", encoding='utf-8') as f:
            self.ui.plainTextEdit.setPlainText(f.read())
        self.open_example_callback()

    def clickRefreshExample(self):
        if len(self.ui.lineEditExample.text()) <= 0:
            # use QmessageBox to display a warning
            QMessageBox.warning(self, "Warning", "Please select a file first")
            return
        # read file content to plainTextEdit and refresh it
        with open(self.ui.lineEditExample.text(), "r", encoding='utf-8') as f:
            self.ui.plainTextEdit.setPlainText(f.read())

    def getExampleContent(self):
        return self.ui.plainTextEdit.toPlainText()