# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(728, 221)
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEditRootDir = QLineEdit(Dialog)
        self.lineEditRootDir.setObjectName(u"lineEditRootDir")

        self.horizontalLayout_2.addWidget(self.lineEditRootDir)

        self.pushButtonOpenFolder = QPushButton(Dialog)
        self.pushButtonOpenFolder.setObjectName(u"pushButtonOpenFolder")

        self.horizontalLayout_2.addWidget(self.pushButtonOpenFolder)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.lineEditResultJsonDir = QLineEdit(Dialog)
        self.lineEditResultJsonDir.setObjectName(u"lineEditResultJsonDir")

        self.horizontalLayout_5.addWidget(self.lineEditResultJsonDir)

        self.pushButtonOpenResultJsonDir = QPushButton(Dialog)
        self.pushButtonOpenResultJsonDir.setObjectName(u"pushButtonOpenResultJsonDir")

        self.horizontalLayout_5.addWidget(self.pushButtonOpenResultJsonDir)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lineEditOpenAIKey = QLineEdit(Dialog)
        self.lineEditOpenAIKey.setObjectName(u"lineEditOpenAIKey")

        self.horizontalLayout_3.addWidget(self.lineEditOpenAIKey)

        self.pushButtonApplyOpenAIKey = QPushButton(Dialog)
        self.pushButtonApplyOpenAIKey.setObjectName(u"pushButtonApplyOpenAIKey")

        self.horizontalLayout_3.addWidget(self.pushButtonApplyOpenAIKey)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.lineEditGooglePalmKey = QLineEdit(Dialog)
        self.lineEditGooglePalmKey.setObjectName(u"lineEditGooglePalmKey")

        self.horizontalLayout_4.addWidget(self.lineEditGooglePalmKey)

        self.pushButtonApplyGooglePalmKey = QPushButton(Dialog)
        self.pushButtonApplyGooglePalmKey.setObjectName(u"pushButtonApplyGooglePalmKey")

        self.horizontalLayout_4.addWidget(self.pushButtonApplyGooglePalmKey)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.lineEditSlackAuthToken = QLineEdit(Dialog)
        self.lineEditSlackAuthToken.setObjectName(u"lineEditSlackAuthToken")

        self.horizontalLayout_6.addWidget(self.lineEditSlackAuthToken)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.lineEditClaudeUserID = QLineEdit(Dialog)
        self.lineEditClaudeUserID.setObjectName(u"lineEditClaudeUserID")

        self.horizontalLayout_6.addWidget(self.lineEditClaudeUserID)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.lineEditSlackChannelID = QLineEdit(Dialog)
        self.lineEditSlackChannelID.setObjectName(u"lineEditSlackChannelID")

        self.horizontalLayout_6.addWidget(self.lineEditSlackChannelID)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Project Root Dir: ", None))
        self.pushButtonOpenFolder.setText(QCoreApplication.translate("Dialog", u"Open Folder...", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Result Json Dir: ", None))
        self.pushButtonOpenResultJsonDir.setText(QCoreApplication.translate("Dialog", u"Open Folder...", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"OpenAI api-key:", None))
        self.pushButtonApplyOpenAIKey.setText(QCoreApplication.translate("Dialog", u"Apply OpenAI api-key", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Google PaLM api-key: ", None))
        self.pushButtonApplyGooglePalmKey.setText(QCoreApplication.translate("Dialog", u"Apply Google PaLM api-key", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"SlackApp Token", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Claude user ID: ", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"General Channel ID: ", None))
    # retranslateUi

