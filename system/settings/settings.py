# -*- coding: utf-8 -*-
# Purpose: load, parse and save setting file

import json
import os

class Settings(object):
    def __init__(self):
        super().__init__()

        self.conf_file = ""
        self.open_ai_key = ""
        self.google_palm_key = ""
        self.project_root_dir = ""

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

    def pack_conf(self, conf_json):
        conf_json['openai_api_key'] = self.open_ai_key
        conf_json['google_palm_key'] = self.google_palm_key
        conf_json['project_root_dir'] = self.project_root_dir

    def save_conf(self):
        '''
        save the config json file
        '''
        conf_json = {}
        self.pack_conf(conf_json)
        with open(self.conf_file, 'w', encoding='utf-8') as f:
            json.dump(conf_json, f)

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