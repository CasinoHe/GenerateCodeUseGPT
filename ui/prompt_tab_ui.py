# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prompt_tab.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(915, 335)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBoxPrompt = QGroupBox(Form)
        self.groupBoxPrompt.setObjectName(u"groupBoxPrompt")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBoxPrompt)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.labelSystem = QLabel(self.groupBoxPrompt)
        self.labelSystem.setObjectName(u"labelSystem")

        self.horizontalLayout_4.addWidget(self.labelSystem)

        self.lineEditPromptSystem = QLineEdit(self.groupBoxPrompt)
        self.lineEditPromptSystem.setObjectName(u"lineEditPromptSystem")

        self.horizontalLayout_4.addWidget(self.lineEditPromptSystem)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.plainTextEditPrompt = QPlainTextEdit(self.groupBoxPrompt)
        self.plainTextEditPrompt.setObjectName(u"plainTextEditPrompt")

        self.verticalLayout_2.addWidget(self.plainTextEditPrompt)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.labelPromptFilePath = QLabel(self.groupBoxPrompt)
        self.labelPromptFilePath.setObjectName(u"labelPromptFilePath")

        self.horizontalLayout_5.addWidget(self.labelPromptFilePath)

        self.lineEditPromptFilePath = QLineEdit(self.groupBoxPrompt)
        self.lineEditPromptFilePath.setObjectName(u"lineEditPromptFilePath")
        self.lineEditPromptFilePath.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.lineEditPromptFilePath)

        self.pushButtonPromptOpen = QPushButton(self.groupBoxPrompt)
        self.pushButtonPromptOpen.setObjectName(u"pushButtonPromptOpen")

        self.horizontalLayout_5.addWidget(self.pushButtonPromptOpen)

        self.pushButtonPromptSave = QPushButton(self.groupBoxPrompt)
        self.pushButtonPromptSave.setObjectName(u"pushButtonPromptSave")

        self.horizontalLayout_5.addWidget(self.pushButtonPromptSave)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.horizontalLayout.addWidget(self.groupBoxPrompt)

        self.groupBoxResponse = QGroupBox(Form)
        self.groupBoxResponse.setObjectName(u"groupBoxResponse")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBoxResponse)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.plainTextEditResponse = QPlainTextEdit(self.groupBoxResponse)
        self.plainTextEditResponse.setObjectName(u"plainTextEditResponse")

        self.verticalLayout_3.addWidget(self.plainTextEditResponse)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButtonCopyResult = QPushButton(self.groupBoxResponse)
        self.pushButtonCopyResult.setObjectName(u"pushButtonCopyResult")

        self.horizontalLayout_6.addWidget(self.pushButtonCopyResult)

        self.pushButtonSaveToFile = QPushButton(self.groupBoxResponse)
        self.pushButtonSaveToFile.setObjectName(u"pushButtonSaveToFile")

        self.horizontalLayout_6.addWidget(self.pushButtonSaveToFile)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.horizontalLayout.addWidget(self.groupBoxResponse)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBoxPrompt.setTitle(QCoreApplication.translate("Form", u"Prompt", None))
        self.labelSystem.setText(QCoreApplication.translate("Form", u"System background :", None))
        self.labelPromptFilePath.setText(QCoreApplication.translate("Form", u"File Path:", None))
        self.pushButtonPromptOpen.setText(QCoreApplication.translate("Form", u"Open", None))
        self.pushButtonPromptSave.setText(QCoreApplication.translate("Form", u"Save", None))
        self.groupBoxResponse.setTitle(QCoreApplication.translate("Form", u"Response", None))
        self.pushButtonCopyResult.setText(QCoreApplication.translate("Form", u"Copy Result", None))
        self.pushButtonSaveToFile.setText(QCoreApplication.translate("Form", u"Save to File", None))
    # retranslateUi

