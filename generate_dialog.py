# -*- coding: utf-8 -*-
# author: CasinoHe
# Purpose:
#    Create a GUI dialog to generate code, So it's easy to use

# using PyQt6 to create a GUI dialog
from PyQt6.QtWidgets import QDialog, QMessageBox, QFileDialog, QApplication
from PyQt6.QtCore import QTimer 
from PyQt6 import QtGui
from PyQt6 import uic
from ui import generate_dialog_ui
import threading
import example_tab
import json

class GenerateCodeDialog(QDialog):
    '''
    GenerateCodeDialog is a dialog that provice convinient way to generate code
    the dialog is divided into 3 parts:
        1. select example file
        2. select prompt file
        3. select models, and set parameters, generate code
    '''
    def __init__(self, llm_interface, parent=None):
        super(GenerateCodeDialog, self).__init__(parent)

        # load ui file
        self.ui = generate_dialog_ui.Ui_Dialog()
        self.ui.setupUi(self)

        self.example_tabs = []
        self.llm_interface = llm_interface
        self.result_content = []
        self.result_index = 0
        self.result_update_timer = QTimer(self)
        self.result_update_mutex = threading.Lock()
        self.result_completed = False
        self.initUI()

    def initUI(self):
        # init the exmpale file part
        self.initTabWidgetExamples()
        # init the prompt file part
        self.initPromptGroup()
        # init the genereate code part
        self.initGenerateCodeGroup()

    def initTabWidgetExamples(self):
        # init example tab
        # first, delete the default tab, there is two default tabs
        self.ui.tabWidgetExamples.removeTab(1)
        self.ui.tabWidgetExamples.removeTab(0)

        # lambda callback function to call onSelectedExampleFile
        open_example_callback = lambda: self.onSelectedExampleFile()
        # then, add example tabs
        self.example_tabs.append(example_tab.ExampleTab(open_example_callback, self))
        self.ui.tabWidgetExamples.addTab(self.example_tabs[0], "Example {}".format(len(self.example_tabs)))

        # connect signals and slots
        self.ui.pushButtonNewExample.clicked.connect(self.clickAddExampleTab)
        # connect delete button
        self.ui.pushButtonDeleteExample.clicked.connect(self.clickDeleteExampleTab)
        # connect clear example button
        self.ui.pushButtonClearExample.clicked.connect(self.clickClearExampleTab)

        # disable new example button first, because there is no file selected
        self.ui.pushButtonNewExample.setEnabled(False)

    def clickClearExampleTab(self):
        # get active tab index
        tab_index = self.ui.tabWidgetExamples.currentIndex()
        # if tab_index is not 0, or there is other tab exist, do not clear
        if tab_index != 0 or len(self.example_tabs) > 1:
            QMessageBox.warning(self, "Warning", "Please delete the tab first")
            return
        self.example_tabs[tab_index].clear()

    def clickAddExampleTab(self):
        # lambda callback function to call onSelectedExampleFile
        open_example_callback = lambda: self.onSelectedExampleFile()
        self.example_tabs.append(example_tab.ExampleTab(open_example_callback, self))
        self.ui.tabWidgetExamples.addTab(self.example_tabs[-1], "Example {}".format(len(self.example_tabs)))
        # change tab to the new tab
        self.ui.tabWidgetExamples.setCurrentIndex(len(self.example_tabs) - 1)

        # disable new example button first, because there is no file selected
        self.ui.pushButtonNewExample.setEnabled(False)

    def clickDeleteExampleTab(self):
        # if there is only one tab, send a warning message to user and return
        if len(self.example_tabs) <= 1:
            QMessageBox.warning(self, "Warning", "There is only one example tab, can't delete it")
            return
        # get active tab index
        tab_index = self.ui.tabWidgetExamples.currentIndex()
        self.ui.tabWidgetExamples.removeTab(tab_index)
        self.example_tabs.pop(tab_index)
        # update tab index
        for i in range(len(self.example_tabs)):
            self.ui.tabWidgetExamples.setTabText(i, "Example {}".format(i + 1))

    def onSelectedExampleFile(self):
        # enable new example button
        self.ui.pushButtonNewExample.setEnabled(True)

    def initPromptGroup(self):
        # disable the file line edit first
        self.ui.lineEditPrompt.setEnabled(False)

        # disable refresh button first, because there is no file selected
        self.ui.pushButtonRefreshPrompt.setEnabled(False)

        # connect signals and slots
        self.ui.pushButtonOpenPromptFile.clicked.connect(self.clickOpenPromptFile)
        self.ui.pushButtonRefreshPrompt.clicked.connect(self.clickRefreshPrompt)
        self.ui.pushButtonClearPrompt.clicked.connect(self.clickClearPrompt)

    def clickOpenPromptFile(self):
        # use QFileDialog to select a prompt file
        prompt_file, _ = QFileDialog.getOpenFileName(self, "Open Prompt File", "", "Text Files (*.txt)")
        if prompt_file:
            self.ui.lineEditPrompt.setText(prompt_file)
            # enable refresh button
            self.ui.pushButtonRefreshPrompt.setEnabled(True)

            # read file content and show it in PlainTextEdit
            with open(prompt_file, "r", encoding='utf-8') as f:
                self.ui.plainTextEditPrompt.setPlainText(f.read())

    def clickRefreshPrompt(self):
        # read file content and show it in PlainTextEdit
        with open(self.ui.lineEditPrompt.text(), "r", encoding='utf-8') as f:
            self.ui.plainTextEditPrompt.setPlainText(f.read())

    def clickClearPrompt(self):
        self.ui.plainTextEditPrompt.clear()

    def initGenerateCodeGroup(self):
        # connect signals and slots
        self.ui.pushButtonGenerateResult.clicked.connect(self.clickGenerateResult)
        # connect save info button
        self.ui.pushButtonSaveQueryInfo.clicked.connect(self.clickSaveInfo)
        # connect load info button
        self.ui.pushButtonLoadQueryInfo.clicked.connect(self.clickLoadInfo)
        # connect copy result button
        self.ui.pushButtonCopyResult.clicked.connect(self.clickCopyResult)

        # we cannot modify the result, so we disable the result plain text edit
        self.ui.plainTextEditResult.setReadOnly(True)

        self.initModelComboBox()

    def initModelComboBox(self):
        # get model list from llm interface
        model_list = self.llm_interface.get_models_name()

        # because we need to access web interface to get model list, so we need a asynchroneous function
        if not model_list:
            # if we cannot get model list, we use a timer to check the model list
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.initModelComboBox)
            self.timer.start(1000)
            # invalid the combobox
            self.ui.comboBoxModel.setEnabled(False)
            return
        else:
            # enable the combobox
            self.ui.comboBoxModel.setEnabled(True)
            self.timer.stop()

        # add model list to combobox
        self.ui.comboBoxModel.addItems(model_list)

    def clickCopyResult(self):
        # copy the text in plainTextEditResult to clipboard
        text = self.ui.plainTextEditResult.toPlainText()
        if text:
            # call system clipboard
            clipboard = QApplication.clipboard()
            clipboard.setText(text)
            # show a message box to user
            QMessageBox.information(self, "Copy Result", "Copy result to clipboard successfully!")

    def clickSaveInfo(self):
        '''save all info to a json file, so we can use it to generate code again'''
        # open a file dialog to select a file
        save_file, _ = QFileDialog.getSaveFileName(self, "Save Query Info", "", "Json Files (*.json)")
        if not save_file:
            return

        # get parameters
        save_info = {}

        # build example info
        example_info = []
        self._packExampleInfo(example_info)
        prompt_info = {}
        self._packPromptInfo(prompt_info)
        generate_info = {}
        self._packGenerateInfo(generate_info)

        save_info["examples"] = example_info
        save_info["prompt"] = prompt_info
        save_info["generate"] = generate_info

        # if there is result, then save the result
        result = self.ui.plainTextEditResult.toPlainText()
        if result: 
            save_info["result"] = result

        # save to file
        with open(save_file, "w", encoding='utf-8') as f:
            json.dump(save_info, f, indent=4)

    def _packExampleInfo(self, example_info):
        # get examples's content
        for example_tab in self.example_tabs:
            single_exmaple_info = {
                "file": example_tab.getExampleFile(),
                "content": example_tab.getExampleContent()
            }
            example_info.append(single_exmaple_info)
    
    def _packPromptInfo(self, prompt_info):
        # get prompt
        prompt = self.ui.plainTextEditPrompt.toPlainText()
        prompt_file = self.ui.lineEditPrompt.text()
        prompt_info["file"] = prompt_file
        prompt_info["content"] = prompt

    def _packGenerateInfo(self, generate_info):
        # get model
        model = self.ui.comboBoxModel.currentText()
        # get temperature
        temperature = self.ui.doubleSpinBoxTemperature.value()
        generate_info["model"] = model
        generate_info["temperature"] = temperature

    def clickLoadInfo(self):
        '''load all info from a json file'''
        # open a file dialog to select a file
        load_file, _ = QFileDialog.getOpenFileName(self, "Load Query Info", "", "Json Files (*.json)")
        if not load_file:
            return

        # load json file
        with open(load_file, "r", encoding='utf-8') as f:
            load_info = json.load(f)

        # set parameters
        example_info = load_info["examples"]
        self._unpackExampleInfo(example_info)

        prompt_info = load_info["prompt"]
        self._unpackPromptInfo(prompt_info)

        generate_info = load_info["generate"]
        self._unpackGenerateInfo(generate_info)

        result_info = load_info.get("result", None)
        if result_info:
            self._unpackResultInfo(result_info)

    def _unpackExampleInfo(self, exmaple_info):
        # load example info from a json file
        # first, set example tab data
        for index in range(len(exmaple_info)):
            if index >= len(self.example_tabs):
                self.clickAddExampleTab()
            self.example_tabs[index].setExampleFile(exmaple_info[index]["file"])
            self.example_tabs[index].setExampleContent(exmaple_info[index]["content"])
        # second, remove extra example tab
        for index in range(len(exmaple_info), len(self.example_tabs)):
            self.clickDeleteExampleTab()

    def _unpackPromptInfo(self, prompt_info):
        # load prompt info from a json file
        self.ui.lineEditPrompt.setText(prompt_info["file"])
        self.ui.plainTextEditPrompt.setPlainText(prompt_info["content"])

    def _unpackGenerateInfo(self, generate_info):
        # load generate info from a json file
        model = generate_info["model"]
        temperature = generate_info["temperature"]
        self.ui.doubleSpinBoxTemperature.setValue(temperature)

        # because there are already some models in combobox, so we need to find the model index
        model_index = self.ui.comboBoxModel.findText(model)
        if model_index != -1:
            self.ui.comboBoxModel.setCurrentIndex(model_index)
        else:
            # insert the model as the first item
            self.ui.comboBoxModel.insertItem(0, model)

    def _unpackResultInfo(self, result_info):
        # load result info from a json file
        self.ui.plainTextEditResult.setPlainText(result_info)

    def clickGenerateResult(self):
        # get parameters
        # get model
        model = self.ui.comboBoxModel.currentText()
        # get temperature
        temperature = self.ui.doubleSpinBoxTemperature.value()

        # get examples's content
        examples = []
        for example_tab in self.example_tabs:
            examples.append(example_tab.getExampleContent())

        # get prompt
        prompt = self.ui.plainTextEditPrompt.toPlainText()

        # init generate result environment
        self.initGenerateResult()

        # we need a lambda function to call onGenerateResultAppend
        callback = lambda result: self.onGenerateResultAppend(result)
        # send request to llm interface
        self.llm_interface.llm_request(model=model, temperature=temperature, examples=examples, prompt=prompt, callback=callback)

    def onGenerateResult(self, result):
        # show result in plainTextEditResult
        self.ui.plainTextEditResult.setPlainText(result)

    def onGenerateResultAppend(self, result):
        # if result is empty, we call onGenerateResultCompleted
        if not result:
            self.result_update_mutex.acquire()
            self.result_completed = True
            self.result_update_mutex.release()
            return

        # to avoid the race condition, we use a timer to update the result
        self.result_update_mutex.acquire()
        self.result_content.append(result)
        self.result_update_mutex.release()

    def onGenerateResultCompleted(self):
        # enable generate button
        self.ui.pushButtonGenerateResult.setEnabled(True)
        self.ui.pushButtonCopyResult.setEnabled(True)
        self.result_update_timer.stop()
        self.result_update_timer.deleteLater()
        self.result_index = 0

    def appendResult(self, result):
        # append result in plainTextEditResult without newline
        text_cursor = QtGui.QTextCursor(self.ui.plainTextEditResult.document())
        text_cursor.movePosition(QtGui.QTextCursor.MoveOperation.End)
        text_cursor.insertText(result)

    def initGenerateResult(self):
        # disable generate button and clear result, copy result button
        self.ui.pushButtonGenerateResult.setEnabled(False)
        self.ui.plainTextEditResult.clear()
        self.ui.pushButtonCopyResult.setEnabled(False)
        self.result_content = []
        self.result_index = 0
        self.result_completed = False
        self.result_update_mutex = threading.Lock()
        self.result_update_timer = QTimer(self)
        self.result_update_timer.timeout.connect(self.onUpdateResultTimeout)
        self.result_update_timer.start(100)

    def onUpdateResultTimeout(self):
        # if result index is not equal to result content length, we append result
        self.result_update_mutex.acquire()
        if self.result_index != len(self.result_content) - 1:
            self.result_index += 1
            for i in range(self.result_index, len(self.result_content)):
                self.appendResult(self.result_content[i])
        if self.result_completed:
            self.onGenerateResultCompleted()
        self.result_update_mutex.release()