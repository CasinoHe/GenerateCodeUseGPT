# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'example_tab.ui'
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

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        if not TabWidget.objectName():
            TabWidget.setObjectName(u"TabWidget")
        TabWidget.resize(915, 348)
        self.horizontalLayout = QHBoxLayout(TabWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBoxExample = QGroupBox(TabWidget)
        self.groupBoxExample.setObjectName(u"groupBoxExample")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBoxExample)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.plainTextEdit = QPlainTextEdit(self.groupBoxExample)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout_4.addWidget(self.plainTextEdit)

        self.groupBoxTabOperation = QGroupBox(self.groupBoxExample)
        self.groupBoxTabOperation.setObjectName(u"groupBoxTabOperation")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBoxTabOperation)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelOPenExample = QLabel(self.groupBoxTabOperation)
        self.labelOPenExample.setObjectName(u"labelOPenExample")

        self.horizontalLayout_3.addWidget(self.labelOPenExample)

        self.lineEditExample = QLineEdit(self.groupBoxTabOperation)
        self.lineEditExample.setObjectName(u"lineEditExample")
        self.lineEditExample.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.lineEditExample)

        self.pushButtonOpenExample = QPushButton(self.groupBoxTabOperation)
        self.pushButtonOpenExample.setObjectName(u"pushButtonOpenExample")

        self.horizontalLayout_3.addWidget(self.pushButtonOpenExample)

        self.pushButtonRefresh = QPushButton(self.groupBoxTabOperation)
        self.pushButtonRefresh.setObjectName(u"pushButtonRefresh")

        self.horizontalLayout_3.addWidget(self.pushButtonRefresh)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addWidget(self.groupBoxTabOperation)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBoxDesc = QGroupBox(self.groupBoxExample)
        self.groupBoxDesc.setObjectName(u"groupBoxDesc")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBoxDesc)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.plainTextEditExampleDesc = QPlainTextEdit(self.groupBoxDesc)
        self.plainTextEditExampleDesc.setObjectName(u"plainTextEditExampleDesc")

        self.horizontalLayout_4.addWidget(self.plainTextEditExampleDesc)


        self.verticalLayout_3.addWidget(self.groupBoxDesc)

        self.groupBoxResponse = QGroupBox(self.groupBoxExample)
        self.groupBoxResponse.setObjectName(u"groupBoxResponse")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBoxResponse)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.plainTextEditExampleResponse = QPlainTextEdit(self.groupBoxResponse)
        self.plainTextEditExampleResponse.setObjectName(u"plainTextEditExampleResponse")

        self.horizontalLayout_6.addWidget(self.plainTextEditExampleResponse)


        self.verticalLayout_3.addWidget(self.groupBoxResponse)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)


        self.verticalLayout.addWidget(self.groupBoxExample)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(TabWidget)

        QMetaObject.connectSlotsByName(TabWidget)
    # setupUi

    def retranslateUi(self, TabWidget):
        TabWidget.setWindowTitle(QCoreApplication.translate("TabWidget", u"Form", None))
        self.groupBoxExample.setTitle(QCoreApplication.translate("TabWidget", u"Example Content", None))
        self.groupBoxTabOperation.setTitle(QCoreApplication.translate("TabWidget", u"Example Content Operation", None))
        self.labelOPenExample.setText(QCoreApplication.translate("TabWidget", u"File path : ", None))
        self.pushButtonOpenExample.setText(QCoreApplication.translate("TabWidget", u"Open", None))
        self.pushButtonRefresh.setText(QCoreApplication.translate("TabWidget", u"Refresh", None))
        self.groupBoxDesc.setTitle(QCoreApplication.translate("TabWidget", u"Example Desc", None))
        self.groupBoxResponse.setTitle(QCoreApplication.translate("TabWidget", u"Example Response", None))
    # retranslateUi

