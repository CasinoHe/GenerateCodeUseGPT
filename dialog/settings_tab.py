# -*- coding: utf-8 -*-
# Purpose: settings tab

from PyQt6.QtWidgets import QDialog, QFileDialog, QMessageBox
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices


import ui.settings_ui

class SettingsTab(QDialog):
    def __init__(self, parent):
        super().__init__(parent)

        # init system
        self.system = parent.system

        # init ui
        self.ui = ui.settings_ui.Ui_Dialog()
        self.ui.setupUi(self)

        self.initUI()

    def initUI(self):
        # connect signals and slots
        self.ui.pushButtonOpenFolder.clicked.connect(self.clickOpenFolder)
        self.ui.pushButtonApplyOpenAIKey.clicked.connect(self.clickApplyOpenAIKey)
        self.ui.pushButtonApplyGooglePalmKey.clicked.connect(self.clickApplyGooglePalmKey)
        self.ui.pushButtonOpenResultJsonDir.clicked.connect(self.clickOpenResultJsonDir)

        openai_key = self.system.call_settings("InterfaceGetOpenAIKey")
        google_palm_key = self.system.call_settings("InterfaceGetGooglePalmKey")
        project_root_dir = self.system.call_settings("InterfaceGetProjectRootDir")
        result_json_dir = self.system.call_settings("InterfaceGetResultJsonDir")

        self.ui.lineEditOpenAIKey.setText(openai_key)
        self.ui.lineEditGooglePalmKey.setText(google_palm_key)
        self.ui.lineEditRootDir.setText(project_root_dir)
        self.ui.lineEditResultJsonDir.setText(result_json_dir)

    def show(self) -> None:
        openai_key = self.system.call_settings("InterfaceGetOpenAIKey")
        google_palm_key = self.system.call_settings("InterfaceGetGooglePalmKey")
        project_root_dir = self.system.call_settings("InterfaceGetProjectRootDir")
        result_json_dir = self.system.call_settings("InterfaceGetResultJsonDir")

        self.ui.lineEditOpenAIKey.setText(openai_key)
        self.ui.lineEditGooglePalmKey.setText(google_palm_key)
        self.ui.lineEditRootDir.setText(project_root_dir)
        self.ui.lineEditResultJsonDir.setText(result_json_dir)
        return super().show()

    def clickOpenResultJsonDir(self):
        result_json_dir = self.system.call_settings("InterfaceGetResultJsonDir")
        if not result_json_dir:
            result_json_dir = "/"

        # get settings file path
        folder_path = QFileDialog.getExistingDirectory(self, "Set Result Json Folder", result_json_dir)
        if not folder_path:
            display_text = self.ui.lineEditResultJsonDir.text()
            if not display_text:
                # use QMessageBox to display a warning
                QMessageBox.warning(self, "Warning", "Please select the result json folder")
                return
        else:
            self.ui.lineEditResultJsonDir.setText(folder_path)

    def clickOpenFolder(self):
        project_root_dir = self.system.call_settings("InterfaceGetProjectRootDir")
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
                if self.system.call_settings("InterfaceIsEmpty"):
                    QMessageBox.warning(self, "Warning", "Please set at least one api settings first")
                    return None
                else:
                    return super().accept()
            else:
                return None
        else:
            if self.system.call_settings("InterfaceIsEmpty"):
                QMessageBox.warning(self, "Warning", "Please set at least one api settings first")
                return None
            else:
                return super().accept()

    def reject(self) -> None:
        if self.system.call_settings("InterfaceIsEmpty"):
            QMessageBox.warning(self, "Warning", "Please set at least one api settings first")
            return None

        if self.textChanged():
            # open a confirm dialog to confirm the settings
            reply = QMessageBox.question(self, "Confirm", "Are you sure to discard the settings?",
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                return super().reject()
            else:
                return None
        else:
            if self.system.call_settings("InterfaceIsEmpty"):
                QMessageBox.warning(self, "Warning", "Please set at least one api settings first")
                return None
            else:
                return super().reject()

    def saveSettings(self):
        openai_key = self.ui.lineEditOpenAIKey.text()
        google_palm_key = self.ui.lineEditGooglePalmKey.text()
        project_root_dir = self.ui.lineEditRootDir.text()
        result_json_dir = self.ui.lineEditResultJsonDir.text()

        self.system.call_settings("InterfaceSetOpenAIKey", openai_key)
        self.system.call_settings("InterfaceSetGooglePalmKey", google_palm_key)
        self.system.call_settings("InterfaceSetProjectRootDir", project_root_dir)
        self.system.call_settings("InterfaceSetResultJsonDir", result_json_dir)
        self.system.call_settings("InterfaceSaveConf")

    def textChanged(self):
        openai_key = self.system.call_settings("InterfaceGetOpenAIKey")
        google_palm_key = self.system.call_settings("InterfaceGetGooglePalmKey")
        project_root_dir = self.system.call_settings("InterfaceGetProjectRootDir")
        result_json_dir = self.system.call_settings("InterfaceGetResultJsonDir")

        openai_key_text = self.ui.lineEditOpenAIKey.text()  
        google_palm_key_text = self.ui.lineEditGooglePalmKey.text()
        project_root_dir_text = self.ui.lineEditRootDir.text()
        result_json_dir_text = self.ui.lineEditResultJsonDir.text()

        if openai_key != openai_key_text or google_palm_key != google_palm_key_text:
            self.system.InterfaceRefreshSystem()

        if openai_key_text != openai_key or google_palm_key_text != google_palm_key \
                or project_root_dir_text != project_root_dir or result_json_dir_text != result_json_dir:
            return True
        else:
            return False

    def clickApplyOpenAIKey(self):
        url = QUrl("https://platform.openai.com/account/api-keys")
        QDesktopServices.openUrl(url)

    def clickApplyGooglePalmKey(self):
        url = QUrl("https://makersuite.google.com/app/apikey")
        QDesktopServices.openUrl(url)