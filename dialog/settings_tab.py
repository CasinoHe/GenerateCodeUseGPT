# -*- coding: utf-8 -*-
# Purpose: settings tab

from PyQt6.QtWidgets import QDialog, QFileDialog, QMessageBox
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices


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
        self.ui.pushButtonApplyOpenAIKey.clicked.connect(self.clickApplyOpenAIKey)
        self.ui.pushButtonApplyGooglePalmKey.clicked.connect(self.clickApplyGooglePalmKey)

        openai_key = self.system("InterfaceGetOpenAIKey")
        google_palm_key = self.system("InterfaceGetGooglePalmKey")
        project_root_dir = self.system("InterfaceGetProjectRootDir")

        self.ui.lineEditOpenAIKey.setText(openai_key)
        self.ui.lineEditGooglePalmKey.setText(google_palm_key)
        self.ui.lineEditRootDir.setText(project_root_dir)

    def show(self) -> None:
        openai_key = self.system("InterfaceGetOpenAIKey")
        google_palm_key = self.system("InterfaceGetGooglePalmKey")
        project_root_dir = self.system("InterfaceGetProjectRootDir")

        self.ui.lineEditOpenAIKey.setText(openai_key)
        self.ui.lineEditGooglePalmKey.setText(google_palm_key)
        self.ui.lineEditRootDir.setText(project_root_dir)
        return super().show()

    def clickOpenFolder(self):
        project_root_dir = self.system("InterfaceGetProjectRootDir")
        if not project_root_dir:
            project_root_dir = "/"

        # get settings file path
        folder_path = QFileDialog.getExistingDirectory(self, "Set Project Root Folder", project_root_dir)
        if not folder_path:
            display_text = self.ui.lineEditRootDir.text()
            if not display_text:
                # use QMessageBox to display a warning
                QMessageBox.warning(self, "Warning", "Please select the root folder of the project")
                return
        else:
            self.ui.lineEditRootDir.setText(folder_path)

    def accept(self) -> None:
        if self.textChanged():
            # open a confirm dialog to confirm the settings
            reply = QMessageBox.question(self, "Confirm", "Are you sure to save the settings?",
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                # save the settings
                self.saveSettings()
                return super().accept()
            else:
                return None
        else:
            return super().accept()

    def reject(self) -> None:
        if self.textChanged():
            # open a confirm dialog to confirm the settings
            reply = QMessageBox.question(self, "Confirm", "Are you sure to discard the settings?",
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                return super().reject()
            else:
                return None
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

    def textChanged(self):
        openai_key = self.system("InterfaceGetOpenAIKey")
        google_palm_key = self.system("InterfaceGetGooglePalmKey")
        project_root_dir = self.system("InterfaceGetProjectRootDir")

        openai_key_text = self.ui.lineEditOpenAIKey.text()  
        google_palm_key_text = self.ui.lineEditGooglePalmKey.text()
        project_root_dir_text = self.ui.lineEditRootDir.text()

        if openai_key_text != openai_key or google_palm_key_text != google_palm_key or project_root_dir_text != project_root_dir:
            return True
        else:
            return False

    def clickApplyOpenAIKey(self):
        url = QUrl("https://platform.openai.com/account/api-keys")
        QDesktopServices.openUrl(url)

    def clickApplyGooglePalmKey(self):
        url = QUrl("https://makersuite.google.com/app/apikey")
        QDesktopServices.openUrl(url)