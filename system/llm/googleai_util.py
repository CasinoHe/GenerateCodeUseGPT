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
        self.embedding_models= []
        self.generate_text_models= []
        self.generate_message_models = []
        self.model_name_list = []
        self.request_names_thread = None
        self.chat_request_thread = None
        self.mutex = threading.Lock()
        self._get_valid_models()
    
    def update_palm_api_key(self):
        if not self.palm_api_key:
            return
        palm.configure(api_key=self.palm_api_key)

    def InterfaceIsValid(self):
        return self.palm_api_key is not None and self.model_list
    
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
            try:
                # there maybe some errors when we fetching the model
                # for example, the api cannot be accessed outside the US
                model_list = palm.list_models()
            except Exception as e:
                return
            self.mutex.acquire()
            self.model_list = model_list
            # save the models name to self.model_name_list
            self.generate_text_models= [model.name for model in self.model_list if 'generateText' in model.supported_generation_methods]
            self.embedding_models = [model.name for model in self.model_list if 'embedText' in model.supported_generation_methods]
            self.generate_message_models = [model.name for model in self.model_list if 'generateMessage' in model.supported_generation_methods]
            self.model_name_list = [model.name for model in self.model_list]
            self.mutex.release()
        
        # start a thread to get the models
        self.request_names_thread = threading.Thread(target=get_models, args=(self,))
        self.request_names_thread.start()

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
        self.request_names_thread = None
        self.chat_request_thread = None

    def InterfaceGetEstimateCost(self, **kwargs):
        return 0, 0, 0

    def make_ordinal(self, n):
        n = int(n)
        if 11 <= (n % 100) <= 13:
            suffix = 'th'
        else:
            suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
        return str(n) + suffix

    def InterfaceChatRequest(self, **kwargs):
        # there are many parameters in the request, we need to check them
        # if some parameters are not set, we need to set them
        model_name = kwargs.get('model', '')  # Google Palm doesn't need model when access the chat api
        temperature = kwargs.get('temperature', 0.0)
        prompts = kwargs.get('prompts', '')
        examples = kwargs.get('examples', [])
        callback = kwargs.get('callback', None)

        # if chat is running, wait for it
        if self.chat_request_thread and self.chat_request_thread.is_alive():
            if callback:
                callback("Chat is running, please wait.", self.ReasonCode.FAILED)
            return

        if not prompts:
            if callback:
                callback("No prompts, Generate exit.", self.ReasonCode.FAILED)
            return None

        context = self._getContext(prompts)
        model = palm.get_model(model_name)

        def get_response(self, model, context, temperature, examples, prompts, callback):
            index = 1
            for example in examples:
                order = self.make_ordinal(index)

                if example['desc']:
                    message = '''This is {} example, the description is: {}, the example is: {}'''.format(order, example['desc'], example["content"])
                else:
                    message = '''This is {} example, please read it: '''.format(order) + example["content"]
                index += 1

                reply = palm.chat(context=context, messages=message)
                callback(reply.last, self.ReasonCode.NEW_REPLY) # type: ignore
            
            for prompt in prompts:
                message = prompt["content"] # type: ignore
                reply = palm.chat(messages=message)
                if reply.last is None:
                    callback("Sorry, I can't understand you. The reply is None.", self.ReasonCode.FAILED)
                else:
                    callback(reply.last, self.ReasonCode.NEW_REPLY) # type: ignore

            callback("") # type: ignore

        self.chat_request_thread = threading.Thread(target=get_response, args=(self, model, context, temperature, examples, prompts, callback))
        self.chat_request_thread.start()

    def _getContext(self, prompts):
        for prompt in prompts:
            if prompt["system"]:
                context = prompt["system"]
                return context
        return "You are a professional programmer in our game develop team."