# -*- coding: utf-8 -*-
# author: CasinoHe
# Purpose: the dialog of prompt tab

from PyQt6.QtWidgets import QWidget, QFileDialog, QMessageBox
from ui import prompt_tab_ui
import json

class PromptTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # init ui
        self.ui = prompt_tab_ui.Ui_Form()
        self.ui.setupUi(self)

        self.initUI()

    def initUI(self):
        # disable file lineEdit
        self.ui.lineEditPromptFilePath.setEnabled(False)

        # connect signals and slots
        self.ui.pushButtonPromptOpen.clicked.connect(self.clickOpenPromptFile)
        self.ui.pushButtonPromptSave.clicked.connect(self.clickSavePrompt)

    def clickSavePrompt(self):
        # get prompt file path
        prompt_file, _ = QFileDialog.getSaveFileName(self, "Save Prompt File", "", "JSON Files (*.json)")
        if len(prompt_file) <= 0:
            # use QMessageBox to display a warning
            QMessageBox.warning(self, "Warning", "Please select a file first")
            return

        # get prompt content
        prompt = {
            "prompt": self.ui.plainTextEditPrompt.toPlainText(),
            "system": self.ui.lineEditPromptSystem.text(),
            "response": self.ui.plainTextEditResponse.toPlainText()
        }

        # save prompt to file
        with open(prompt_file, "w", encoding='utf-8') as f:
            json.dump(prompt, f, ensure_ascii=False, indent=4)
            QMessageBox.information(self, "Information", "Save prompt file successfully")

    def clickOpenPromptFile(self):
        # use QFileDialog to select a prompt file
        prompt_file, _ = QFileDialog.getOpenFileName(self, "Open Prompt File", "", "JSON Files (*.json)")
        if prompt_file:
            self.ui.lineEditPromptFilePath.setText(prompt_file)

            # read file content and show it in PlainTextEdit
            with open(prompt_file, "r", encoding='utf-8') as f:
                # parse json file
                prompt = json.load(f)
                self.ui.plainTextEditPrompt.setPlainText(prompt["prompt"])
                self.ui.lineEditPromptSystem.setText(prompt["system"])
                self.ui.plainTextEditResponse.setPlainText(prompt["response"])

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