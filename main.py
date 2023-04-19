# -*- coding: utf-8 -*-
# author: CasinoHe
# Process:
#   1. prepare data in config.json, including example files, prompt file, openai api key
#   2. main.py will read config.json and all examples, prompts, then send request to openai api

from PyQt6.QtWidgets import QApplication

import generate_dialog

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    dialog = generate_dialog.GenerateCodeDialog()
    dialog.show()
    sys.exit(app.exec())