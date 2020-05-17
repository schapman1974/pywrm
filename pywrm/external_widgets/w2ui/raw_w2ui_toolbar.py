from uuid import uuid4

from pywrm_decorators.decorators import (function_wrapper,
                                   event_wrapper,
                                   init_wrapper,
                                   return_wrapper)

from pywrm_spool import spooler
from .raw_w2ui_base import W2UIBase


class Toolbar(W2UIBase):
    widget_set = "w2ui"

    def __init__(self, parent, session_id):
        self._unique_id = str(uuid4())
        self.session_id = session_id
        self.parent = parent
        self.widget_type = "Toolbar"
        spooler.add_widget(self.session_id, self._unique_id, self)

        self._resizable = False
        self.event_callable = {}

    @init_wrapper
    def initToolbar(self, config):
        pass

    @function_wrapper("function")
    def add(self, items):
        """Adds a toolbar item or items."""
        pass

    @function_wrapper("function")
    def check(self, id1, id2=None, **kwargs):
        """Checks toolbar item or items with id (visually looks like pressed button)."""
        pass

    @function_wrapper("function")
    def click(self, id, event=None):
        """Called when user clicks on a toolbar item."""
        pass

    @function_wrapper("function")
    def colorClick(self, event):
        """Called when user selects an item from a color picker drop down menu."""
        pass

    @function_wrapper("function")
    def disable(self, id1, id2=None, **kwargs):
        """Disables toolbar item or items with id."""
        pass

    @function_wrapper("function")
    def enable(self, id1, id2=None, **kwargs):
        """Enables toolbar item or items with id."""
        pass

    @function_wrapper("function")
    def get(self, id=None, returnIndex=None):
        """Finds toolbar item with id and returns it or its index."""
        pass

    @function_wrapper("function")
    def getItemHTML(self, item):
        """Generates HTML for the toolbar item."""
        pass

    @function_wrapper("function")
    def hide(self, id1, id2=None, **kwargs):
        """Hides toolbar item or items with id."""
        pass

    @function_wrapper("function")
    def insert(self, before, items):
        """Inserts a toolbar item or items before item with id=before."""
        pass

    @function_wrapper("function")
    def menuClick(self, id, menu_index, event=None):
        """Called when user selects an item from a drop down menu."""
        pass

    @function_wrapper("function")
    def remove(self, id1, id2=None, **kwargs):
        """Removes items from the toolbar."""
        pass

    @function_wrapper("function")
    def scroll(self, direction):
        """Scrolls toolbar items if they overflow."""
        pass

    @function_wrapper("function")
    def set(self, id, item):
        """Finds toolbar item with id and extends it with item object."""
        pass

    @function_wrapper("function")
    def show(self, id1, id2=None, **kwargs):
        """Shows toolbar item or items with id."""
        pass

    @function_wrapper("function")
    def tooltipHide(self, id):
        """Shows tooltip of the item with id."""
        pass

    @function_wrapper("function")
    def tooltipShow(self, id, event=None, forceRefresh=None):
        """Shows tooltip of the item with id."""
        pass

    @function_wrapper("function")
    def uncheck(self, id1, id2=None, **kwargs):
        """Unchecks toolbar item or items with id (visually looks like pressed button)."""
        pass

    @function_wrapper("property")
    def style(self):
        """adds style classes to Toolbar"""
        pass

    @event_wrapper
    def onClick(self, callable, ret_widget_values=[], block_signal = False):
        """Called when toolbar item is clicked."""
        pass

    @return_wrapper
    def onClick_return(self, event, *args, **kwargs):
        pass

