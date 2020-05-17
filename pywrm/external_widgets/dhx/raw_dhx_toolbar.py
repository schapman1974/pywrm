from uuid import uuid4
from typing import AnyStr, Callable
from functools import singledispatch, update_wrapper

from pywrm_decorators.decorators import (function_wrapper,
                                         event_wrapper,
                                         init_wrapper,
                                         return_wrapper)
from pywrm_spool import spooler


class Toolbar:
    widget_set = "dhx"

    def __init__(self, parent, session_id):
        self._unique_id = str(uuid4())
        self.session_id = session_id
        self.parent = parent
        self.widget_type = "Toolbar"
        spooler.add_widget(self.session_id, self._unique_id, self)
        self._resizable = False
        self.event_callable = {}

    @init_wrapper
    def initToolbar(self, *args):
        pass

    @function_wrapper("function")
    def destructor(self):
        """removes a Toolbar instance and releases occupied resources"""
        pass

    @function_wrapper("cell_function")
    def disable(self, ids):
        """disables and dims an item(s) of Toolbar"""
        pass
    
    @function_wrapper("cell_function")
    def enable(self, ids):
        """enables a disabled item(s) of Toolbar"""
        pass
    
    @function_wrapper("function")
    def getState(self):
        """gets current values/states of controls"""
        pass

    @function_wrapper("data_function")
    def parse(self, data):
        """Parse config data into toolbar"""
        pass
    
    @function_wrapper("cell_function")
    def hide(self, ids):
        """hides an item of Toolbar"""
        pass
    
    @function_wrapper("cell_function")
    def isDisabled(self, id):
        """checks whether an item of Toolbar is disabled"""
        pass
    
    @function_wrapper("function")
    def paint(self):
        """repaints Toolbar on a page"""
        pass
    
    @function_wrapper("function")
    def setState(self, state_config):
        """sets values/states of controls"""
        pass
    
    @function_wrapper("cell_function")
    def show(self, ids):
        """shows an item of Toolbar"""
        pass
    
    @function_wrapper("property")
    def css(self):
        """adds style classes to Toolbar"""
        pass
    
    @event_wrapper
    def afterHide(self, callable, ret_widget_values=[], block_signal = False):
        """fires after hiding an item of Toolbar"""
        pass

    @event_wrapper
    def afterHide_return(self, event, *args, **kwargs):
        """fires after hiding an item of Toolbar"""
        pass
    
    @event_wrapper
    def beforeHide(self, callable, ret_widget_values=[], block_signal = False):
        """fires before hiding an item of Toolbar"""
        pass

    @return_wrapper
    def beforeHide_return(self, id, event, *args, **kwargs):
        """fires before hiding an item of Toolbar"""
        pass
    
    @event_wrapper
    def click(self, callable, ret_widget_values=[], block_signal = False):
        """fires after a click on a control"""
        pass

    @return_wrapper
    def click_return(self, id, event, *args, **kwargs):
        """fires after a click on a control"""
        pass
    
    @event_wrapper
    def inputBlur(self, callable, ret_widget_values=[], block_signal = False):
        """fires when a control is blurred"""
        pass

    @return_wrapper
    def inputBlur_return(self, id, *args, **kwargs):
        """fires when a control is blurred"""
        pass
    
    @event_wrapper
    def inputCreated(self, callable, ret_widget_values=[], block_signal = False):
        """fires when a new input is added"""
        pass

    @return_wrapper
    def inputCreated_return(self, id, el, *args, **kwargs):
        """fires when a new input is added"""
        pass
    
    @event_wrapper
    def inputFocus(self, callable, ret_widget_values=[], block_signal = False):
        """fires when a control is focused"""
        pass

    @return_wrapper
    def inputFocus_return(self, id, *args, **kwargs):
        """fires when a control is focused"""
        pass
    
    @event_wrapper
    def openMenu(self, callable, ret_widget_values=[], block_signal = False):
        """fires on expanding a menu control"""
        pass

    @return_wrapper
    def openMenu_return(self, id, *args, **kwargs):
        """fires on expanding a menu control"""
        pass
