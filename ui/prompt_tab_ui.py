# Form implementation generated from reading ui file 'C:\Users\vipno\Documents\projects\GenerateCodeUseGPT\ui\prompt_tab.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(915, 335)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBoxPrompt = QtWidgets.QGroupBox(parent=Form)
        self.groupBoxPrompt.setObjectName("groupBoxPrompt")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBoxPrompt)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelSystem = QtWidgets.QLabel(parent=self.groupBoxPrompt)
        self.labelSystem.setObjectName("labelSystem")
        self.horizontalLayout_4.addWidget(self.labelSystem)
        self.lineEditPromptSystem = QtWidgets.QLineEdit(parent=self.groupBoxPrompt)
        self.lineEditPromptSystem.setObjectName("lineEditPromptSystem")
        self.horizontalLayout_4.addWidget(self.lineEditPromptSystem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.plainTextEditPrompt = QtWidgets.QPlainTextEdit(parent=self.groupBoxPrompt)
        self.plainTextEditPrompt.setObjectName("plainTextEditPrompt")
        self.verticalLayout_2.addWidget(self.plainTextEditPrompt)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelPromptFilePath = QtWidgets.QLabel(parent=self.groupBoxPrompt)
        self.labelPromptFilePath.setObjectName("labelPromptFilePath")
        self.horizontalLayout_5.addWidget(self.labelPromptFilePath)
        self.lineEditPromptFilePath = QtWidgets.QLineEdit(parent=self.groupBoxPrompt)
        self.lineEditPromptFilePath.setReadOnly(True)
        self.lineEditPromptFilePath.setObjectName("lineEditPromptFilePath")
        self.horizontalLayout_5.addWidget(self.lineEditPromptFilePath)
        self.pushButtonPromptOpen = QtWidgets.QPushButton(parent=self.groupBoxPrompt)
        self.pushButtonPromptOpen.setObjectName("pushButtonPromptOpen")
        self.horizontalLayout_5.addWidget(self.pushButtonPromptOpen)
        self.pushButtonPromptSave = QtWidgets.QPushButton(parent=self.groupBoxPrompt)
        self.pushButtonPromptSave.setObjectName("pushButtonPromptSave")
        self.horizontalLayout_5.addWidget(self.pushButtonPromptSave)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addWidget(self.groupBoxPrompt)
        self.groupBoxResponse = QtWidgets.QGroupBox(parent=Form)
        self.groupBoxResponse.setObjectName("groupBoxResponse")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBoxResponse)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.plainTextEditResponse = QtWidgets.QPlainTextEdit(parent=self.groupBoxResponse)
        self.plainTextEditResponse.setObjectName("plainTextEditResponse")
        self.horizontalLayout_3.addWidget(self.plainTextEditResponse)
        self.horizontalLayout.addWidget(self.groupBoxResponse)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBoxPrompt.setTitle(_translate("Form", "Prompt"))
        self.labelSystem.setText(_translate("Form", "System background :"))
        self.labelPromptFilePath.setText(_translate("Form", "File Path:"))
        self.pushButtonPromptOpen.setText(_translate("Form", "Open"))
        self.pushButtonPromptSave.setText(_translate("Form", "Save"))
        self.groupBoxResponse.setTitle(_translate("Form", "Response"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
