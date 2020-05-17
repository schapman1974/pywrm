from uuid import uuid4
from typing import AnyStr, Callable
from functools import singledispatch, update_wrapper

from pywrm_decorators.decorators import (function_wrapper,
                                         event_wrapper,
                                         init_wrapper,
                                         return_wrapper)
from pywrm_spool import spooler

class Layout:
    widget_set = "dhx"

    def __init__(self, parent, session_id):
        self._unique_id = str(uuid4())
        self.session_id = session_id
        self.parent = parent
        self.widget_type = "Layout"
        spooler.add_widget(self.session_id, self._unique_id, self)
        self._resizable = False
        self.event_callable = {}

    @init_wrapper
    def initLayout(self, config, **kwargs):
        pass

    @function_wrapper("attach")
    def attach(self, cell_id, **kwargs):
        """attaches a DHTMLX component into a Layout cell"""
        #TODO This function takes no parameters but should point to a specific cell
        #      We need to figure out how to pass this parameter EX: layout.cell(cell_id).attach(component, config)
        pass

    @function_wrapper("cell_function")
    def attachHTML(self, cell_id, html):
        """adds an HTML content into a dhtmlxLayout cell"""
        pass

    @function_wrapper("cell_function")
    def collapse(self, cell_id):
        """collapses a specified cell"""
        #TODO This function takes no parameters but should point to a specific cell
        #      We need to figure out how to pas this parameter EX: layout.cell(cell_id).collapse()
        pass

    @function_wrapper("cell_function")
    def expand(self, cell_id):
        """expands a collapsed cell"""
        #TODO This function takes no parameters but should point to a specific cell
        #      We need to figure out how to pas this parameter EX: layout.cell(cell_id).expand()
        pass

    @function_wrapper("function")
    def paint(self):
        """repaints Layout on a page"""
        pass

    @function_wrapper("cell_function")
    def hide(self, cell_id):
        """Hide layout cell"""
        pass

    @function_wrapper("cell_function")
    def show(self, cell_id):
        """Show Layout cell on a page"""
        pass

    @function_wrapper("cell_function")
    def toggle(self, cell_id):
        """Toggle hide/show Layout cell on a page"""
        pass

    def resizable(self, resize_bool):
        self._resizable = resize_bool

    @event_wrapper
    def afterAdd(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.LayoutEvents.afterCollapse, [this.id]);"""
        pass

    @return_wrapper
    def afterAdd_return(self, arg: dict, **kwargs):
        pass

    @event_wrapper
    def afterCollapse(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.LayoutEvents.afterCollapse, [this.id]);"""
        pass

    @return_wrapper
    def afterCollapse_return(self, arg: dict, **kwargs):
        pass

    @event_wrapper
    def afterExpand(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.LayoutEvents.afterExpand, [this.id]);"""
        pass

    @return_wrapper
    def afterExpand_return(self, arg: dict, **kwargs):
        pass

    @event_wrapper
    def afterHide(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.LayoutEvents.afterHide, [this.id]);"""
        pass

    @return_wrapper
    def afterHide_return(self, arg: dict, **kwargs):
        pass

    @event_wrapper
    def afterRemove(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.LayoutEvents.afterRemove, [id]);"""
        pass

    @return_wrapper
    def afterRemove_return(self, arg: dict, **kwargs):
        pass

    @event_wrapper
    def afterResizeEnd(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.LayoutEvents.afterResizeEnd, [_this.id]);"""
        pass

    @return_wrapper
    def afterResizeEnd_return(self, arg: dict, **kwargs):
        pass

    @event_wrapper
    def afterShow(self, callable, ret_widget_values: list = [], block_signal: bool = False):
        pass

    @return_wrapper
    def afterShow_return(self, arg: dict, **kwargs):
        pass

    @event_wrapper
    def beforeAdd(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.LayoutEvents.beforeAdd, [config.id])) {"""
        pass

    @return_wrapper
    def beforeAdd_return(self, arg: dict, **kwargs):
        pass

    @event_wrapper
    def beforeCollapse(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.LayoutEvents.beforeCollapse, [this.id])) {"""
        pass

    @return_wrapper
    def beforeCollapse_return(self, arg: dict, **kwargs):
        pass

    @event_wrapper
    def beforeExpand(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.LayoutEvents.beforeExpand, [this.id])) {"""
        pass

    @return_wrapper
    def beforeExpand_return(self, arg: dict, **kwargs):
        pass

    @event_wrapper
    def beforeHide(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.LayoutEvents.beforeHide, [this.id])) {"""
        pass

    @return_wrapper
    def beforeHide_return(self, arg: dict, **kwargs):
        pass

    @event_wrapper
    def beforeRemove(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.LayoutEvents.beforeRemove, [id])) {"""
        pass

    @return_wrapper
    def beforeRemove_return(self, arg: dict, **kwargs):
        pass

    @event_wrapper
    def beforeResizeStart(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.LayoutEvents.beforeResizeStart, [_this.id])) {"""
        pass

    @return_wrapper
    def beforeResizeStart_return(self, arg: dict, **kwargs):
        pass

    @event_wrapper
    def beforeShow(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.LayoutEvents.beforeShow, [this.id])) {"""
        pass

    @return_wrapper
    def beforeShow_return(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.LayoutEvents.beforeShow, [this.id])) {"""
        pass

    @event_wrapper
    def resize(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.LayoutEvents.resize, [_this.id]);"""
        pass

    @return_wrapper
    def resize_return(self, panel_id, *args, **kwargs):
        pass