# -*- coding -*-
# Purpose: save all prompt and result to database(json file)

import json
import os


class ResultDatabase(object):
    '''
    ResultDatabase is a singleton class, it is used to save all prompt and result to database(json file)'''

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()

    def save_prompt(self, prompt, context, response, filepath):
        save_dict = {
            'prompt': prompt,
            'system': context,
            'response': response
        }
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(save_dict, f, ensure_ascii=False, indent=4)
        return True

    def load_prompt_file(self, filepath):
        if not os.path.exists(filepath):
            return False, False, False

        with open(filepath, 'r', encoding='utf-8') as f:
            load_dict = json.load(f)

        prompt = load_dict.get("prompt", "")
        context = load_dict.get("system", "")
        response = load_dict.get("response", "")

        return prompt, context, response

    def save_generate_result(self, examples, prompts, generators, results, filepath):
        save_dict = {
            "examples": examples,
            "prompts": prompts,
            "generate": generators,
            "results": results
        }

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(save_dict, f, ensure_ascii=False, indent=4)
        return True

    def load_generate_result(self, filepath):
        if not os.path.exists(filepath):
            return False, False, False, False

        with open(filepath, 'r', encoding='utf-8') as f:
            load_dict = json.load(f)

        example = load_dict.get("examples", None)
        prompt = load_dict.get("prompt", None)
        generate = load_dict.get("generate", None)
        result = load_dict.get("result", None)

        return example, prompt, generate, result

    def InterfaceLoadPrompt(self, filepath):
        return self.load_prompt_file(filepath)
    
    def InterfaceLoadResultFile(self, filepath):
        return self.load_generate_result(filepath)

    def InterfaceSavePrompt(self, prompt, context, response, filepath):
        return self.save_prompt(prompt, context, response, filepath)

    def InterfaceSaveResult(self, examples, prompts, generators, results, filepath):
        return self.save_generate_result(examples, prompts, generators, results, filepath)