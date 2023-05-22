# -*- coding: utf-8 -*-
# purpose:
#   a class to access google's aigc api

from system.llm import llm_interface
import google.generativeai as palm
import threading

class GoogleAIUtil(llm_interface.LLMInterface):
    def __init__(self, palm_api_key):
        super().__init__()
        self.palm_api_key = palm_api_key

        self.update_palm_api_key()

        self.model_init = False
        self.model_list = []
        self.embedding_model_names = []
        self.generate_model_names = []
        self.model_name_list = []
        self.thread_pool = []
        self.mutex = threading.Lock()
        self._get_valid_models()
    
    def update_palm_api_key(self):
        if not self.palm_api_key:
            return
        palm.configure(api_key=self.palm_api_key)

    def InterfaceIsValid(self):
        return self.palm_api_key is not None
    
    def InterfaceGetSupplyName(self):
        return "Google"

    def _get_valid_models(self):
        # if we have got the models, we don't need to get them again
        if self.model_init:
            return

        self.model_init = True

        # get the valid models from openai
        # because the access of internet is slow, so we use a thread to get the models
        # and we use a signal to notify the main thread that the models are ready
        # we use a list to store the models, because the thread can't return value
        def get_models(self):
            model_list = palm.list_models()
            self.mutex.acquire()
            self.model_list = model_list
            # save the models name to self.model_name_list
            self.generate_model_names = [model.name for model in self.model_list if 'generateText' in model.supported_generation_methods]
            self.embedding_model_names = [model.name for model in self.model_list if 'embedText' in model.supported_generation_methods]
            self.model_name_list = [model.name for model in self.model_list]
            self.mutex.release()
        
        # start a thread to get the models
        t = threading.Thread(target=get_models, args=(self,))
        t.start()
        self.thread_pool.append(t)

    def InterfaceGetAllModelNames(self):
        # get the models name
        # if the model list is empty, we need to get the models first
        if not self.model_list:
            self._get_valid_models()
        # return the models name, because model_list is a race resource, we need to lock it
        self.mutex.acquire()
        name_list = self.model_name_list
        self.mutex.release()
        return name_list

    def clear_models(self):
        # clear the models
        self.mutex.acquire()
        self.model_list = []
        self.model_name_list = []
        self.mutex.release()

        self.model_init = False

    # when delete the object, we need to stop all the threads
    def __del__(self):
        for t in self.thread_pool:
            t.join()
        self.thread_pool = []

    def InterfaceGetEstimateCost(self, **kwargs):
        return 0, 0, 0

    def InterfaceChatRequest(self, **kwargs):
        return super().InterfaceChatRequest(**kwargs)