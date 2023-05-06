# -*- coding: utf-8 -*-
# author: CasinoHe
# Process:
#   1. prepare data in config.json, including example files, prompt file, openai api key
#   2. main.py will read config.json and all examples, prompts, then send request to openai api

from typing import Any
from PyQt6.QtWidgets import QApplication

import generate_dialog
import query_openai

class LLMInterface(object):
    def __init__(self):
        self.model_interface = query_openai.OpenAIUtil("conf.json")

    def get_models_name(self):
        return self.model_interface.get_models_name()

    def llm_request(self, **kwargs):
        return self.model_interface.llm_request(**kwargs)

    def get_estimate_cost(self, **kwargs):
        return self.model_interface.get_estimate_cost(**kwargs)

if __name__ == "__main__":
    # prepare llm interface
    # we need another thread to run the interface, so we can use the GUI
    llm_interface = LLMInterface()

    import sys
    app = QApplication(sys.argv)
    dialog = generate_dialog.GenerateCodeDialog(llm_interface)
    dialog.show()

    sys.exit(app.exec())