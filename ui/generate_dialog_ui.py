# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'generate_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QDoubleSpinBox,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1278, 888)
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1258, 868))
        self.horizontalLayout_17 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBoxExamples = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxExamples.setObjectName(u"groupBoxExamples")
        self.verticalLayout_2 = QVBoxLayout(self.groupBoxExamples)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidgetExamples = QTabWidget(self.groupBoxExamples)
        self.tabWidgetExamples.setObjectName(u"tabWidgetExamples")
        self.tabExample1 = QWidget()
        self.tabExample1.setObjectName(u"tabExample1")
        self.tabWidgetExamples.addTab(self.tabExample1, "")
        self.tabExample2 = QWidget()
        self.tabExample2.setObjectName(u"tabExample2")
        self.tabExample2.setEnabled(True)
        self.tabWidgetExamples.addTab(self.tabExample2, "")

        self.verticalLayout_2.addWidget(self.tabWidgetExamples)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_6)

        self.pushButtonClearExample = QPushButton(self.groupBoxExamples)
        self.pushButtonClearExample.setObjectName(u"pushButtonClearExample")

        self.horizontalLayout_15.addWidget(self.pushButtonClearExample)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_4)

        self.pushButtonDeleteExample = QPushButton(self.groupBoxExamples)
        self.pushButtonDeleteExample.setObjectName(u"pushButtonDeleteExample")

        self.horizontalLayout_15.addWidget(self.pushButtonDeleteExample)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_5)

        self.pushButtonNewExample = QPushButton(self.groupBoxExamples)
        self.pushButtonNewExample.setObjectName(u"pushButtonNewExample")

        self.horizontalLayout_15.addWidget(self.pushButtonNewExample)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_15)


        self.verticalLayout.addWidget(self.groupBoxExamples)

        self.groupBoxPrompt = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxPrompt.setObjectName(u"groupBoxPrompt")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBoxPrompt)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidgetPrompt = QTabWidget(self.groupBoxPrompt)
        self.tabWidgetPrompt.setObjectName(u"tabWidgetPrompt")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidgetPrompt.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidgetPrompt.addTab(self.tab_2, "")

        self.verticalLayout_3.addWidget(self.tabWidgetPrompt)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.pushButtonClearPrompt = QPushButton(self.groupBoxPrompt)
        self.pushButtonClearPrompt.setObjectName(u"pushButtonClearPrompt")

        self.horizontalLayout_2.addWidget(self.pushButtonClearPrompt)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButtonDeletePrompt = QPushButton(self.groupBoxPrompt)
        self.pushButtonDeletePrompt.setObjectName(u"pushButtonDeletePrompt")

        self.horizontalLayout_2.addWidget(self.pushButtonDeletePrompt)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButtonNewPrompt = QPushButton(self.groupBoxPrompt)
        self.pushButtonNewPrompt.setObjectName(u"pushButtonNewPrompt")

        self.horizontalLayout_2.addWidget(self.pushButtonNewPrompt)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.verticalLayout.addWidget(self.groupBoxPrompt)

        self.groupBoxOutPut = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxOutPut.setObjectName(u"groupBoxOutPut")
        self.horizontalLayout_12 = QHBoxLayout(self.groupBoxOutPut)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.plainTextEditResult = QPlainTextEdit(self.groupBoxOutPut)
        self.plainTextEditResult.setObjectName(u"plainTextEditResult")

        self.verticalLayout_8.addWidget(self.plainTextEditResult)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.labelUsedToken = QLabel(self.groupBoxOutPut)
        self.labelUsedToken.setObjectName(u"labelUsedToken")

        self.horizontalLayout_21.addWidget(self.labelUsedToken)

        self.lineEditTokenAmount = QLineEdit(self.groupBoxOutPut)
        self.lineEditTokenAmount.setObjectName(u"lineEditTokenAmount")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditTokenAmount.sizePolicy().hasHeightForWidth())
        self.lineEditTokenAmount.setSizePolicy(sizePolicy)
        self.lineEditTokenAmount.setReadOnly(True)

        self.horizontalLayout_21.addWidget(self.lineEditTokenAmount)

        self.labelEstimateCost = QLabel(self.groupBoxOutPut)
        self.labelEstimateCost.setObjectName(u"labelEstimateCost")

        self.horizontalLayout_21.addWidget(self.labelEstimateCost)

        self.lineEditEstimateCost = QLineEdit(self.groupBoxOutPut)
        self.lineEditEstimateCost.setObjectName(u"lineEditEstimateCost")
        self.lineEditEstimateCost.setReadOnly(True)

        self.horizontalLayout_21.addWidget(self.lineEditEstimateCost)

        self.labelRealCost = QLabel(self.groupBoxOutPut)
        self.labelRealCost.setObjectName(u"labelRealCost")

        self.horizontalLayout_21.addWidget(self.labelRealCost)

        self.lineEdit = QLineEdit(self.groupBoxOutPut)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_21.addWidget(self.lineEdit)

        self.label_3 = QLabel(self.groupBoxOutPut)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_21.addWidget(self.label_3)

        self.lineEditTotalCost = QLineEdit(self.groupBoxOutPut)
        self.lineEditTotalCost.setObjectName(u"lineEditTotalCost")

        self.horizontalLayout_21.addWidget(self.lineEditTotalCost)

        self.label_2 = QLabel(self.groupBoxOutPut)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_21.addWidget(self.label_2)

        self.lineEditHistoricalCost = QLineEdit(self.groupBoxOutPut)
        self.lineEditHistoricalCost.setObjectName(u"lineEditHistoricalCost")

        self.horizontalLayout_21.addWidget(self.lineEditHistoricalCost)


        self.verticalLayout_8.addLayout(self.horizontalLayout_21)


        self.horizontalLayout_11.addLayout(self.verticalLayout_8)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.groupBoxResult = QGroupBox(self.groupBoxOutPut)
        self.groupBoxResult.setObjectName(u"groupBoxResult")
        self.horizontalLayout_14 = QHBoxLayout(self.groupBoxResult)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.comboBoxSupplyName = QComboBox(self.groupBoxResult)
        self.comboBoxSupplyName.setObjectName(u"comboBoxSupplyName")

        self.horizontalLayout_4.addWidget(self.comboBoxSupplyName)

        self.comboBoxModel = QComboBox(self.groupBoxResult)
        self.comboBoxModel.setObjectName(u"comboBoxModel")
        self.comboBoxModel.setMinimumSize(QSize(90, 0))
        self.comboBoxModel.setToolTipDuration(1)
        self.comboBoxModel.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_4.addWidget(self.comboBoxModel)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.groupBoxResult)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label)

        self.doubleSpinBoxTemperature = QDoubleSpinBox(self.groupBoxResult)
        self.doubleSpinBoxTemperature.setObjectName(u"doubleSpinBoxTemperature")
        self.doubleSpinBoxTemperature.setMaximum(1.000000000000000)
        self.doubleSpinBoxTemperature.setSingleStep(0.050000000000000)

        self.horizontalLayout_5.addWidget(self.doubleSpinBoxTemperature)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.pushButtonGenerateResult = QPushButton(self.groupBoxResult)
        self.pushButtonGenerateResult.setObjectName(u"pushButtonGenerateResult")

        self.verticalLayout_5.addWidget(self.pushButtonGenerateResult)

        self.pushButtonLoadQueryInfo = QPushButton(self.groupBoxResult)
        self.pushButtonLoadQueryInfo.setObjectName(u"pushButtonLoadQueryInfo")

        self.verticalLayout_5.addWidget(self.pushButtonLoadQueryInfo)

        self.pushButtonSaveQueryInfo = QPushButton(self.groupBoxResult)
        self.pushButtonSaveQueryInfo.setObjectName(u"pushButtonSaveQueryInfo")

        self.verticalLayout_5.addWidget(self.pushButtonSaveQueryInfo)

        self.pushButtonCopyResult = QPushButton(self.groupBoxResult)
        self.pushButtonCopyResult.setObjectName(u"pushButtonCopyResult")

        self.verticalLayout_5.addWidget(self.pushButtonCopyResult)

        self.pushButtonSendPrompt = QPushButton(self.groupBoxResult)
        self.pushButtonSendPrompt.setObjectName(u"pushButtonSendPrompt")

        self.verticalLayout_5.addWidget(self.pushButtonSendPrompt)


        self.horizontalLayout_14.addLayout(self.verticalLayout_5)


        self.horizontalLayout_13.addWidget(self.groupBoxResult)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_13)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)


        self.verticalLayout.addWidget(self.groupBoxOutPut)


        self.horizontalLayout_17.addLayout(self.verticalLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Dialog)

        self.tabWidgetExamples.setCurrentIndex(0)
        self.tabWidgetPrompt.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Generate Code from Examples", None))
        self.groupBoxExamples.setTitle(QCoreApplication.translate("Dialog", u"Examples", None))
        self.tabWidgetExamples.setTabText(self.tabWidgetExamples.indexOf(self.tabExample1), QCoreApplication.translate("Dialog", u"Tab 1", None))
        self.tabWidgetExamples.setTabText(self.tabWidgetExamples.indexOf(self.tabExample2), QCoreApplication.translate("Dialog", u"Example 2", None))
        self.pushButtonClearExample.setText(QCoreApplication.translate("Dialog", u"Clear Current", None))
        self.pushButtonDeleteExample.setText(QCoreApplication.translate("Dialog", u"Delete Example", None))
        self.pushButtonNewExample.setText(QCoreApplication.translate("Dialog", u"New Example", None))
        self.groupBoxPrompt.setTitle(QCoreApplication.translate("Dialog", u"Prompt", None))
        self.tabWidgetPrompt.setTabText(self.tabWidgetPrompt.indexOf(self.tab), QCoreApplication.translate("Dialog", u"Tab 1", None))
        self.tabWidgetPrompt.setTabText(self.tabWidgetPrompt.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"Tab 2", None))
        self.pushButtonClearPrompt.setText(QCoreApplication.translate("Dialog", u"Clear Current", None))
        self.pushButtonDeletePrompt.setText(QCoreApplication.translate("Dialog", u"Delete Prompt", None))
        self.pushButtonNewPrompt.setText(QCoreApplication.translate("Dialog", u"New Prompt", None))
        self.groupBoxOutPut.setTitle(QCoreApplication.translate("Dialog", u"Result", None))
        self.labelUsedToken.setText(QCoreApplication.translate("Dialog", u"Used token amount: ", None))
        self.lineEditTokenAmount.setText("")
        self.labelEstimateCost.setText(QCoreApplication.translate("Dialog", u"Estimate cost: ", None))
        self.labelRealCost.setText(QCoreApplication.translate("Dialog", u"Real cost: ", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Total cost: ", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Historical cost: ", None))
        self.groupBoxResult.setTitle(QCoreApplication.translate("Dialog", u"Result operation", None))
#if QT_CONFIG(tooltip)
        self.comboBoxModel.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.comboBoxModel.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label.setText(QCoreApplication.translate("Dialog", u"Temperature: ", None))
        self.pushButtonGenerateResult.setText(QCoreApplication.translate("Dialog", u"Generate", None))
        self.pushButtonLoadQueryInfo.setText(QCoreApplication.translate("Dialog", u"Load Data", None))
        self.pushButtonSaveQueryInfo.setText(QCoreApplication.translate("Dialog", u"Save Data", None))
        self.pushButtonCopyResult.setText(QCoreApplication.translate("Dialog", u"Copy result", None))
        self.pushButtonSendPrompt.setText(QCoreApplication.translate("Dialog", u"Send to Prompt", None))
    # retranslateUi

