# -*- coding: utf-8 -*-
# Purpose: abstract interface for all aigc api

class LLMInterface(object):
    def __init__(self):
        pass

    def get_models_name(self):
        raise NotImplementedError

    def llm_request(self, **kwargs):
        raise NotImplementedError

    def get_estimate_cost(self, **kwargs):
        raise NotImplementedError