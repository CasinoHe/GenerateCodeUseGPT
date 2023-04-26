# -*- coding: utf-8 -*-
# author: CasinoHe
# Purpose: the dialog of prompt tab

from PyQt6.QtWidgets import QWidget, QFileDialog, QMessageBox
from ui import prompt_tab_ui

class PromptTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # init ui
        self.ui = prompt_tab_ui.Ui_Form()
        self.ui.setupUi(self)

        self.initUI()

    def initUI(self):
        pass