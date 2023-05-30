# Purpose: It's hard to apply claude api, so we make a slack app to chat with Claude

from system.llm import llm_interface
import slack_sdk
import threading
import time


class SlackAppUtil(llm_interface.LLMInterface):
    class LastMessageStatus(object):
        TYPING = 0
        WAITING = 1
        COMPLETED = 2

    def __init__(self, token, claude_id, channel_id):
        super().__init__()

        self.channel_id = channel_id
        self.claude_id = claude_id

        self.last_timestamp = time.time()
        self.at_clause_message = " <@{}>".format(self.claude_id)

        # initialize slack web client
        self.client = slack_sdk.WebClient(token=token)
        self.reply = None
        self.conversation_ts = None
        self.chat_request_thread = None

    def find_conversation(self, channel_name):
        response = self.client.conversations_list()
        for channel in response["channels"]: # type: ignore
            if channel["name"] == channel_name:
                self.channel_id = channel["id"]
                return channel["id"]

    def retreving_history(self, channel_id=None):
        if not channel_id:
            channel_id = self.channel_id
        response = self.client.conversations_history(channel=channel_id)
        if not response:
            return None
        else:
            return response["messages"]  # type: ignore

    def retreving_thread_replies(self, thread_ts, channel_id=None):
        if not channel_id:
            channel_id = self.channel_id
        response = self.client.conversations_replies(channel=channel_id, ts=thread_ts, include_all_metadata=True) # , oldest=str(self.last_timestamp), inclusive=True)
        if not response:
            return False
        else:
            return response["messages"]  # type: ignore

    def get_last_message(self, thread_ts, channel_id=None):
        status = SlackAppUtil.LastMessageStatus.WAITING
        if not channel_id:
            channel_id = self.channel_id
        messages = self.retreving_thread_replies(thread_ts, channel_id)
        if not messages:
            return None, status

        # find the message that sent previously
        found = False
        last_message = None
        # reverse the list, and find the first message that claude sent
        messages.reverse()
        for message in messages:
            # find the first message that claude sent
            if message["user"] == self.claude_id:
                last_message = message["text"]

                if last_message.endswith("Typing…") or last_message.endswith("Typing…_"):
                    status = SlackAppUtil.LastMessageStatus.TYPING
                elif last_message.startswith("&gt; _*Please note:* Claude"):
                    '''
                    claude will send a notice like this, we need to skip it:

                    &gt; _*Please note:* Claude is not skilled at solving math problems._
                    &gt; _See the <https://console.anthropic.com/docs|Claude documentation> for more information._
                    '''
                    continue
                else:
                    status = SlackAppUtil.LastMessageStatus.COMPLETED
            # we need find the first message as the same as the message previousely sent
            elif message["text"] == self.reply["message"]["text"]: # type: ignore
                found = True
                break

        if found:
            return last_message, status
        else:
            return None, status

    def post_message(self, message, threads_ts=None, channel_id=None):
        if not channel_id:
            channel_id = self.channel_id

        # we neet to metion claude in the message
        message += self.at_clause_message

        timeout = 300 # protect the loopless function
        interval = 5
        self.last_timestamp = int(time.time())
        while True:
            self.reply = self.client.chat_postMessage(channel=channel_id, text=message, thread_ts=threads_ts)
            if self.conversation_ts is None:
                self.conversation_ts = self.reply["ts"]

            if not self.reply or not self.reply['ts']:
                # if no reply, send it again
                time.sleep(interval)
                timeout -= interval
                if timeout <= 0:
                    return False
            else:
                # if reply, return
                return True

    def get_claude_reply(self, interval=2):
        # wait and get reply
        timeout = 300
        while True:
            last_message, status = self.get_last_message(self.conversation_ts)
            if status == SlackAppUtil.LastMessageStatus.TYPING:
                time.sleep(interval)
                timeout -= interval
                if timeout <= 0:
                    return "get claude reply timeout!"
                yield last_message 
            elif status == SlackAppUtil.LastMessageStatus.WAITING:
                continue
            elif status == SlackAppUtil.LastMessageStatus.COMPLETED:
                yield last_message
                break
            else:
                return "API Error. Get Claude reply failed!"

    def start_conversation(self, message, channel_id=None):
        if not self.reply:
            return self.post_message(message, channel_id)
        else:
            return self.post_message(message, self.conversation_ts, channel_id)

    def InterfaceGetSupplyName(self):
        return "Slack"

    def InterfaceGetAllModelNames(self):
        return ["claude"]

    def InterfaceChatRequest(self, **kwargs):
        # there are many parameters in the request, we need to check them
        # if some parameters are not set, we need to set them
        model_name = kwargs.get('model', '')  # Google Palm doesn't need model when access the chat api
        prompts = kwargs.get('prompts', '')
        examples = kwargs.get('examples', [])
        callback = kwargs.get('callback', None)
        new_chat = kwargs.get('new_chat', True)

        # if chat is running, wait for it
        if self.chat_request_thread and self.chat_request_thread.is_alive():
            if callback:
                callback("Chat is running, please wait.", self.ReasonCode.FAILED)
            return

        if not prompts:
            if callback:
                callback("No prompts, Generate exit.", self.ReasonCode.FAILED)
            return None

        # if starts new conversation, clear the reply, and find the last prompt
        context = self._getContext(prompts)

        if new_chat:
            self.reply = None
            self.conversation_ts = None
        else:
            examples = []
            prompt = prompts[-1]
            prompts = [prompt]

        def handle_reply(reply, call_func, error_message):
            if reply:
                # send message succeed, then get reply
                for message in self.get_claude_reply():
                    print("get reply: ", message)
                    call_func(message, self.ReasonCode.NEW_REPLY)
                return True
            else:
                call_func(error_message, self.ReasonCode.SUCCESS)
                return False

        def get_response(self, context, examples, prompts, callback):
            index = 1

            # if the message is not sent, send it again
            if new_chat:
                reply = self.start_conversation(context)
                if not handle_reply(reply, callback, "Slack app error, Cannot send message to slack."):
                    return
            
            for example in examples:
                order = self.make_ordinal(index)

                if example['desc']:
                    message = '''This is {} example, the description is: {}, the example is: """{}""", please read it.'''.format(order, example['desc'], example["content"])
                else:
                    message = '''This is {} example, please read it: '''.format(order) + example["content"]
                index += 1

                reply = self.start_conversation(message)
                if not handle_reply(reply, callback, "Sorry, I can't understand you. The reply is None."):
                    return
            
            for prompt in prompts:
                message = prompt["content"] # type: ignore
                reply = self.start_conversation(message)
                if not handle_reply(reply, callback, "Sorry, I can't understand you. The reply is None."):
                    return

            callback("") # type: ignore

        self.chat_request_thread = threading.Thread(target=get_response, args=(self, context, examples, prompts, callback))
        self.chat_request_thread.start()

    def _getContext(self, prompts):
        for prompt in prompts:
            if prompt["system"]:
                context = prompt["system"]
                return context
        return "Suppose you are a programming asistant, please help me at programming."

    def InterfaceEmbeddingRequest(self, **kwargs):
        raise NotImplementedError

    def InterfaceGetEstimateCost(self, **kwargs):
        return 0, 0, 0

    def InterfaceIsValid(self):
        if self.channel_id and self.claude_id:
            return True
        else:
            return False

    def make_ordinal(self, n):
        n = int(n)
        if 11 <= (n % 100) <= 13:
            suffix = 'th'
        else:
            suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
        return str(n) + suffix