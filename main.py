# -*- coding: utf-8 -*-
# author: CasinoHe
# Process:
#   1. prepare data in config.json, including example files, prompt file, openai api key
#   2. main.py will read config.json and all examples, prompts, then send request to openai api

from PyQt6.QtWidgets import QApplication

import dialog.main_windows
import system.manager
import sys

if __name__ == "__main__":
    # init the system
    manager = system.manager.MainManager()

    app = QApplication(sys.argv)
    main_window = dialog.main_windows.ProductiveAIGCToolWindows(manager)
    main_window.show()

    sys.exit(app.exec())