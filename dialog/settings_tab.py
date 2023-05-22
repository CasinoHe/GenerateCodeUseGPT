# -*- coding: utf-8 -*-
# Purpose: settings tab

from PyQt6.QtWidgets import QDialog, QFileDialog, QMessageBox

import ui.settings_ui

class SettingsTab(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # init system
        self.system = parent.system.call_settings # type: ignore

        # init ui
        self.ui = ui.settings_ui.Ui_Dialog()
        self.ui.setupUi(self)

        self.initUI()

    def initUI(self):
        # connect signals and slots
        self.ui.pushButtonOpenFolder.clicked.connect(self.clickOpenFolder)

        openai_key = self.system("InterfaceGetOpenAIKey")
        google_palm_key = self.system("InterfaceGetGooglePalmKey")
        project_root_dir = self.system("InterfaceGetProjectRootDir")

        self.ui.lineEditOpenAIKey.setText(openai_key)
        self.ui.lineEditGooglePalmKey.setText(google_palm_key)
        self.ui.lineEditRootDir.setText(project_root_dir)

    def clickOpenFolder(self):
        # get settings file path
        folder_path = QFileDialog.getExistingDirectory(self, "Set Project Root Folder", "/")
        if not folder_path:
            # use QMessageBox to display a warning
            QMessageBox.warning(self, "Warning", "Please select the root folder of the project")
            return
        else:
            self.ui.lineEditRootDir.setText(folder_path)

    def accept(self) -> None:
        # open a confirm dialog to confirm the settings
        reply = QMessageBox.question(self, "Confirm", "Are you sure to save the settings?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            # save the settings
            self.saveSettings()
            return super().accept()
        else:
            return super().reject()

    def saveSettings(self):
        openai_key = self.ui.lineEditOpenAIKey.text()
        google_palm_key = self.ui.lineEditGooglePalmKey.text()
        project_root_dir = self.ui.lineEditRootDir.text()

        self.system("InterfaceSetOpenAIKey", openai_key)
        self.system("InterfaceSetGooglePalmKey", google_palm_key)
        self.system("InterfaceSetProjectRootDir", project_root_dir)
        self.system("InterfaceSaveConf")