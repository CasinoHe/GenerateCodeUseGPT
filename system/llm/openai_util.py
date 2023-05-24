# -*- coding: utf-8 -*-
# purpose:
#   a class to access openai's api

from system.llm import llm_interface
import openai
import threading


class OpenAIUtil(llm_interface.LLMInterface):
    def __init__(self, openai_key):
        super().__init__()
        self.open_ai_key = openai_key

        self.request_name_thread = None
        self.request_chat_thread = None
        self.model_list = []
        self.model_name_list = []
        self.mutex = threading.Lock()
        self.model_init = False

        self.update_openai_key()
        self._get_valid_models()

    def update_openai_key(self):
        if not self.open_ai_key:
            return
        openai.api_key = self.open_ai_key

    def InterfaceIsValid(self):
        return self.open_ai_key is not None

    def InterfaceGetSupplyName(self):
        return "OpenAI"

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
            self.model_name_list = [model['id'] for model in model_list['data']] # type: ignore
            # put the 'gpt-3.5-turbo' the first element in the list
            if 'gpt-3.5-turbo' in self.model_name_list:
                self.model_name_list.remove('gpt-3.5-turbo')
                self.model_name_list.insert(0, 'gpt-3.5-turbo')
            self.mutex.release()
        
        # start a thread to get the models
        self.request_name_thread = threading.Thread(target=get_models, args=(self,))
        self.request_name_thread.start()

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

    def InterfaceChatRequest(self, **kwargs):
        # there are many parameters in the request, we need to check them
        # if some parameters are not set, we need to set them
        model = kwargs.get('model', 'gpt-3.5-turbo')
        temperature = kwargs.get('temperature', 0.0)
        prompts = kwargs.get('prompts', '')
        examples = kwargs.get('examples', [])
        callback = kwargs.get('callback', None)

        if self.request_chat_thread and self.request_chat_thread.is_alive():
            if callback is not None:
                callback("The previous request is not completed, please wait.")
                callback("")

        if not prompts:
            if callback:
                callback("No prompts, Generate exit.")
                callback("")
            return None

        messages = self._build_message(prompts, examples)

        # use the stream to get the response
        # we cannot occupy the main thread for a long time, otherwise the gui or other logic which requires the main thread will be blocked
        def get_response(self, model, temperature, message, callback):
            response = openai.ChatCompletion.create(
                model = model,
                temperature = temperature,
                stream = True,
                messages = message,
                # top_p = 1,
                # n = 1,
                # max_tokens = 4096,
                # presence_penalty = 0,
                # frequency_penalty = 0,
            )

            for chunk in response:
                if 'usage' in chunk:
                    print ('usage is :', chunk['usage']) # type: ignore
                # if the response is completed, we need to notify the main thread
                if chunk['choices'][0]['finish_reason'] in ['stop', 'max_tokens', 'timeout', 'length', 'api_call_error']: # type: ignore
                    print("response completed, the result is :{}".format(chunk['choices'][0]['finish_reason'])) # type: ignore
                    callback('')
                    return

                chunk_message = chunk['choices'][0]['delta'].get('content', '') # type: ignore

                # if the chunk is empty, we need to continue
                if not chunk_message:
                    continue

                if callback:
                    callback(chunk_message)
                else:
                    print(chunk_message)

        # start a thread to get the response
        self.request_chat_thread = threading.Thread(target=get_response, args=(self, model, temperature, messages, callback))
        self.request_chat_thread.start()

    # when delete the object, we need to stop all the threads
    def __del__(self):
        self.request_chat_thread = None
        self.request_name_thread = None

    def make_ordinal(self, n):
        n = int(n)
        if 11 <= (n % 100) <= 13:
            suffix = 'th'
        else:
            suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
        return str(n) + suffix

    def _build_message(self, prompts, examples):
        # the system information in the last prompt is the system information send to openai
        system = ""
        # reverse iterate the prompts, we need to get the system information
        for prompt in reversed(prompts):
            system = prompt['system'] # type: ignore
            if system:
                break

        if not system:
            system = '''You are a professional programmer in our game develop team.'''
        messages = [
            {'role': 'system', 'content': system},
        ]

        if examples:
            index = 1
            for example in examples:
                order = self.make_ordinal(index)
                if example['desc']:
                    messages.append({'role': 'user', 'content': '''This is {} example, the description is: {}, the example is: {}'''.format(order, example['desc'], example["content"])}) 
                else:
                    messages.append({'role': 'user', 'content': '''This is {} example, please read it: '''.format(order) + example["content"]})
                index += 1

                if example['response']:
                    messages.append({'role': 'assistant', 'content': example['response']})
            
        for prompt in prompts:
            if not prompt['content']: # type: ignore
                continue
            messages.append({'role': 'user', 'content': prompt['content']}) # type: ignore
            if prompt['response']: # type: ignore
                messages.append({'role': 'assistant', 'content': prompt['response']}) # type: ignore
        return messages

    def InterfaceGetEstimateCost(self, **kwargs):
        model = kwargs.get('model', 'gpt-3.5-turbo')
        prompts = kwargs.get('prompts', '')
        examples = kwargs.get('examples', [])

        messages = self._build_message(prompts, examples)
        estimate_token = self.count_token(messages, model)

        price_dict = {
            'gpt-3.5-turbo': [0.002, 0.002],
            'text-davinci-003': [0.002, 0.002],
            'text-davinci-002': [0.002, 0.002],
            'code-davinci-002': [0.002, 0.002],
            'gpt-4': [0.03, 0.06],
            'gpt-4-0314': [0.03, 0.06], 
            'gpt-4-32k': [0.06, 0.12],
            'gpt-4-32k-0314': [0.06, 0.12],
        }

        prompt_cost = 0
        complete_cost = 0

        if model not in price_dict:
            prompt_cost = 0.002
            complete_cost = 0.002
        else:
            prompt_cost = price_dict[model][0]
            complete_cost = price_dict[model][1]

        return estimate_token, estimate_token * prompt_cost / 1000, estimate_token * complete_cost / 1000

    def count_token(self, messages, model) -> int:
        import tiktoken
        """Returns the number of tokens used by a list of messages."""
        try:
            encoding = tiktoken.encoding_for_model(model)
        except KeyError:
            print("Warning: model not found. Using cl100k_base encoding.")
            encoding = tiktoken.get_encoding("cl100k_base")

        if model == "gpt-3.5-turbo":
            # print("Warning: gpt-3.5-turbo may change over time. Returning num tokens assuming gpt-3.5-turbo-0301.")
            return self.count_token(messages, model="gpt-3.5-turbo-0301")
        elif model == "gpt-4":
            # print("Warning: gpt-4 may change over time. Returning num tokens assuming gpt-4-0314.")
            return self.count_token(messages, model="gpt-4-0314")
        elif model == "gpt-3.5-turbo-0301":
            tokens_per_message = 4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
            tokens_per_name = -1  # if there's a name, the role is omitted
        elif model == "gpt-4-0314":
            tokens_per_message = 3
            tokens_per_name = 1
        else:
            raise NotImplementedError(f"""count_token() is not implemented for model {model}. See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens.""")

        num_tokens = 0
        for message in messages:
            num_tokens += tokens_per_message
            for key, value in message.items():
                num_tokens += len(encoding.encode(value))
                if key == "name":
                    num_tokens += tokens_per_name
        num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
        return num_tokens