from uuid import uuid4
from typing import AnyStr, Callable
from functools import singledispatch, update_wrapper

from pywrm_decorators.decorators import (function_wrapper,
                                         event_wrapper,
                                         init_wrapper,
                                         return_wrapper)
from pywrm_spool import spooler


def overloadmethod(func):
    dispatcher = singledispatch(func)
    def wrapper(*args, **kw):
        return dispatcher.dispatch(args[1].__class__)(*args, **kw)
    wrapper.register = dispatcher.register
    update_wrapper(wrapper, func)
    return wrapper

class Calendar:
    def __init__(self, parent, session_id):
        self._unique_id = str(uuid4())
        self._event_param_qty = {
            "beforeChange": 3,
            "cancelClick": 0,
            "change": 3,
            "dateMouseOver": 2,
            "modeChange": 1,
            "monthSelected": 1,
            "yearSelected": 1,
        }

    @init_wrapper
    def initCalendar(self, config):
        pass

    @function_wrapper
    def setValue(self, value):
        pass

    @function_wrapper
    def getValue(self, asDateObject):
        pass

    @function_wrapper
    def getCurrentMode(self):
        pass

    @function_wrapper
    def showDate(self, date,  mode):
        pass

    @function_wrapper
    def destructor(self):
        pass

    @function_wrapper
    def clear(self):
        pass

    @function_wrapper
    def link(self, targetCalendar):
        pass

    @event_wrapper
    def beforeChange(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.CalendarEvents.beforeChange, [newDate, oldDate, true])) {"""
        pass

    @event_wrapper
    def cancelClick(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def change(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.CalendarEvents.change, [_this._getSelected(), oldDate, true]);"""
        pass

    @event_wrapper
    def dateMouseOver(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.CalendarEvents.dateMouseOver, [new Date(node.attrs._date), event]);"""
        pass

    @event_wrapper
    def modeChange(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.CalendarEvents.modeChange, [types_1.ViewMode.timepicker]);"""
        pass

    @event_wrapper
    def monthSelected(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.CalendarEvents.monthSelected, [date]);"""
        pass

    @event_wrapper
    def yearSelected(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.CalendarEvents.yearSelected, [date]);"""
        pass


class Chart:
    def __init__(self, parent, session_id):
        self._unique_id = str(uuid4())
        self._event_param_qty = {
            "chartMouseLeave": 0,
            "chartMouseMove": 4,
            "resize": 1,
            "serieClick": 2,
            "toggleSeries": 2,
        }

    @init_wrapper
    def initChart(self, config):
        pass

    @function_wrapper
    def getSeries(self, key):
        pass

    @function_wrapper
    def eachSeries(self, handler):
        pass

    @function_wrapper
    def destructor(self):
        pass

    @function_wrapper
    def setConfig(self, config):
        pass

    @event_wrapper
    def chartMouseLeave(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def chartMouseMove(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.ChartEvents.chartMouseMove, [x, y, _this._left + left, _this._top + top]);"""
        pass

    @event_wrapper
    def resize(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.ChartEvents.resize, [{width: _this._width,height: _this._height}]);"""
        pass

    @event_wrapper
    def serieClick(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.ChartEvents.serieClick, [id, value]); }"""
        pass

    @event_wrapper
    def toggleSeries(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.ChartEvents.toggleSeries, [id, pieLike]); }"""
        pass


class Colorpicker:
    def __init__(self, parent, session_id):
        self._unique_id = str(uuid4())
        self._event_param_qty = {
            "apply": 0,
            "cancelClick": 0,
            "change": 1,
            "modeChange": 1,
            "selectClick": 0,
        }

    @init_wrapper
    def initColorpicker(self, config):
        pass

    @function_wrapper
    def destructor(self):
        pass

    @function_wrapper
    def clear(self):
        pass

    @function_wrapper
    def setValue(self, value):
        pass

    @function_wrapper
    def setFocus(self, value):
        pass

    @function_wrapper
    def getValue(self):
        pass

    @function_wrapper
    def getCustomColors(self):
        pass

    @function_wrapper
    def setCustomColors(self, customColors):
        pass

    @function_wrapper
    def setCurrentMode(self, mode):
        pass

    @function_wrapper
    def getCurrentMode(self):
        pass

    @function_wrapper
    def getView(self):
        pass

    @function_wrapper
    def setView(self, mode):
        pass

    @function_wrapper
    def focusValue(self, value):
        pass

    @event_wrapper
    def apply(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def cancelClick(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def change(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.ColorpickerEvents.change, [this._selected]);"""
        pass

    @event_wrapper
    def modeChange(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.ColorpickerEvents.modeChange, [mode]);"""
        pass

    @event_wrapper
    def selectClick(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass


class Combobox:
    def __init__(self, parent, session_id):
        self._unique_id = str(uuid4())
        self._event_param_qty = {
            "afterClose": 0,
            "beforeClose": 0,
            "change": 0,
            "close": 0,
            "input": 1,
            "open": 0,
        }

    @init_wrapper
    def initCombobox(self, config):
        pass

    @function_wrapper
    def focus(self):
        pass

    @function_wrapper
    def enable(self):
        pass

    @function_wrapper
    def disable(self):
        pass

    @function_wrapper
    def isDisabled(self):
        pass

    @function_wrapper
    def clear(self):
        pass

    @function_wrapper
    def getValue(self, asArray):
        pass

    @function_wrapper
    def setValue(self, ids):
        pass

    @function_wrapper
    def destructor(self):
        pass

    @function_wrapper
    def setState(self, state):
        pass

    @event_wrapper
    def afterClose(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def beforeClose(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def change(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def close(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def input(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.ComboboxEvents.input, [value]);"""
        pass

    @event_wrapper
    def open(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass


class DataView:
    def __init__(self, parent, session_id):
        self._unique_id = str(uuid4())
        self._event_param_qty = {
            "afterEditEnd": 2,
            "afterEditStart": 1,
            "beforeEditEnd": 2,
            "beforeEditStart": 1,
            "click": 2,
            "doubleClick": 2,
            "focusChange": 2,
            "itemMouseOver": 2,
            "itemRightClick": 2,
        }

    @init_wrapper
    def initDataView(self, config):
        pass

    @function_wrapper
    def editItem(self, id):
        pass

    @function_wrapper
    def getFocusItem(self):
        pass

    @function_wrapper
    def setItemInRow(self, amount):
        pass

    @function_wrapper
    def setFocus(self, id):
        pass

    @function_wrapper
    def getFocus(self):
        pass

    @function_wrapper
    def destructor(self):
        pass

    @function_wrapper
    def getFocusIndex(self):
        pass

    @function_wrapper
    def setFocusIndex(self, index):
        pass

    @function_wrapper
    def edit(self, id):
        pass

    @event_wrapper
    def afterEditEnd(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.DataViewEvents.afterEditEnd, [value, this._item.id]);"""
        pass

    @event_wrapper
    def afterEditStart(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_2.DataViewEvents.afterEditStart, [id]);"""
        pass

    @event_wrapper
    def beforeEditEnd(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.DataViewEvents.beforeEditEnd, [value, this._item.id])) {"""
        pass

    @event_wrapper
    def beforeEditStart(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_2.DataViewEvents.beforeEditStart, [id])) {"""
        pass

    @event_wrapper
    def click(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_2.DataViewEvents.click, [id, e]);"""
        pass

    @event_wrapper
    def doubleClick(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_2.DataViewEvents.doubleClick, [id, e]);"""
        pass

    @event_wrapper
    def focusChange(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_2.DataViewEvents.focusChange, [this._focusIndex, this.data.getId(this._focusIndex)]);"""
        pass

    @event_wrapper
    def itemMouseOver(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_2.DataViewEvents.itemMouseOver, [id, e]);"""
        pass

    @event_wrapper
    def itemRightClick(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_2.DataViewEvents.itemRightClick, [id, e]);"""
        pass


class Form:
    def __init__(self, parent, session_id):
        self._unique_id = str(uuid4())
        self._event_param_qty = {
            "afterSend": 0,
            "beforeSend": 0,
            "buttonClick": 2,
            "change": 2,
            "validationFail": 2,
        }

    @init_wrapper
    def initForm(self, config):
        pass

    @function_wrapper
    def send(self, url,  method,  asFormData):
        pass

    @function_wrapper
    def clear(self, method):
        pass

    @function_wrapper
    def setValue(self, obj):
        pass

    @function_wrapper
    def getValue(self, asFormData):
        pass

    @function_wrapper
    def getItem(self, id):
        pass

    @function_wrapper
    def validate(self):
        pass

    @function_wrapper
    def getRootView(self):
        pass

    @function_wrapper
    def disable(self):
        pass

    @function_wrapper
    def enable(self):
        pass

    @function_wrapper
    def isDisabled(self, id):
        pass

    @function_wrapper
    def forEach(self, callback):
        pass

    @function_wrapper
    def destructor(self):
        pass

    @function_wrapper
    def setConfig(self, config):
        pass

    @function_wrapper
    def getWidget(self):
        pass

    @event_wrapper
    def afterSend(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def beforeSend(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def buttonClick(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.FormEvents.buttonClick, [id, e]);"""
        pass

    @event_wrapper
    def change(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.FormEvents.change, [name, value]);"""
        pass

    @event_wrapper
    def validationFail(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.FormEvents.validationFail, [id, component]);"""
        pass


class Grid:
    def __init__(self, parent, session_id):
        self._unique_id = str(uuid4())
        self._event_param_qty = {
            "afterEditEnd": 3,
            "afterEditStart": 3,
            "afterKeyDown": 1,
            "afterResizeEnd": 2,
            "beforeEditEnd": 3,
            "beforeEditStart": 3,
            "beforeKeyDown": 1,
            "beforeResizeStart": 2,
            "cellClick": 0,
            "cellDblClick": 0,
            "cellMouseDown": 0,
            "cellMouseOver": 0,
            "cellRightClick": 0,
            "expand": 1,
            "filterChange": 3,
            "footerCellClick": 0,
            "footerCellDblClick": 0,
            "footerCellMouseDown": 0,
            "footerCellMouseOver": 0,
            "footerCellRightClick": 0,
            "headerCellClick": 0,
            "headerCellDblClick": 0,
            "headerCellMouseDown": 0,
            "headerCellMouseOver": 0,
            "headerCellRightClick": 0,
            "resize": 1,
            "scroll": 1,
            "sort": 1,
        }

    @init_wrapper
    def initGrid(self, config):
        pass

    @function_wrapper
    def destructor(self):
        pass

    @function_wrapper
    def setColumns(self, columns):
        pass

    @function_wrapper
    def addRowCss(self, id,  css):
        pass

    @function_wrapper
    def removeRowCss(self, id,  css):
        pass

    @function_wrapper
    def addCellCss(self, row,  col,  css):
        pass

    @function_wrapper
    def removeCellCss(self, row,  col,  css):
        pass

    @function_wrapper
    def showColumn(self, colId):
        pass

    @function_wrapper
    def hideColumn(self, colId):
        pass

    @function_wrapper
    def isColumnHidden(self, colId):
        pass

    @function_wrapper
    def getScrollState(self):
        pass

    @function_wrapper
    def scroll(self, x,  y):
        pass

    @function_wrapper
    def scrollTo(self, row,  col):
        pass

    @function_wrapper
    def adjustColumnWidth(self, id,  adjust):
        pass

    @function_wrapper
    def getCellRect(self, row,  col):
        pass

    @function_wrapper
    def getColumn(self, colId):
        pass

    @function_wrapper
    def addSpan(self, spanObj):
        pass

    @function_wrapper
    def getSpan(self, row,  col):
        pass

    @function_wrapper
    def removeSpan(self, row,  col):
        pass

    @function_wrapper
    def editCell(self, rowId,  colId,  editorType):
        pass

    @function_wrapper
    def editEnd(self, withoutSave):
        pass

    @function_wrapper
    def getSortingState(self):
        pass

    @function_wrapper
    def edit(self, rowId,  colId,  editorType):
        pass

    @event_wrapper
    def afterEditEnd(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.GridEvents.afterEditEnd, [value, this._cell.row, this._cell.col]);"""
        pass

    @event_wrapper
    def afterEditStart(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.GridEvents.afterEditStart, [row, col, editorType]);"""
        pass

    @event_wrapper
    def afterKeyDown(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.GridEvents.afterKeyDown, [e]);"""
        pass

    @event_wrapper
    def afterResizeEnd(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.GridEvents.afterResizeEnd, [col, e]);"""
        pass

    @event_wrapper
    def beforeEditEnd(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.GridEvents.beforeEditEnd, [value, this._cell.row, this._cell.col])) {"""
        pass

    @event_wrapper
    def beforeEditStart(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.GridEvents.beforeEditStart, [row, col, editorType])) {"""
        pass

    @event_wrapper
    def beforeKeyDown(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.GridEvents.beforeKeyDown, [e])) {"""
        pass

    @event_wrapper
    def beforeResizeStart(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.GridEvents.beforeResizeStart, [col, e])) {"""
        pass

    @event_wrapper
    def cellClick(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def cellDblClick(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def cellMouseDown(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def cellMouseOver(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def cellRightClick(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def expand(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.GridEvents.expand, [item]);"""
        pass

    @event_wrapper
    def filterChange(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.GridEvents.filterChange, ["", colId, "comboFilter"]);"""
        pass

    @event_wrapper
    def footerCellClick(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def footerCellDblClick(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def footerCellMouseDown(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def footerCellMouseOver(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def footerCellRightClick(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def headerCellClick(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def headerCellDblClick(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def headerCellMouseDown(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def headerCellMouseOver(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def headerCellRightClick(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def resize(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.GridEvents.resize, [grid.config.columns[i], e]);"""
        pass

    @event_wrapper
    def scroll_event(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.GridEvents.scroll, [{y: e.target.scrollTop,x: e.target.scrollLeft}]);"""
        pass

    @event_wrapper
    def sort(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.GridEvents.sort, [item]);"""
        pass


class Layout:
    widget_set = "dhx"

    def __init__(self, parent, session_id):
        self._unique_id = "L"+str(uuid4()).replace("-", "")
        self.session_id = session_id
        self.parent = parent
        self.widget_type = "Layout"
        spooler.add_widget(self.session_id, self._unique_id, self)
        self._event_param_qty = {
            "afterAdd": 1,
            "afterCollapse": 1,
            "afterExpand": 1,
            "afterHide": 1,
            "afterRemove": 1,
            "afterResizeEnd": 1,
            "afterShow": 0,
            "beforeAdd": 1,
            "beforeCollapse": 1,
            "beforeExpand": 1,
            "beforeHide": 1,
            "beforeRemove": 1,
            "beforeResizeStart": 1,
            "beforeShow": 1,
            "resize": 1,
        }
        self._resizable = False
        self.event_callable = {}

    @init_wrapper
    def initLayout(self, config):
        pass

    @function_wrapper("function")
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


class List:
    def __init__(self, parent, session_id):
        self._unique_id = str(uuid4())
        self._event_param_qty = {
            "afterEditEnd": 2,
            "afterEditStart": 1,
            "beforeEditEnd": 2,
            "beforeEditStart": 1,
            "click": 2,
            "doubleClick": 2,
            "focusChange": 2,
            "itemMouseOver": 2,
            "itemRightClick": 2,
        }

    @init_wrapper
    def initList(self, config):
        pass

    @function_wrapper
    def editItem(self, id):
        pass

    @function_wrapper
    def getFocusItem(self):
        pass

    @function_wrapper
    def setFocus(self, id):
        pass

    @function_wrapper
    def getFocus(self):
        pass

    @function_wrapper
    def destructor(self):
        pass

    @function_wrapper
    def getFocusIndex(self):
        pass

    @function_wrapper
    def setFocusIndex(self, index):
        pass

    @function_wrapper
    def edit(self, id):
        pass

    @event_wrapper
    def afterEditEnd(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.ListEvents.afterEditEnd, [value, this._item.id]);"""
        pass

    @event_wrapper
    def afterEditStart(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_2.ListEvents.afterEditStart, [id]);"""
        pass

    @event_wrapper
    def beforeEditEnd(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.ListEvents.beforeEditEnd, [value, this._item.id])) {"""
        pass

    @event_wrapper
    def beforeEditStart(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_2.ListEvents.beforeEditStart, [id])) {"""
        pass

    @event_wrapper
    def click(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_2.ListEvents.click, [id, e]);"""
        pass

    @event_wrapper
    def doubleClick(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_2.ListEvents.doubleClick, [id, e]);"""
        pass

    @event_wrapper
    def focusChange(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_2.ListEvents.focusChange, [this._focusIndex, this.data.getId(this._focusIndex)]);"""
        pass

    @event_wrapper
    def itemMouseOver(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_2.ListEvents.itemMouseOver, [id, e]);"""
        pass

    @event_wrapper
    def itemRightClick(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_2.ListEvents.itemRightClick, [id, e]);"""
        pass


class Menu:
    def __init__(self, parent, session_id):
        self._unique_id = str(uuid4())
        self._event_param_qty = {
        }

    @init_wrapper
    def initMenu(self, config):
        pass

    @function_wrapper
    def showAt(self, elem,  showAt):
        pass


class Popup:
    def __init__(self, parent, session_id):
        self._unique_id = str(uuid4())
        self._event_param_qty = {
            "afterHide": 1,
            "afterShow": 1,
            "beforeHide": 2,
            "beforeShow": 1,
            "click": 1,
        }

    @init_wrapper
    def initPopup(self, config):
        pass

    @function_wrapper
    def show(self, node,  config,  attached):
        pass

    @function_wrapper
    def hide(self):
        pass

    @function_wrapper
    def isVisible(self):
        pass

    @function_wrapper
    def attach(self, name,  config):
        pass

    @function_wrapper
    def attachHTML(self, html):
        pass

    @function_wrapper
    def getWidget(self):
        pass

    @function_wrapper
    def getContainer(self):
        pass

    @function_wrapper
    def toVDOM(self):
        pass

    @function_wrapper
    def destructor(self):
        pass

    @event_wrapper
    def afterHide(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.PopupEvents.afterHide, [e]);"""
        pass

    @event_wrapper
    def afterShow(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.PopupEvents.afterShow, [node]);"""
        pass

    @event_wrapper
    def beforeHide(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.PopupEvents.beforeHide, [fromOuterClick, e])) {"""
        pass

    @event_wrapper
    def beforeShow(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.PopupEvents.beforeShow, [node])) {"""
        pass

    @event_wrapper
    def click(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.PopupEvents.click, [e]); };"""
        pass


class Ribbon:
    def __init__(self, parent, session_id):
        self._unique_id = str(uuid4())
        self._event_param_qty = {
        }

    @init_wrapper
    def initRibbon(self, config):
        pass

    @function_wrapper
    def getState(self):
        pass

    @function_wrapper
    def setState(self, state):
        pass


class Sidebar:
    def __init__(self, parent, session_id):
        self._unique_id = str(uuid4())
        self._event_param_qty = {
            "afterCollapse": 0,
            "afterExpand": 0,
            "beforeCollapse": 0,
            "beforeExpand": 0,
        }

    @init_wrapper
    def initSidebar(self, config):
        pass

    @function_wrapper
    def toggle(self):
        pass

    @function_wrapper
    def collapse(self):
        pass

    @function_wrapper
    def expand(self):
        pass

    @function_wrapper
    def isCollapsed(self):
        pass

    @event_wrapper
    def afterCollapse(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def afterExpand(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def beforeCollapse(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def beforeExpand(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass


class Slider:
    def __init__(self, parent, session_id):
        self._unique_id = str(uuid4())
        self._event_param_qty = {
            "change": 3,
            "mousedown": 1,
            "mouseup": 1,
        }

    @init_wrapper
    def initSlider(self, config):
        pass

    @function_wrapper
    def disable(self):
        pass

    @function_wrapper
    def enable(self):
        pass

    @function_wrapper
    def isDisabled(self):
        pass

    @function_wrapper
    def focus(self, extra):
        pass

    @function_wrapper
    def getValue(self):
        pass

    @function_wrapper
    def setValue(self, value):
        pass

    @function_wrapper
    def destructor(self):
        pass

    @event_wrapper
    def change(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.SliderEvents.change, [newValue, oldValue, extra]);"""
        pass

    @event_wrapper
    def mousedown(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.SliderEvents.mousedown, [e]);"""
        pass

    @event_wrapper
    def mouseup(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.SliderEvents.mouseup, [e]);"""
        pass


class Tabbar:
    def __init__(self, parent, session_id):
        self._unique_id = str(uuid4())
        self._event_param_qty = {
            "afterClose": 1,
            "beforeClose": 1,
            "change": 2,
        }

    @init_wrapper
    def initTabbar(self, config):
        pass

    @function_wrapper
    def toVDOM(self):
        pass

    @function_wrapper
    def destructor(self):
        pass

    @function_wrapper
    def getWidget(self):
        pass

    @function_wrapper
    def setActive(self, id):
        pass

    @function_wrapper
    def getActive(self):
        pass

    @function_wrapper
    def addTab(self, config,  index):
        pass

    @function_wrapper
    def removeTab(self, id):
        pass

    @function_wrapper
    def disableTab(self, id):
        pass

    @function_wrapper
    def enableTab(self, id):
        pass

    @function_wrapper
    def isDisabled(self, id):
        pass

    @function_wrapper
    def removeCell(self, id):
        pass

    @event_wrapper
    def afterClose(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.TabbarEvents.afterClose, [id]);"""
        pass

    @event_wrapper
    def beforeClose(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.TabbarEvents.beforeClose, [id])) {"""
        pass

    @event_wrapper
    def change(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.TabbarEvents.change, [_this.config.activeView, prev]);"""
        pass


class Timepicker:
    def __init__(self, parent, session_id):
        self._unique_id = str(uuid4())
        self._event_param_qty = {
            "afterClose": 0,
            "apply": 1,
            "beforeClose": 0,
            "change": 1,
            "close": 0,
        }

    @init_wrapper
    def initTimepicker(self, config):
        pass

    @function_wrapper
    def getValue(self, asOBject):
        pass

    @function_wrapper
    def setValue(self, value):
        pass

    @function_wrapper
    def clear(self):
        pass

    @function_wrapper
    def destructor(self):
        pass

    @function_wrapper
    def getRootView(self):
        pass

    @event_wrapper
    def afterClose(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def apply(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.TimepickerEvents.apply, [_this._time]);"""
        pass

    @event_wrapper
    def beforeClose(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def change(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.TimepickerEvents.change, [_this.getValue()]);"""
        pass

    @event_wrapper
    def close(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass


class Toolbar:
    def __init__(self, parent, session_id):
        self._unique_id = str(uuid4())
        self._event_param_qty = {
        }

    @init_wrapper
    def initToolbar(self, config):
        pass

    @function_wrapper
    def getState(self):
        pass

    @function_wrapper
    def setState(self, state):
        pass


class Tree:
    def __init__(self, parent, session_id):
        self._unique_id = str(uuid4())
        self._event_param_qty = {
            "afterCollapse": 1,
            "afterExpand": 1,
            "beforeCollapse": 1,
            "beforeExpand": 1,
            "itemClick": 2,
            "itemDblClick": 2,
            "itemRightClick": 2,
        }

    @init_wrapper
    def initTree(self, config):
        pass

    @function_wrapper
    def focusItem(self, id):
        pass

    @function_wrapper
    def destructor(self):
        pass

    @function_wrapper
    def editItem(self, id,  config):
        pass

    @function_wrapper
    def getState(self):
        pass

    @function_wrapper
    def setState(self, state):
        pass

    @function_wrapper
    def toggle(self, id):
        pass

    @function_wrapper
    def getChecked(self):
        pass

    @function_wrapper
    def checkItem(self, id):
        pass

    @function_wrapper
    def collapse(self, id):
        pass

    @function_wrapper
    def collapseAll(self):
        pass

    @function_wrapper
    def expand(self, id):
        pass

    @function_wrapper
    def expandAll(self):
        pass

    @function_wrapper
    def uncheckItem(self, id):
        pass

    @function_wrapper
    def close(self, id):
        pass

    @function_wrapper
    def closeAll(self):
        pass

    @function_wrapper
    def open(self, id):
        pass

    @function_wrapper
    def openAll(self):
        pass

    @function_wrapper
    def unCheckItem(self, id):
        pass

    @event_wrapper
    def afterCollapse(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_2.TreeEvents.afterCollapse, [id]);"""
        pass

    @event_wrapper
    def afterExpand(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_2.TreeEvents.afterExpand, [id]);"""
        pass

    @event_wrapper
    def beforeCollapse(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_2.TreeEvents.beforeCollapse, [id])) {"""
        pass

    @event_wrapper
    def beforeExpand(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_2.TreeEvents.beforeExpand, [id])) {"""
        pass

    @event_wrapper
    def itemClick(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_2.TreeEvents.itemClick, [id, e]);"""
        pass

    @event_wrapper
    def itemDblClick(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_2.TreeEvents.itemDblClick, [id, e]);"""
        pass

    @event_wrapper
    def itemRightClick(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_2.TreeEvents.itemRightClick, [id, e]);"""
        pass


class Window:
    def __init__(self, parent, session_id):
        self._unique_id = str(uuid4())
        self._event_param_qty = {
            "afterHide": 0,
            "afterShow": 0,
            "beforeHide": 0,
            "beforeShow": 2,
            "headerDoubleClick": 0,
            "move": 3,
            "resize": 3,
        }

    @init_wrapper
    def initWindow(self, config):
        pass

    @function_wrapper
    def paint(self):
        pass

    @function_wrapper
    def setFullScreen(self):
        pass

    @function_wrapper
    def setSize(self, width,  height):
        pass

    @function_wrapper
    def getSize(self):
        pass

    @function_wrapper
    def setPosition(self, left,  top):
        pass

    @function_wrapper
    def getPosition(self):
        pass

    @function_wrapper
    def show(self, left,  top):
        pass

    @function_wrapper
    def hide(self):
        pass

    @function_wrapper
    def isVisible(self):
        pass

    @function_wrapper
    def getWidget(self):
        pass

    @function_wrapper
    def getContainer(self):
        pass

    @function_wrapper
    def attach(self, name,  config):
        pass

    @function_wrapper
    def attachHTML(self, html):
        pass

    @function_wrapper
    def getRootView(self):
        pass

    @function_wrapper
    def destructor(self):
        pass

    @function_wrapper
    def fullScreen(self):
        pass

    @event_wrapper
    def afterHide(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def afterShow(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def beforeHide(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def beforeShow(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.WindowEvents.beforeShow, [left, top])) {"""
        pass

    @event_wrapper
    def headerDoubleClick(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: NO ARGS"""
        pass

    @event_wrapper
    def move(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.WindowEvents.move, [position,oldposition,{ left: true, top: true, bottom: true, right: true }]);"""
        pass

    @event_wrapper
    def resize(self, callable, ret_widget_values=[], block_signal = False):
        """JS_ARGS: types_1.WindowEvents.resize, [size, { left: left, top: top, height: height, width: width }, resizeConfig]);"""
        pass



if __name__=="__main__":
    layout = Layout()
    layout.afterAdd({})