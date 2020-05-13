from uuid import uuid4

from pywrm_decorators.decorators import (function_wrapper,
                                   event_wrapper,
                                   init_wrapper,
                                   return_wrapper)

from pywrm_spool import spooler

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

class Layout(W2UIBase):
    widget_set = "w2ui"

    def __init__(self, parent, session_id):
        self._unique_id = str(uuid4())
        self.session_id = session_id
        self.parent = parent
        self.widget_type = "Layout"
        spooler.add_widget(self.session_id, self._unique_id, self)
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

        self._resizable = False
        self.event_callable = {}

    @init_wrapper
    def initLayout(self, config):
        pass

    @function_wrapper("function")
    def assignToolbar(self, panel, toolbar):
        pass

    @function_wrapper("function")
    def content(self, cell_id, **kwargs):
        pass

    @function_wrapper("function")
    def el(self, type):
        pass

    @function_wrapper("function")
    def get(self, type):
        pass

    @function_wrapper("function")
    def hide(self, panel_id, immediate=False):
        pass

    @function_wrapper("function")
    def hideTabs(self, type):
        pass

    @function_wrapper("function")
    def hideToolbar(self, type):
        pass

    @function_wrapper("function")
    def html(self, type, content, transition=""):
        pass

    @function_wrapper("function")
    def load(self, type, url, transition, onLoad):
        pass

    @function_wrapper("function")
    def lock(self, panel, message, showSpinner):
        pass

    @function_wrapper("function")
    def message(self, panel, msgOptions):
        pass
    
    @function_wrapper("function")
    def set(self, type, panel):
        pass

    @function_wrapper("function")
    def show(self, panel, immediate=False):
        pass

    @function_wrapper("function")
    def showTabs(self, type):
        pass

    @function_wrapper("function")
    def showToolbar(self, type):
        pass

    @function_wrapper("function")
    def sizeTo(self, type, size, instant):
        pass

    @function_wrapper("function")
    def toggle(self, type, immediate):
        pass

    @function_wrapper("function")
    def toggleToolbar(self, type):
        pass

    @function_wrapper("function")
    def unlock(self, panel_id):
        pass

    @event_wrapper
    def onContent(self, callable, ret_widget_values=[], block_signal = False):
        pass

    @return_wrapper
    def onContent_return(self, event, *args, **kwargs):
        pass
    
    @event_wrapper
    def onHide(self, callable, ret_widget_values=[], block_signal = False):
        pass

    @return_wrapper
    def onHide_return(self, event, *args, **kwargs):
        pass

    @event_wrapper
    def onResizerClick(self, callable, ret_widget_values=[], block_signal = False):
        pass

    @return_wrapper
    def onResizerClick_return(self, event, *args, **kwargs):
        pass

    @event_wrapper
    def onResizing(self, callable, ret_widget_values=[], block_signal = False):
        pass

    @return_wrapper
    def onResizing_return(self, event, *args, **kwargs):
        pass

    @event_wrapper
    def onShow(self, callable, ret_widget_values=[], block_signal = False):
        pass

    @return_wrapper
    def onShow_return(self, event, *args, **kwargs):
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