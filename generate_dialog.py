# -*- coding: utf-8 -*-
# author: CasinoHe
# Purpose:
#    Create a GUI dialog to generate code, So it's easy to use

# using PyQt6 to create a GUI dialog
from PyQt6.QtWidgets import QDialog
from PyQt6 import uic
from ui import generate_dialog_ui


class GenerateCodeDialog(QDialog):
    '''
    GenerateCodeDialog is a dialog that provice convinient way to generate code
    the dialog is divided into 4 parts:
        1. select example file
        2. select prompt file
        3. select models, and set parameters
        4. generate code
    '''
    def __init__(self, parent=None):
        super(GenerateCodeDialog, self).__init__(parent)
        self.ui = None
        self.initUI()

    def initUI(self):
        # create dialog from a ui file
        if not self.ui:
            self.ui = generate_dialog_ui.Ui_Dialog()
            self.ui.setupUi(self)
