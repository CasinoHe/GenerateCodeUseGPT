# -*- coding: utf-8 -*-
# author: CasinoHe
# Purpose:
#    Create a GUI dialog to generate code, So it's easy to use

# using PySide6 to create a GUI dialog
from PySide6.QtWidgets import QDialog, QMessageBox, QFileDialog, QApplication
from PySide6.QtCore import QTimer, Qt
from PySide6 import QtGui
from ui import generate_dialog_ui
import threading
from dialog import example_tab
from dialog import prompt_tab
import copy
from system.llm import llm_interface


class GeneratorWithExampleDialog(QDialog):
    '''
    GeneratorWithExampleDialog is a dialog that provice convinient way to generate code
    the dialog is divided into 3 parts:
        1. select example file
        2. select prompt file
        3. select models, and set parameters, generate code
    '''
    def __init__(self, parent):
        super().__init__(parent)

        self.system = parent.system

        # load ui file
        self.ui = generate_dialog_ui.Ui_Dialog()
        self.ui.setupUi(self)

        self.example_tabs = []
        self.prompt_tabs = []
        self.result_content = []
        self.result_update_timer = QTimer(self)
        self.result_update_mutex = threading.Lock()
        self.result_completed = False
        self.last_chat_request = None
        self.initUI()
        self.setModal(True)

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

        # get the height of tab widget, if height is less than 300, set it to 350
        tab_widget_height = self.ui.tabWidgetExamples.height()
        if tab_widget_height < 350:
            self.ui.tabWidgetExamples.setFixedHeight(350)

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
        # delete default tab, there is two default tabs
        self.ui.tabWidgetPrompt.removeTab(1)
        self.ui.tabWidgetPrompt.removeTab(0)

        # create new tab
        self.prompt_tabs.append(prompt_tab.PromptTab(self))
        self.ui.tabWidgetPrompt.addTab(self.prompt_tabs[0], "Prompt {}".format(len(self.prompt_tabs)))

        # check the height of group box, if height is less than 350, set it to 350
        group_box_height = self.ui.groupBoxPrompt.height()
        if group_box_height < 350:
            self.ui.groupBoxPrompt.setFixedHeight(350)

        # connect signals and slots
        self.ui.pushButtonNewPrompt.clicked.connect(self.clickAddPromptTab)
        # connect delete button
        self.ui.pushButtonDeletePrompt.clicked.connect(self.clickDeletePromptTab)
        # connect clear prompt button
        self.ui.pushButtonClearPrompt.clicked.connect(self.clickClearPromptTab)

    def clickAddPromptTab(self):
        # if the prompt content in the last tab is empty, do not add new tab
        if self.prompt_tabs[-1].isEmpty():
            QMessageBox.warning(self, "Warning", "Please input the prompt content first")
            return
        self.prompt_tabs.append(prompt_tab.PromptTab(self))
        self.ui.tabWidgetPrompt.addTab(self.prompt_tabs[-1], "Prompt {}".format(len(self.prompt_tabs)))
        # change tab to the new tab
        self.ui.tabWidgetPrompt.setCurrentIndex(len(self.prompt_tabs) - 1)

    def clickDeletePromptTab(self):
        # if there is only one tab, send a warning message to user and return
        if len(self.prompt_tabs) <= 1:
            QMessageBox.warning(self, "Warning", "There is only one prompt tab, can't delete it")
            return
        # get active tab index
        tab_index = self.ui.tabWidgetPrompt.currentIndex()
        self.ui.tabWidgetPrompt.removeTab(tab_index)
        self.prompt_tabs.pop(tab_index)
        # update tab index
        for i in range(len(self.prompt_tabs)):
            self.ui.tabWidgetPrompt.setTabText(i, "Prompt {}".format(i + 1))

    def clickClearPromptTab(self):
        # get active tab index
        tab_index = self.ui.tabWidgetPrompt.currentIndex()
        # if tab_index is 0, or there is other tab exist, do not clear
        if tab_index != 0 or len(self.prompt_tabs) > 1:
            QMessageBox.warning(self, "Warning", "Please delete the tab first")
            return
        self.prompt_tabs[tab_index].clear()

    def initGenerateCodeGroup(self):
        # connect signals and slots
        self.ui.pushButtonGenerateResult.clicked.connect(self.clickGenerateResult)
        # connect save info button
        self.ui.pushButtonSaveQueryInfo.clicked.connect(self.clickSaveInfo)
        # connect load info button
        self.ui.pushButtonLoadQueryInfo.clicked.connect(self.clickLoadInfo)
        # connect supply name combo box change
        self.ui.comboBoxSupplyName.currentIndexChanged.connect(self.changeSupplyName)
        # connect supply name combo box when user click it
        self.ui.comboBoxSupplyName.activated.connect(self.clickSupplyName)
        # connect model name combo box when user click it
        self.ui.comboBoxModel.activated.connect(self.clickModelComboBox)

        self.initModelComboBox()

    def initModelComboBox(self):
        # clear supply name combo box and model combo box, because the api may be changed at runtime
        self.ui.comboBoxModel.clear()
        self.ui.comboBoxSupplyName.clear()

        # get model list from llm interface
        model_dict = self.system.InterfaceGetAllModels()

        # # initialize the timer
        self.timer = None

        # # because we need to access web interface to get model list, so we need a asynchroneous function
        if not model_dict:
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
            if self.timer:
                # stop the timer
                self.timer.stop()

        # get model list
        supplys = list(model_dict.keys())
        supply = supplys[0]
        model_list = model_dict[supply]

        # add model list to combobox
        if model_list:
            self.ui.comboBoxModel.addItems(model_list)

            model = self.ui.comboBoxModel.model()
            for i in range(model.rowCount()):
                hint_text = model.item(i).text() # type: ignore
                model.setData(model.index(i, 0), hint_text, Qt.ToolTipRole) # type: ignore

        self.ui.comboBoxSupplyName.addItems(supplys)
    
    def clickModelComboBox(self):
        # if there is no model's name in models combo box, request the model's name from llm interface
        if self.ui.comboBoxModel.count() > 0:
            return

        self.clickSupplyName()

    def clickSupplyName(self):
        # get supply name
        supply = self.ui.comboBoxSupplyName.currentText()

        # if there is no model's name in models combo box, request the model's name from llm interface
        if self.ui.comboBoxModel.count() > 0:
            return

        # get model list from llm interface
        model_dict = self.system.InterfaceGetAllModels()

        # clear model combobox
        self.ui.comboBoxModel.clear()

        if supply not in model_dict:
            return

        model_list = model_dict[supply]
        # add model list to combobox
        self.ui.comboBoxModel.addItems(model_list)
        
    def changeSupplyName(self, index):
        # get supply name
        supply = self.ui.comboBoxSupplyName.currentText()
        # get model list from llm interface
        model_dict = self.system.InterfaceGetAllModels()

        # clear model combobox
        self.ui.comboBoxModel.clear()

        if supply not in model_dict:
            return
        model_list = model_dict[supply]

        # add model list to combobox
        self.ui.comboBoxModel.addItems(model_list)
        model = self.ui.comboBoxModel.model()
        for i in range(model.rowCount()):
            hint_text = model.item(i).text() # type: ignore
            model.setData(model.index(i, 0), hint_text, Qt.ToolTipRole) # type: ignore

    def clickSaveInfo(self):
        '''save all info to a json file, so we can use it to generate code again'''
        opendir = self.system.call_settings("InterfaceGetResultJsonDir")
        # open a file dialog to select a file
        save_file, _ = QFileDialog.getSaveFileName(self, "Save Query Info", opendir, "Json Files (*.json)")
        if not save_file:
            return

        # build example info
        example_info = []
        self._packExampleInfo(example_info)
        prompt_info = []
        self._packPromptInfo(prompt_info)
        generate_info = {}
        self._packGenerateInfo(generate_info)
        # result is deprecated
        result = ""

        # save file
        save_result = self.system.call_database(
            "InterfaceSaveResult", example_info, prompt_info, generate_info, result, save_file)

        if save_result:
            QMessageBox.information(self, "Save Query Info", "Save query info successfully!")
        else:
            QMessageBox.warning(self, "Save Query Info", "Save query info failed!")

    def _packExampleInfo(self, example_info):
        # get examples's content
        for example_tab in self.example_tabs:
            single_exmaple_info = {
                "file": example_tab.getExampleFile(),
                "content": example_tab.getExampleContent(),
                "desc": example_tab.getExampleDesc(),
                "response": example_tab.getExampleResponse()
            }
            example_info.append(single_exmaple_info)
    
    def _packPromptInfo(self, prompt_info):
        # get all prompts
        for prompt_tab in self.prompt_tabs:
            single_prompt_info = {
                "file": prompt_tab.getPromptFile(),
                "content": prompt_tab.getPromptContent(),
                "system": prompt_tab.getPromptSystem(),
                "response": prompt_tab.getPromptResponse()
            }

            if not single_prompt_info['content'] and not single_prompt_info['response'] and not single_prompt_info['system']:
                continue

            prompt_info.append(single_prompt_info)

    def _packGenerateInfo(self, generate_info):
        # get model
        model = self.ui.comboBoxModel.currentText()
        # get temperature
        temperature = self.ui.doubleSpinBoxTemperature.value()
        supply = self.ui.comboBoxSupplyName.currentText()
        generate_info["supply"] = supply
        generate_info["model"] = model
        generate_info["temperature"] = temperature

    def clickLoadInfo(self):
        '''load all info from a json file'''
        opendir = self.system.call_settings("InterfaceGetResultJsonDir")
        # open a file dialog to select a file
        load_file, _ = QFileDialog.getOpenFileName(self, "Load Query Info", opendir, "Json Files (*.json)")
        if not load_file:
            return

        self.loadResultFileDirectly(load_file)

    def loadResultFileDirectly(self, load_file):
        # load json file
        example_info, prompt_info, generate_info, result_info = self.system.call_database(
            "InterfaceLoadResultFile", load_file)

        if example_info is None:
            QMessageBox.warning(self, "Load Query Info", "Load query info failed!")
            return

        # set parameters
        self._unpackExampleInfo(example_info)
        self._unpackPromptInfo(prompt_info)
        self._unpackGenerateInfo(generate_info)
        self._unpackResultInfo(result_info)

    def _unpackExampleInfo(self, exmaple_info):
        if not exmaple_info:
            return
        # load example info from a json file
        # first, set example tab data
        for index in range(len(exmaple_info)):
            if index >= len(self.example_tabs):
                self.clickAddExampleTab()
            self.example_tabs[index].setExampleFile(exmaple_info[index]["file"])
            self.example_tabs[index].setExampleContent(exmaple_info[index]["content"])
            self.example_tabs[index].setExampleDesc(exmaple_info[index]["desc"])
            self.example_tabs[index].setExampleResponse(exmaple_info[index]["response"])
        # second, remove extra example tab
        for index in range(len(exmaple_info), len(self.example_tabs)):
            self.clickDeleteExampleTab()

        if len(self.example_tabs) > 0:
            # enable new example tab
            self.ui.pushButtonNewExample.setEnabled(True)

    def _unpackPromptInfo(self, prompt_info):
        if not prompt_info:
            return
        # load prompt info from a json file, there maybe an old style prompt info
        # old style is only a dict, new style is a list of dict
        if isinstance(prompt_info, dict):
            # old style, there is only one prompt
            # delete the extra prompt tab
            for index in range(1, len(self.prompt_tabs)):
                self.clickDeletePromptTab()
            # clear the first prompt tab
            # set the active tab to the first tab
            self.ui.tabWidgetPrompt.setCurrentIndex(0)
            self.clickClearPromptTab()

            prompt_tab = self.prompt_tabs[0]
            prompt_tab.setPromptFile(prompt_info["file"])
            prompt_tab.setPromptContent(prompt_info["content"])
            prompt_tab.setPromptSystem(prompt_info["system"])
        else:
            # new style
            # first, set prompt tab data
            for index in range(len(prompt_info)):
                if index >= len(self.prompt_tabs):
                    self.clickAddPromptTab()
                self.prompt_tabs[index].setPromptFile(prompt_info[index]["file"])
                self.prompt_tabs[index].setPromptContent(prompt_info[index]["content"])
                self.prompt_tabs[index].setPromptSystem(prompt_info[index]["system"])
                self.prompt_tabs[index].setPromptResponse(prompt_info[index]["response"])

            # second, remove extra prompt tab
            for index in range(len(prompt_info), len(self.prompt_tabs)):
                self.clickDeletePromptTab()

    def _unpackGenerateInfo(self, generate_info):
        if not generate_info:
            return
        # load generate info from a json file
        supply = generate_info.get("supply", "OpenAI")
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

        # because there are already some supplies in combobox, so we need to find the supply index
        supply_index = self.ui.comboBoxSupplyName.findText(supply)
        if supply_index != -1:
            self.ui.comboBoxSupplyName.setCurrentIndex(supply_index)
        else:
            # insert the supply as the first item
            self.ui.comboBoxSupplyName.insertItem(0, supply)

    def _unpackResultInfo(self, result_info):
        if not result_info:
            return
        # find the last prompt tab
        last_prompt_tab = self.prompt_tabs[-1]
        # set the prompt tab data
        last_prompt_tab.setPromptResponse(result_info)

    def clickGenerateResult(self):
        # get parameters
        # get model
        model = self.ui.comboBoxModel.currentText()
        # get temperature
        temperature = self.ui.doubleSpinBoxTemperature.value()

        # get examples's content
        examples = []
        # if there is only 1 example tab, and the content is empty, then we don't need to send request
        if len(self.example_tabs) > 1 or self.example_tabs[0].getExampleContent():
            for example_tab in self.example_tabs:
                # example element is a dict, with key "content" and "desc"
                element = {
                    "content": example_tab.getExampleContent(),
                    "desc": example_tab.getExampleDesc(),
                    "response": example_tab.getExampleResponse(),
                }
                examples.append(element)

        # get prompt
        prompts = []
        for prompt_tab in self.prompt_tabs:
            # prompt element is a dict, with key "content" and "system"
            element = {
                "content": prompt_tab.getPromptContent(),
                "system": prompt_tab.getPromptSystem(),
                "response": prompt_tab.getPromptResponse(),
            }
            prompts.append(element)

        supply_name = self.ui.comboBoxSupplyName.currentText()
        estimate_token, prompt_cost, complete_cost = self.system.call_llm(supply_name, "InterfaceGetEstimateCost", model=model, examples=examples, prompts=prompts)
        # use confirm message box to confirm the cost
        confirm_message = "This request will cost {} tokens, prompt cost is ${}, estimate of complete cost base on the token amount of prompt is ${}, continue?".format(estimate_token, prompt_cost, complete_cost)
        reply = QMessageBox.question(self, "Confirm", confirm_message, QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.No:
            return

        self.ui.lineEditEstimateCost.setText("$" + str(prompt_cost + complete_cost))
        self.ui.lineEditTokenAmount.setText(str(estimate_token))

        # init generate result environment
        self.initGenerateResult()

        # we need a lambda function to call onGenerateResultAppend
        callback = lambda result, reason = None: self.onGenerateResultAppend(result, reason)

        current_request = {
            "examples": examples,
            "prompts": prompts,
        }
        new_chat = self.isNewChat(self.last_chat_request, current_request)

        # send request to llm interface
        self.system.call_llm(supply_name, "InterfaceChatRequest", model=model, temperature=temperature,
                             examples=examples, prompts=prompts, new_chat=new_chat, callback=callback)

        self.last_chat_request = current_request

    def onGenerateResult(self, result):
        # find the last prompt tab
        last_prompt_tab = self.prompt_tabs[-1]
        # show result in prompt tab's response
        last_prompt_tab.setPromptResponse(result)

    def onGenerateResultAppend(self, result, reason):
        # if result is empty, we call onGenerateResultCompleted
        if not result:
            self.result_update_mutex.acquire()
            self.result_completed = True
            self.result_update_mutex.release()
            return

        self.result_update_mutex.acquire()
        if reason == llm_interface.LLMInterface.ReasonCode.NEW_REPLY:
            self.result_content = []
            # find the last prompt tab
            last_prompt_tab = self.prompt_tabs[-1]
            last_prompt_tab.clearPromptResponse()

        # to avoid the race condition, we use a timer to update the result
        self.result_content.append(result)
        self.result_update_mutex.release()

    def onGenerateResultCompleted(self):
        # enable generate button
        self.ui.pushButtonGenerateResult.setEnabled(True)
        self.ui.pushButtonDeletePrompt.setEnabled(True)
        self.ui.pushButtonClearPrompt.setEnabled(True)
        self.ui.pushButtonNewPrompt.setEnabled(True)
        self.result_update_timer.stop()
        self.result_update_timer.deleteLater()
        self.result_content = []

    def appendResult(self, result):
        # find the last prompt tab
        last_prompt_tab = self.prompt_tabs[-1]
        # show result in prompt tab's response
        last_prompt_tab.appendPromptResponse(result)

    def initGenerateResult(self):
        # find the last prompt tab
        last_prompt_tab = self.prompt_tabs[-1]
        last_prompt_tab.initGenerateResult()
        # disable generate button and clear result, copy result button
        self.ui.pushButtonGenerateResult.setEnabled(False)
        self.ui.pushButtonDeletePrompt.setEnabled(False)
        self.ui.pushButtonClearPrompt.setEnabled(False)
        self.ui.pushButtonNewPrompt.setEnabled(False)
        self.result_content = []
        self.result_completed = False
        self.result_update_mutex = threading.Lock()
        self.result_update_timer = QTimer(self)
        self.result_update_timer.timeout.connect(self.onUpdateResultTimeout)
        self.result_update_timer.start(100)

    def onUpdateResultTimeout(self):
        # if result content is not empty, output to result text edit
        self.result_update_mutex.acquire()
        result_content = []
        if self.result_content:
            result_content = copy.deepcopy(self.result_content)
            self.result_content = []
        self.result_update_mutex.release()

        for content in result_content:
            self.appendResult(content)
        if self.result_completed:
            self.result_update_mutex.acquire()
            for content in self.result_content:
                self.appendResult(content)
            self.onGenerateResultCompleted()
            self.result_update_mutex.release()

    def loadExampleFileDirectly(self, file_path):
        # get example tab
        example_tab = self.example_tabs[-1]
        example_tab.loadExampleFileDirectly(file_path)

    def isNewChat(self, last_chat_request, current_chat_request):

        # if the last chat request is empty, then it is not continouse chat
        if not last_chat_request:
            return True

        # if the current chat request is empty, then it is not continouse chat
        if not current_chat_request:
            return True

        # if the last chat request and current chat request are not the same, then it is not continouse chat
        if len(last_chat_request["examples"]) != len(current_chat_request["examples"]):
            return True

        # compare the last chat request and current chat request
        for index in range(len(last_chat_request["examples"])):
            example = last_chat_request["examples"][index]
            example2 = current_chat_request["examples"][index]

            if example['desc'] != example2['desc']:
                return True
            if example['content'] != example2['content']:
                return True
            if example['response'] != example2['response']:
                return True

        if len(last_chat_request["prompts"]) + 1 != len(current_chat_request["prompts"]):
            return True

        for index in range(len(last_chat_request["prompts"])):
            prompt = last_chat_request["prompts"][index]
            prompt2 = current_chat_request["prompts"][index]

            if prompt['system'] != prompt2['system']:
                return True
            if prompt['content'] != prompt2['content']:
                return True

        # if the last chat request and current chat request are the same, then it is continouse chat
        return False