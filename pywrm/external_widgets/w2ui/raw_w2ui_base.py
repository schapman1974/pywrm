"""
Base W2UI widget class
"""

from pywrm_decorators.decorators import (function_wrapper,
                                         event_wrapper,
                                         init_wrapper,
                                         return_wrapper)


class W2UIBase(object):
    widget_set = "w2ui"

    @function_wrapper("function")
    def destroy(self):
        pass

    @function_wrapper("function")
    def off(self, otype: str, handler: str = ""):
        pass

    @function_wrapper("function")
    def on(self, otype: str, handler: str):
        pass

    @function_wrapper("function")
    def refresh(self, id: str = ""):
        pass

    @function_wrapper("function")
    def resize(self):
        pass

    @function_wrapper("function")
    def trigger(self, event_data):
        pass

    @event_wrapper
    def onDestroy(self, callable, ret_widget_values=[], block_signal = False):
        pass

    @return_wrapper
    def onDestroy_return(self, event, *args, **kwargs):
        pass

    @event_wrapper
    def onRefresh(self, callable, ret_widget_values=[], block_signal = False):
        pass

    @return_wrapper
    def onRefresh_return(self, event, *args, **kwargs):
        pass

    @event_wrapper
    def onRender(self, callable, ret_widget_values=[], block_signal = False):
        pass

    @return_wrapper
    def onRender_return(self, event, *args, **kwargs):
        pass

    @event_wrapper
    def onResize(self, callable, ret_widget_values=[], block_signal = False):
        pass

    @return_wrapper
    def onResize_return(self, event, *args, **kwargs):
        pass
