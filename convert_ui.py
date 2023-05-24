# -*- coding: utf-8 -*-
# Purpose: convert .ui file to .py file using pyuic6

import os
import sys
import subprocess

def convert_ui_to_py(ui_file_path, py_file_path):
    '''
    convert .ui file to .py file using pyuic6
    '''
    cmd = 'pyside6-uic {} -o {}'.format(ui_file_path, py_file_path)
    # output some information
    print('convert {} to {}'.format(ui_file_path, py_file_path))
    subprocess.call(cmd, shell=True)

def convert_ui_to_py_recursive(ui_dir_path, py_dir_path):
    '''
    convert .ui file to .py file using pyuic6 recursively
    '''
    for root, dirs, files in os.walk(ui_dir_path):
        for file in files:
            if file.endswith('.ui'):
                ui_file_path = os.path.join(root, file)
                py_file_path = os.path.join(py_dir_path, file.replace('.ui', '_ui.py'))
                convert_ui_to_py(ui_file_path, py_file_path)

if __name__ == '__main__':
    # get ui dir path
    ui_dir_path = os.path.join(os.path.dirname(__file__), 'ui')
    # get py dir path
    py_dir_path = os.path.join(os.path.dirname(__file__), 'ui')
    # convert ui to py
    convert_ui_to_py_recursive(ui_dir_path, py_dir_path)