# -*- coding:utf-8 -*_
# purpose: a windows that based on PySide6


from PySide6.QtWidgets import QMainWindow, QFileSystemModel, QMenu
from PySide6.QtGui import QAction
from PySide6.QtCore import QDir, Qt
from ui import generate_windows_ui
import os

class ProductiveAIGCToolWindows(QMainWindow):
    '''
    ProductiveAIGCToolWindows is a windows that based on PySide6
    '''
    def __init__(self, system_manager, parent=None):
        super(ProductiveAIGCToolWindows, self).__init__(parent)

        # init ui
        self.ui = generate_windows_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setting_panel = None
        self.gen_code_panel = None
        self.system = system_manager
        self.result_path = ""
        self.project_path = ""
        self.project_model = None
        self.result_model = None

        self.initUI()

        self.checkSettings()

    def initUI(self):
        self.initMenu()
        self.initResultDirectoryView()
        self.initProjectRootDirectoryView()

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
        self.initProjectRootDirectoryView()
        self.initResultDirectoryView()

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

    def initResultDirectoryView(self):
        result_path = self.system.call_settings("InterfaceGetResultJsonDir")
        if not result_path or os.path.exists(result_path) == False:
            return

        if self.result_path == result_path:
            return
        
        self.result_path = result_path
        tree_view = self.ui.treeViewResultDir
        self.result_model = QFileSystemModel()
        result_dir = QDir(result_path)
        self.result_model.setRootPath(result_dir.absolutePath())
        tree_view.setModel(self.result_model)
        tree_view.setRootIndex(self.result_model.index(result_dir.absolutePath()))
        tree_view.setColumnWidth(0, 200)
        tree_view.setContextMenuPolicy(Qt.CustomContextMenu) # type: ignore
        tree_view.customContextMenuRequested.connect(self.resultDirectoryContextMenu)
        tree_view.doubleClicked.connect(lambda index: self.clickOpenResultFile(index, ""))

    def initProjectRootDirectoryView(self):
        project_path = self.system.call_settings("InterfaceGetProjectRootDir")
        if not project_path or os.path.exists(project_path) == False:
            return

        if self.project_path == project_path:
            return

        self.project_path = project_path
        tree_view = self.ui.treeViewProjectRootDir
        self.project_model = QFileSystemModel()
        project_dir = QDir(project_path)
        self.project_model.setRootPath(project_dir.absolutePath())
        tree_view.setModel(self.project_model)
        tree_view.setRootIndex(self.project_model.index(project_dir.absolutePath()))
        tree_view.setColumnWidth(0, 200)
        tree_view.setContextMenuPolicy(Qt.CustomContextMenu) # type: ignore
        tree_view.customContextMenuRequested.connect(self.projectDirectoryContextMenu)
        tree_view.doubleClicked.connect(lambda index: self.clickOpenProjectFile(index, ""))

    def resultDirectoryContextMenu(self, point):
        index = self.ui.treeViewResultDir.indexAt(point)
        if not index.isValid():
            return

        file_path = self.result_model.filePath(index) # type:ignore 

        menu = QMenu()
        open_action = QAction("Open", self)
        open_action.triggered.connect(lambda index: self.clickOpenResultFile(index, file_path))
        menu.addAction(open_action)
        generate_action = QAction("Load and Generate", self)
        generate_action.triggered.connect(lambda index: self.clickGenerateWithResult(index, file_path))
        menu.addAction(generate_action)
        menu.exec_(self.ui.treeViewResultDir.mapToGlobal(point))

    def openFileOnEditor(self, file_path):
        # clear the text editor
        self.ui.plainTextEdit.clear()
        # get content of the file, and show it in the text editor
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            self.ui.plainTextEdit.setPlainText(content)

    def clickOpenResultFile(self, index, file_path):
        self.openFileOnEditor(file_path)

    def clickGenerateWithResult(self, index, file_path):
        # open generate code panel
        import dialog.generator_with_example_dialog

        if self.gen_code_panel is None:
            self.gen_code_panel = dialog.generator_with_example_dialog.GeneratorWithExampleDialog(self)
        else:
            self.gen_code_panel.initModelComboBox()
        self.gen_code_panel.loadResultFileDirectly(file_path)
        self.gen_code_panel.show()

    def projectDirectoryContextMenu(self, point):
        index = self.ui.treeViewProjectRootDir.indexAt(point)
        if not index.isValid():
            return

        file_path = self.project_model.filePath(index) # type:ignore 

        menu = QMenu()
        open_action = QAction("Open", self)
        open_action.triggered.connect(lambda index: self.clickOpenProjectFile(index, file_path))
        menu.addAction(open_action)
        generate_action = QAction("Generate as example", self)
        generate_action.triggered.connect(lambda index: self.clickGenerateWithExample(index, file_path))
        menu.addAction(generate_action)
        menu.exec_(self.ui.treeViewProjectRootDir.mapToGlobal(point))

    def clickOpenProjectFile(self, index, file_path):
        if not file_path:
            file_path = self.project_model.filePath(index) # type: ignore
        self.openFileOnEditor(file_path)

    def clickGenerateWithExample(self, index, file_path):
        # open generate code panel
        import dialog.generator_with_example_dialog

        if self.gen_code_panel is None:
            self.gen_code_panel = dialog.generator_with_example_dialog.GeneratorWithExampleDialog(self)
        else:
            self.gen_code_panel.initModelComboBox()
        self.gen_code_panel.loadExampleFileDirectly(file_path)
        self.gen_code_panel.show()