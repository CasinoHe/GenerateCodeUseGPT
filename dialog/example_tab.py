# -*- coding: utf-8 -*-
# author: CasinoHe
# Purpose: the dialog of example tab

from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
from ui import example_tab_ui

class ExampleTab(QWidget):
    '''
    ExampleTab is a widget that provide convinient way to select example file
    '''
    def __init__(self, callback, parent):
        super(ExampleTab, self).__init__(parent)

        self.system = parent.system
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
        project_dir = self.system.call_settings("InterfaceGetProjectRootDir")
        filepath = QFileDialog.getOpenFileName(self, "Open Example File", project_dir, "Python Files (*.py);;All Files (*)")
        # if user select a file, then set the file path to lineEdit
        if len(filepath[0]) <= 0:
            return

        self.loadExampleFileDirectly(filepath[0])

    def loadExampleFileDirectly(self, file_path):
        # set file path to lineEdit
        self.ui.lineEditExample.setText(file_path)
        # read file content to plainTextEdit and refresh it
        with open(file_path, "r", encoding='utf-8') as f:
            self.ui.plainTextEdit.setPlainText(f.read())

        # enable refresh button
        self.ui.pushButtonRefresh.setEnabled(True)
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

    def getExampleFile(self):
        return self.ui.lineEditExample.text()

    def setExampleFile(self, filepath):
        self.ui.lineEditExample.setText(filepath)
        self.ui.pushButtonRefresh.setEnabled(True)

    def setExampleContent(self, content):
        self.ui.plainTextEdit.setPlainText(content)

    def getExampleDesc(self):
        return self.ui.plainTextEditExampleDesc.toPlainText()

    def setExampleDesc(self, desc):
        self.ui.plainTextEditExampleDesc.setPlainText(desc)

    def getExampleResponse(self):
        return self.ui.plainTextEditExampleResponse.toPlainText()
    
    def setExampleResponse(self, response):
        self.ui.plainTextEditExampleResponse.setPlainText(response)

    def clear(self):
        # clear lineEdit and plainTextEdit
        self.ui.lineEditExample.clear()
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEditExampleDesc.clear()