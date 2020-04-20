import functools
import inspect
import json


def function_wrapper(func):
    """wrapper for functions that passes the operation to the spool non-blocking"""
    function_name = func.__name__
    stack = inspect.stack()
    widget_class_name = stack[1][0].f_locals["__qualname__"]
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        ret = func(self, *args, **kwargs)
        operation = [self._unique_id, widget_class_name, function_name] + list(args)
        print(operation)
        #TODO Pass the operation off to the spool to be processed
        return ret
    return wrapper

def event_wrapper(func):
    """wrapper for functions that passes the operation to the spool non-blocking"""
    function_name = func.__name__
    stack = inspect.stack()
    widget_class_name = stack[1][0].f_locals["__qualname__"]
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        ret = func(self, *args, **kwargs)
        operation = ["add_signal",
                     self._unique_id,
                     widget_class_name,
                     function_name] + kwargs.get("ret_widget_values", [])
        self.event_callable[function_name] = args[0]
        print(operation)
        #TODO Pass the operation off to the spool to be processed
        return ret
    return wrapper

def return_wrapper(func):
    """wrapper for functions that passes the operation to the spool non-blocking"""
    function_name = func.__name__
    stack = inspect.stack()
    widget_class_name = stack[1][0].f_locals["__qualname__"]
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        ret = func(self, *args, **kwargs)
        self.event_callable[function_name.replace("_return", "")](args[0]["value"])
        #TODO Pass the operation off to the spool to be processed
        return ret
    return wrapper

def init_wrapper(func):
    """wrapper for functions that passes the operation to the spool non-blocking"""
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        ret = func(self, *args, **kwargs)
        init_cmd = self.js_init_call.format(unique_id=self._unique_id,
                                            config=json.dumps(args[0]))
        operation = ["init_widget", init_cmd]
        print(operation)
        #TODO Pass the operation off to the spool to be processed
        return ret
    return wrapper