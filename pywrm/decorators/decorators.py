from base64 import b64decode
import functools
import inspect
import json

from pywrm_spool import spooler


def function_wrapper(function_type="function", blocking=False):
    """wrapper for functions that passes the operation to the spool non-blocking"""
    def inner_function(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            function_name = func.__name__
            ret = func(self, *args, **kwargs)
            cell_id = ""
            if function_type == "cell_function":
                cell_id = args[0]
                args = args[1:]
            operation={
                "type": function_type,
                "widget_id": self._unique_id,
                "widget_type": self.widget_type,
                "function_name": function_name,
                "cell_id": cell_id,
                "args": list(args),
                "kwargs": kwargs,
                "widget_set": self.widget_set,
            }
            spooler.add_item(self.session_id, operation)
            return ret
        return wrapper
    return inner_function

def event_wrapper(func):
    """wrapper for functions that passes the operation to the spool non-blocking"""
    function_name = func.__name__
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        ret = func(self, *args, **kwargs)
        operation = {
            "type": "add_signal",
            "widget_id": self._unique_id,
            "widget_type": self.widget_type,
            "function_name": function_name,
            "ret_widget_args": kwargs.get("ret_widget_values", []),
            "args": [],
            "widget_set": self.widget_set
        }
        self.event_callable[function_name] = args[0]
        spooler.add_item(self.session_id, operation)
        return ret
    return wrapper

def return_wrapper(func):
    """wrapper for functions that passes the operation to the spool non-blocking"""
    function_name = func.__name__
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        ret = func(self, *args, **kwargs)
        arguments = []
        for arg in args:
            arguments.append(b64decode(arg).decode())
            print(function_name)
            print(self.event_callable)
        self.event_callable[function_name.replace("_return", "")](*arguments)
        return ret
    return wrapper

def init_wrapper(func):
    """wrapper for functions that passes the operation to the spool non-blocking"""
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        ret = func(self, *args, **kwargs)
        operation = ["init_widget", self._unique_id, self.widget_type] + list(args)
        operation={
            "type":"init_widget",
            "widget_id": self._unique_id,
            "widget_type": self.widget_type,
            "function_name": "init_main",
            "args": list(args),
            "widget_set": self.widget_set
        }
        spooler.add_item(self.session_id, operation)
        return ret
    return wrapper

def spool_wrapper(session_id):
    print("SESSIONID", session_id)
    def inner_function(func):
        """ Wrapper for spool functions to deal with completion of spool """
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            _ = func(self, *args, **kwargs)
            spooler.add_item(session_id, {"type":"done"})
        return wrapper
    return inner_function