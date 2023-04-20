# -*- coding: utf-8 -*-
# purpose:
#   a class to access openai's api

import json
import openai
import threading
import number_parser


class OpenAIUtil(object):
    def __init__(self, conf_file):
        self.conf_file = conf_file
        self.open_ai_key = None
        self.thread_pool = []

        self.model_list = []
        self.model_name_list = []
        self.mutex = threading.Lock()
        self.model_init = False

        self.get_open_ai_key()
        self._get_valid_models()

    def get_open_ai_key(self):
        if self.open_ai_key:
            return

        # get the openai key from a json config file, key is 'openai_api_key'
        with open(self.conf_file, 'r') as f:
            conf = json.load(f)
            self.open_ai_key = conf['openai_api_key']
        openai.api_key = self.open_ai_key

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
            model_list = openai.Engine.list()
            self.mutex.acquire()
            self.model_list = model_list
            # save the models name to self.model_name_list
            self.model_name_list = [model['id'] for model in model_list['data']]
            # put the 'gpt-3.5-turbo' the first element in the list
            if 'gpt-3.5-turbo' in self.model_name_list:
                self.model_name_list.remove('gpt-3.5-turbo')
                self.model_name_list.insert(0, 'gpt-3.5-turbo')
            self.mutex.release()
        
        # start a thread to get the models
        t = threading.Thread(target=get_models, args=(self,))
        t.start()
        self.thread_pool.append(t)

    def get_models_name(self):
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

    def llm_request(self, **kwargs):
        # there are many parameters in the request, we need to check them
        # if some parameters are not set, we need to set them
        model = kwargs.get('model', 'gpt-3.5-turbo')
        temperature = kwargs.get('temperature', 0.0)
        prompt = kwargs.get('prompt', '')
        examples = kwargs.get('examples', [])
        callback = kwargs.get('callback', None)

        if not prompt:
            return None

        message = [
            {'role': 'system', 'content': '''You are a professional programmer in our game develop team.'''},
        ]

        if examples:
            message.append({'role': 'user', 'content': '''Here are some examples of our game code:'''})
            index = 0
            for example in examples:
                order = number_parser.parse_ordinal(str(index))
                message.append({'role': 'user', 'content': '''This is {} example, please read it: '''.format(order) + example})
                index += 1
            
        message.append({'role': 'user', 'content': prompt})

        # use the stream to get the response
        # we cannot occupy the main thread for a long time, otherwise the gui or other logic which requires the main thread will be blocked
        def get_response(self, model, temperature, message, callback):
            response = openai.ChatCompletion.create(
                model = model,
                temperature = temperature,
                stream = True,
                messages = message
            )

            for chunk in response:
                # if the response is completed, we need to notify the main thread
                if chunk['choices'][0]['finish_reason'] == 'stop':
                    callback('')
                    return

                chunk_message = chunk['choices'][0]['delta'].get('content', '')

                # if the chunk is empty, we need to continue
                if not chunk_message:
                    continue

                if callback:
                    callback(chunk_message)
                else:
                    print(chunk_message)

        # start a thread to get the response
        t = threading.Thread(target=get_response, args=(self, model, temperature, message, callback))
        t.start()
        self.thread_pool.append(t)

    # when delete the object, we need to stop all the threads
    def __del__(self):
        for t in self.thread_pool:
            t.join()
        self.thread_pool = []