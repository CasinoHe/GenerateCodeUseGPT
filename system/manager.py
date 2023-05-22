# -*- coding: utf-8 -*-

from system.settings import settings

def call_system_decorator(system_name):
    """
    A decorator that calls a method of a system module specified by `system_name` with the keyword arguments `kwargs`.

    Args:
        system_name (str): The name of the system module to call.

    Returns:
        A decorator that wraps methods of the `MainManager` class that call methods of system modules.
    """
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            if func(self) is False:
                return None
            module = getattr(self, system_name)
            if module is None:
                return None

            # if 'func' exists in kwargs, call the function specified by 'func'
            if 'func' not in kwargs or kwargs['func'] is None:
                funcname = args[0]
            # else use the first argument as the function name
            else:
                funcname = kwargs['func']

            if not funcname.startswith('Interface'):
                print("Cannot call system function directly, Please call 'InterfaceXXX' method instead.")
                return None
            execute_func = getattr(module, funcname)
            if execute_func is None:
                return None
            func_kwargs = {k: v for k, v in kwargs.items() if k != 'func'}
            # get args[1:] as the arguments of the function
            return execute_func(*args[1:], **func_kwargs)
        return wrapper
    return decorator


class MainManager(object):
    '''
    MainManager is the main manager of the system.
    It's a singleton class.
    It controls the whole system.
    '''
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()
        self.init_systems()

    def init_systems(self):
        self.settings = settings.Settings()

    @call_system_decorator("settings")
    def call_settings(self, *args, **kwargs):
        return True