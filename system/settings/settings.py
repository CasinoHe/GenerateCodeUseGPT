# -*- coding: utf-8 -*-
# Purpose: load, parse and save setting file

import json
import os

class Settings(object):
    '''
    Settings is a singleton class, it is used to load, parse and save setting file
    '''
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        super().__init__()

        self.conf_file = ""
        self.open_ai_key = ""
        self.google_palm_key = ""
        self.project_root_dir = ""
        self.result_json_dir = ""
        self.slack_token = ""
        self.claude_user_id = ""
        self.general_channel_id = ""

        self.init_conf_file()

    def init_conf_file(self):
        '''
        init config file, it not exists, create it
        '''
        # get the path of config.json
        self.conf_file = os.path.join(os.path.dirname(__file__), 'config.json')

        # if file not exists, create it
        if not os.path.exists(self.conf_file):
            with open(self.conf_file, 'w', encoding='utf-8') as f:
                f.write('{}')
        else:
            # read conf file
            with open(self.conf_file, 'r', encoding='utf-8') as f:
                conf = json.load(f)
                # if the conf file is empty, write an empty json to it
                if not conf:
                    with open(self.conf_file, 'w', encoding='utf-8') as f:
                        f.write('{}')
                else:
                    self.unpack_conf(conf)

    def unpack_conf(self, conf_json):
        '''
        unpack the config json file
        '''
        if 'openai_api_key' in conf_json:
            self.open_ai_key = conf_json['openai_api_key']

        if 'google_palm_key' in conf_json:
            self.google_palm_key = conf_json['google_palm_key']

        if 'project_root_dir' in conf_json:
            self.project_root_dir = conf_json['project_root_dir']

        if 'result_json_dir' in conf_json:
            self.result_json_dir = conf_json['result_json_dir']

        if 'slack_token' in conf_json:
            self.slack_token = conf_json['slack_token']

        if 'claude_user_id' in conf_json:
            self.claude_user_id = conf_json['claude_user_id']

        if 'general_channel_id' in conf_json:
            self.general_channel_id = conf_json['general_channel_id']

    def pack_conf(self, conf_json):
        conf_json['openai_api_key'] = self.open_ai_key
        conf_json['google_palm_key'] = self.google_palm_key
        conf_json['project_root_dir'] = self.project_root_dir
        conf_json['result_json_dir'] = self.result_json_dir
        conf_json['slack_token'] = self.slack_token
        conf_json['claude_user_id'] = self.claude_user_id
        conf_json['general_channel_id'] = self.general_channel_id

    def save_conf(self):
        '''
        save the config json file
        '''
        conf_json = {}
        self.pack_conf(conf_json)
        with open(self.conf_file, 'w', encoding='utf-8') as f:
            json.dump(conf_json, f)

    def is_empty(self):
        if self.open_ai_key:
            return False

        if self.google_palm_key:
            return False

        if self.slack_token and self.claude_user_id and self.general_channel_id:
            return False

        return True

    def InterfaceIsEmpty(self):
        '''
        Interface, called outside
        check if the settings is empty
        '''
        return self.is_empty()

    def InterfaceSaveConf(self):
        '''
        Interface, called outside
        save the config json file
        '''
        self.save_conf()

    def InterfaceGetOpenAIKey(self):
        '''
        Interface, called outside
        get the openai key
        '''
        return self.open_ai_key

    def InterfaceGetConfFile(self):
        '''
        Interface, called outside
        get the config file path
        '''
        return self.conf_file

    def InterfaceGetGooglePalmKey(self):
        '''
        Interface, called outside
        get the google palm key
        '''
        return self.google_palm_key

    def InterfaceSetOpenAIKey(self, key):
        '''
        Interface, called outside
        set the openai key
        '''
        self.open_ai_key = key
        self.save_conf()

    def InterfaceSetGooglePalmKey(self, key):
        '''
        Interface, called outside
        set the google palm key
        '''
        self.google_palm_key = key
        self.save_conf()

    def InterfaceSetProjectRootDir(self, dir):
        '''
        Interface, called outside
        set the project root dir
        '''
        self.project_root_dir = dir
        self.save_conf()

    def InterfaceGetProjectRootDir(self):
        '''
        Interface, called outside
        get the project root dir
        '''
        return self.project_root_dir

    def InterfaceSetResultJsonDir(self, dir):
        '''
        Interface, called outside
        set the result json dir
        '''
        self.result_json_dir = dir
        self.save_conf()

    def InterfaceGetResultJsonDir(self):
        '''
        Interface, called outside
        get the result json dir
        '''
        return self.result_json_dir

    def InterfaceSetSlackToken(self, token):
        '''
        Interface, called outside
        set the slack token
        '''
        self.slack_token = token
        self.save_conf()

    def InterfaceSetClaudeUserID(self, id):
        '''
        Interface, called outside
        set the claude user id
        '''
        self.claude_user_id = id
        self.save_conf()

    def InterfaceSetGeneralChannelID(self, id):
        '''
        Interface, called outside
        set the general channel id
        '''
        self.general_channel_id = id
        self.save_conf()

    def InterfaceGetSlackToken(self):
        '''
        Interface, called outside
        get the slack token
        '''
        return self.slack_token

    def InterfaceGetClaudeUserID(self):
        '''
        Interface, called outside
        get the claude user id
        '''
        return self.claude_user_id

    def InterfaceGetGeneralChannelID(self):
        '''
        Interface, called outside
        get the general channel id
        '''
        return self.general_channel_id