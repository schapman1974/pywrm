import functools
import inspect


def function_wrapper(func):
    """wrapper for apicalls that passes in the operation"""
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