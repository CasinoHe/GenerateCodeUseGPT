# -*- coding: utf-8 -*-
# author: CasinoHe
# Purpose: the dialog of prompt tab

from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox, QApplication
from PySide6 import QtGui
from ui import prompt_tab_ui

class PromptTab(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        # init ui
        self.ui = prompt_tab_ui.Ui_Form()
        self.ui.setupUi(self)

        self.initUI()

        self.system = parent.system

    def initUI(self):
        # disable file lineEdit
        self.ui.lineEditPromptFilePath.setEnabled(False)

        # connect signals and slots
        self.ui.pushButtonPromptOpen.clicked.connect(self.clickOpenPromptFile)
        self.ui.pushButtonPromptSave.clicked.connect(self.clickSavePrompt)
        # connect copy result button
        self.ui.pushButtonCopyResult.clicked.connect(self.clickCopyResult)
        # connect save file button
        self.ui.pushButtonSaveToFile.clicked.connect(self.clickSaveResultToFile)

    def clickSavePrompt(self):
        result_dir = self.system.call_settings("InterfaceGetResultJsonDir")
        # get prompt file path
        prompt_file, _ = QFileDialog.getSaveFileName(self, "Save Prompt File", result_dir, "JSON Files (*.json)")
        if len(prompt_file) <= 0:
            # use QMessageBox to display a warning
            QMessageBox.warning(self, "Warning", "Please select a file first")
            return

        # get prompt content
        prompt = self.ui.plainTextEditPrompt.toPlainText()
        context = self.ui.lineEditPromptSystem.text()
        response = self.ui.plainTextEditResponse.toPlainText()

        # save prompt to file
        result = self.system.call_database("InterfaceSavePrompt", prompt, context, response, prompt_file)
        if result:
            QMessageBox.information(self, "Information", "Save prompt file successfully")
        else:
            QMessageBox.warning(self, "Warning", "Save prompt file failed")

    def clickOpenPromptFile(self):
        result_dir = self.system.call_settings("InterfaceGetResultJsonDir")
        # use QFileDialog to select a prompt file
        prompt_file, _ = QFileDialog.getOpenFileName(self, "Open Prompt File", result_dir, "JSON Files (*.json)")
        if prompt_file:
            self.ui.lineEditPromptFilePath.setText(prompt_file)

            # read file content and show it in PlainTextEdit
            prompt, system, response = self.system.call_database("InterfaceLoadPrompt", prompt_file)
            self.ui.plainTextEditPrompt.setPlainText(prompt)
            self.ui.lineEditPromptSystem.setText(system)
            self.ui.plainTextEditResponse.setPlainText(response)

    def clear(self):
        self.ui.lineEditPromptFilePath.clear()
        self.ui.plainTextEditPrompt.clear()
        self.ui.lineEditPromptSystem.clear()
        self.ui.plainTextEditResponse.clear()

    def getPromptFile(self):
        return self.ui.lineEditPromptFilePath.text()
    
    def getPromptContent(self):
        return self.ui.plainTextEditPrompt.toPlainText()

    def getPromptSystem(self):
        return self.ui.lineEditPromptSystem.text()
    
    def getPromptResponse(self):
        return self.ui.plainTextEditResponse.toPlainText()

    def setPromptContent(self, content):
        self.ui.plainTextEditPrompt.setPlainText(content)

    def setPromptSystem(self, system):
        self.ui.lineEditPromptSystem.setText(system)

    def setPromptResponse(self, response):
        self.ui.plainTextEditResponse.setPlainText(response)
    
    def clearPromptResponse(self):
        self.ui.plainTextEditResponse.clear()

    def appendPromptResponse(self, response):
        # append result in plainTextEditResult without newline
        text_cursor = QtGui.QTextCursor(self.ui.plainTextEditResponse.document())
        text_cursor.movePosition(QtGui.QTextCursor.MoveOperation.End)
        text_cursor.insertText(response)

    def setPromptFile(self, filepath):
        self.ui.lineEditPromptFilePath.setText(filepath)

    def setFocusResponseContent(self):
        self.ui.plainTextEditResponse.setFocus()

    def isEmpty(self):
        if self.ui.plainTextEditPrompt.toPlainText() == "" or self.ui.plainTextEditResponse.toPlainText() == "":
            return True
        else:
            return False

    def isPromptEmpty(self):
        if self.ui.plainTextEditPrompt.toPlainText() == "":
            return True
        else:
            return False

    def clickCopyResult(self):
        # copy the text in plainTextEditResult to clipboard
        text = self.ui.plainTextEditResponse.toPlainText()
        if text:
            # call system clipboard
            clipboard = QApplication.clipboard()
            clipboard.setText(text)
            # show a message box to user
            QMessageBox.information(self, "Copy Result", "Copy result to clipboard successfully!")
        else:
            QMessageBox.warning(self, "Copy Result", "No result to copy!")

    def initGenerateResult(self):
        self.ui.plainTextEditResponse.clear()

    def clickSaveResultToFile(self):
        # get result content
        result = self.ui.plainTextEditResponse.toPlainText()
        if not result:
            QMessageBox.warning(self, "Warning", "No result to save")
            return

        # get result file path
        result_dir = self.system.call_settings("InterfaceGetResultJsonDir")
        result_file, _ = QFileDialog.getSaveFileName(self, "Save Result File", result_dir, "JSON Files (*.json)")
        if len(result_file) <= 0:
            # use QMessageBox to display a warning
            QMessageBox.warning(self, "Warning", "Please select a file first")
            return

        # save result to file
        with open(result_file, "w", encoding="utf-8") as f:
            if f.write(result) <= 0:
                QMessageBox.warning(self, "Warning", "Save result file failed")
            else:
                QMessageBox.information(
                    self, "Information", "Save result file successfully")
