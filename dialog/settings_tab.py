# -*- coding: utf-8 -*-
# Purpose: settings tab

from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox
from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices


import ui.settings_ui

class SettingsTab(QDialog):
    def __init__(self, parent):
        super().__init__(parent)

        # init system
        self.system = parent.system
        self.openai_key = ""
        self.google_palm_key = ""
        self.project_root_dir = ""
        self.result_json_dir = ""
        self.slack_token = ""
        self.claude_user_id = ""
        self.general_channel_id = ""

        # read config
        self.read_settings()

        # init ui
        self.ui = ui.settings_ui.Ui_Dialog()
        self.ui.setupUi(self)
        # set modal
        self.setModal(True)

        self.initUI()

    def initUI(self):
        # connect signals and slots
        self.ui.pushButtonOpenFolder.clicked.connect(self.clickOpenFolder)
        self.ui.pushButtonApplyOpenAIKey.clicked.connect(self.clickApplyOpenAIKey)
        self.ui.pushButtonApplyGooglePalmKey.clicked.connect(self.clickApplyGooglePalmKey)
        self.ui.pushButtonOpenResultJsonDir.clicked.connect(self.clickOpenResultJsonDir)

        self.ui.lineEditOpenAIKey.setText(self.openai_key)
        self.ui.lineEditGooglePalmKey.setText(self.google_palm_key)
        self.ui.lineEditRootDir.setText(self.project_root_dir)
        self.ui.lineEditResultJsonDir.setText(self.result_json_dir)
        self.ui.lineEditSlackAuthToken.setText(self.slack_token)
        self.ui.lineEditClaudeUserID.setText(self.claude_user_id)
        self.ui.lineEditSlackChannelID.setText(self.general_channel_id)

    def read_settings(self):
        self.openai_key = self.system.call_settings("InterfaceGetOpenAIKey")
        self.google_palm_key = self.system.call_settings("InterfaceGetGooglePalmKey")
        self.project_root_dir = self.system.call_settings("InterfaceGetProjectRootDir")
        self.result_json_dir = self.system.call_settings("InterfaceGetResultJsonDir")
        self.slack_token = self.system.call_settings("InterfaceGetSlackToken")
        self.claude_user_id = self.system.call_settings("InterfaceGetClaudeUserID")
        self.general_channel_id = self.system.call_settings("InterfaceGetGeneralChannelID")

    def show(self) -> None:
        self.ui.lineEditOpenAIKey.setText(self.openai_key)
        self.ui.lineEditGooglePalmKey.setText(self.google_palm_key)
        self.ui.lineEditRootDir.setText(self.project_root_dir)
        self.ui.lineEditResultJsonDir.setText(self.result_json_dir)
        self.ui.lineEditSlackAuthToken.setText(self.slack_token)
        self.ui.lineEditClaudeUserID.setText(self.claude_user_id)
        self.ui.lineEditSlackChannelID.setText(self.general_channel_id)
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
                self.save_settings()
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

    def save_settings(self):
        self.openai_key = self.ui.lineEditOpenAIKey.text()
        self.google_palm_key = self.ui.lineEditGooglePalmKey.text()
        self.project_root_dir = self.ui.lineEditRootDir.text()
        self.result_json_dir = self.ui.lineEditResultJsonDir.text()
        self.slack_token = self.ui.lineEditSlackAuthToken.text()
        self.claude_user_id = self.ui.lineEditClaudeUserID.text()
        self.general_channel_id = self.ui.lineEditSlackChannelID.text()

        self.system.call_settings("InterfaceSetOpenAIKey", self.openai_key)
        self.system.call_settings("InterfaceSetGooglePalmKey", self.google_palm_key)
        self.system.call_settings("InterfaceSetProjectRootDir", self.project_root_dir)
        self.system.call_settings("InterfaceSetResultJsonDir", self.result_json_dir)
        self.system.call_settings("InterfaceSetSlackToken", self.slack_token)
        self.system.call_settings("InterfaceSetClaudeUserID", self.claude_user_id)
        self.system.call_settings("InterfaceSetGeneralChannelID", self.general_channel_id)
        self.system.call_settings("InterfaceSaveConf")

    def textChanged(self):
        openai_key_text = self.ui.lineEditOpenAIKey.text()  
        google_palm_key_text = self.ui.lineEditGooglePalmKey.text()
        project_root_dir_text = self.ui.lineEditRootDir.text()
        result_json_dir_text = self.ui.lineEditResultJsonDir.text()
        slack_token = self.ui.lineEditSlackAuthToken.text()
        claude_user_id = self.ui.lineEditClaudeUserID.text()
        general_channel_id = self.ui.lineEditSlackChannelID.text()

        if openai_key_text != self.openai_key:
            return True
        if google_palm_key_text != self.google_palm_key:
            return True
        if project_root_dir_text != self.project_root_dir:
            return True
        if result_json_dir_text != self.result_json_dir:
            return True
        if slack_token != self.slack_token:
            return True
        if claude_user_id != self.claude_user_id:
            return True
        if general_channel_id != self.general_channel_id:
            return True
        else:
            return False

    def clickApplyOpenAIKey(self):
        url = QUrl("https://platform.openai.com/account/api-keys")
        QDesktopServices.openUrl(url)

    def clickApplyGooglePalmKey(self):
        url = QUrl("https://makersuite.google.com/app/apikey")
        QDesktopServices.openUrl(url)