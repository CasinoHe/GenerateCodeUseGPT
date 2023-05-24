# -*- coding:utf-8 -*_
# purpose: a windows that based on PyQt6


from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QAction
from ui import generate_windows_ui

class ProductiveAIGCToolWindows(QMainWindow):
    '''
    ProductiveAIGCToolWindows is a windows that based on PyQt6
    '''
    def __init__(self, system_manager, parent=None):
        super(ProductiveAIGCToolWindows, self).__init__(parent)

        # init ui
        self.ui = generate_windows_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setting_panel = None
        self.gen_code_panel = None
        self.system = system_manager

        self.initUI()

        self.checkSettings()

    def initUI(self):
        self.initMenu()

    def initMenu(self):
        '''
        There are several menus in the menu bar:
         1. Settings
         2. Embeddings by AIGC
         3. Generate text module using AIGC
         4. Search text interface by AIGC
         5. Review text interface by AIGC
        '''

        # Settings menu
        self.initReviewMenu()
        self.initGeneratorMenu()
        self.initEmbeddingsMenu()
        self.initSettingsMenu()

    def initSettingsMenu(self):
        new_menu = self.ui.menubar.addMenu("Settings")
        new_action = QAction("Open Setting", self)
        new_menu.addAction(new_action)
        new_action.triggered.connect(self.clickSettings)

    def initGeneratorMenu(self):
        new_menu = self.ui.menubar.addMenu("Generate")
        new_action = QAction("Generate with Example", self)
        new_menu.addAction(new_action)
        new_action.triggered.connect(self.clickGeneratorWithExample)

    def initEmbeddingsMenu(self):
        new_menu = self.ui.menubar.addMenu("Embeddings")
        new_action = QAction("Create Embeddings", self)
        new_menu.addAction(new_action)
        new_action.triggered.connect(self.clickEmbeddings)

    def initReviewMenu(self):
        new_menu = self.ui.menubar.addMenu("Review")
        new_action = QAction("Code Review", self)
        new_menu.addAction(new_action)
        new_action.triggered.connect(self.clickReview)

    def clickReview(self):
        pass

    def clickSettings(self):
        '''
        clickSettings will show a dialog to set the parameters of AIGC
        '''
        import dialog.settings_tab
        if self.setting_panel is None:
            self.setting_panel = dialog.settings_tab.SettingsTab(self)
        self.setting_panel.show()

    def checkSettings(self):
        if self.system.call_settings("InterfaceIsEmpty"):
            self.clickSettings()
            return False

    def clickGeneratorWithExample(self):
        '''
        clickGeneratorWithExample will show a dialog to set the parameters of AIGC
        '''
        import dialog.generator_with_example_dialog

        if self.gen_code_panel is None:
            self.gen_code_panel = dialog.generator_with_example_dialog.GeneratorWithExampleDialog(self)
        else:
            self.gen_code_panel.initModelComboBox()
        self.gen_code_panel.show()
        
    def clickEmbeddings(self):
        '''
        clickEmbeddings will show a dialog to set the parameters of AIGC
        '''
        # import dialog.embedding_dialog

        # if self.setting_panel is None:
        #     self.setting_panel = dialog.embedding_dialog.EmbeddingDialog(self)
        # self.setting_panel.show()
        pass