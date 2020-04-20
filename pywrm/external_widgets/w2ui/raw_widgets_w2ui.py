from uuid import uuid4

from decorators.decorators import (function_wrapper, event_wrapper, init_wrapper)

class W2UIBase(object):
    @function_wrapper
    def destroy(self):
        pass

    @function_wrapper
    def off(self, otype: str, handler: str = ""):
        pass

    @function_wrapper
    def on(self, otype: str, handler: str):
        pass

    @function_wrapper
    def refresh(self, id: str = ""):
        pass

    @function_wrapper
    def resize(self):
        pass

    @function_wrapper
    def trigger(self, event_data):
        pass

class Layout(W2UIBase):
    def __init__(self):
        self._unique_id = str(uuid4())
        self._event_param_qty = {
            "onContent": 1,
            "onHide": 1,
            "onResizerClick": 1,
            "onResizing": 1,
            "onShow": 1,
            "onDestroy": 1,
            "onRefresh": 0,
            "onRender": 1,
            "onResize": 1,
        }
        self.js_init = ""

    @init_wrapper
    def initLayout(self, config):
        pass

    @function_wrapper
    def assignToolbar(self, panel, toolbar):
        pass

    @function_wrapper
    def content(self, type, content, transition):
        pass

    @function_wrapper
    def el(self, type):
        pass

    @function_wrapper
    def get(self, type):
        pass

    @function_wrapper
    def hide(self, panel, immediate):
        pass

    @function_wrapper
    def hideTabs(self, type):
        pass

    @function_wrapper
    def hideToolbar(self, type):
        pass

    @function_wrapper
    def html(self, type, content, transition):
        pass

    @function_wrapper
    def load(self, type, url, transition, onLoad):
        pass

    @function_wrapper
    def lock(self, panel, message, showSpinner):
        pass

    @function_wrapper
    def message(self, panel, msgOptions):
        pass
    
    @function_wrapper
    def set(self, type, panel):
        pass

    @function_wrapper
    def show(self, panel, immediate):
        pass

    @function_wrapper
    def showTabs(self, type):
        pass

    @function_wrapper
    def showToolbar(self, type):
        pass

    @function_wrapper
    def sizeTo(self, type, size, instant):
        pass

    @function_wrapper
    def toggle(self, type, immediate):
        pass

    @function_wrapper
    def toggleToolbar(self, type):
        pass

    @function_wrapper
    def unlock(self, panel):
        pass

    @event_wrapper
    def onContent(self, callable, ret_widget_values=[], block_signal = False):
        pass
    
    @event_wrapper
    def onHide(self, callable, ret_widget_values=[], block_signal = False):
        pass

    @event_wrapper
    def onResizerClick(self, callable, ret_widget_values=[], block_signal = False):
        pass

    @event_wrapper
    def onResizing(self, callable, ret_widget_values=[], block_signal = False):
        pass

    @event_wrapper
    def onShow(self, callable, ret_widget_values=[], block_signal = False):
        pass

    @event_wrapper
    def onDestroy(self, callable, ret_widget_values=[], block_signal = False):
        pass

    @event_wrapper
    def onRefresh(self, callable, ret_widget_values=[], block_signal = False):
        pass

    @event_wrapper
    def onRender(self, callable, ret_widget_values=[], block_signal = False):
        pass

    @event_wrapper
    def onResize(self, callable, ret_widget_values=[], block_signal = False):
        pass