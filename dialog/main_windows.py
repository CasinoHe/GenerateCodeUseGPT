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
        '''

        # Settings menu
        self.initGeneratorMenu()
        self.initSettingsMenu()

    def initSettingsMenu(self):
        new_menu = self.ui.menubar.addMenu("Settings")
        new_action = QAction("Open Setting", self)
        new_menu.addAction(new_action)
        new_action.triggered.connect(self.clickSettings)

    def initGeneratorMenu(self):
        new_menu = self.ui.menubar.addMenu("Generator")
        new_action = QAction("Generator with Example", self)
        new_menu.addAction(new_action)
        new_action.triggered.connect(self.clickGeneratorWithExample)

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

        if self.setting_panel is None:
            self.setting_panel = dialog.generator_with_example_dialog.GeneratorWithExampleDialog(self)
        self.setting_panel.show()
        