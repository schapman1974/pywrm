""" Auto Generated raw classes for dhx. """
from uuid import uuid4

from decorators.decorators import function_wrapper


class Calendar:
    def __init__(self):
        self._unique_id = str(uuid4())

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

    def change(self, arg0, arg1, arg2):
        """JS_ARGS: types_1.CalendarEvents.change, [_this._getSelected(), oldDate, true]);"""
        pass

    def beforeChange(self, arg0, arg1, arg2):
        """JS_ARGS: types_1.CalendarEvents.beforeChange, [newDate, oldDate, true])) {"""
        pass

    def modeChange(self, arg0):
        """JS_ARGS: types_1.CalendarEvents.modeChange, [types_1.ViewMode.timepicker]);"""
        pass

    def monthSelected(self, arg0):
        """JS_ARGS: types_1.CalendarEvents.monthSelected, [date]);"""
        pass

    def yearSelected(self, arg0):
        """JS_ARGS: types_1.CalendarEvents.yearSelected, [date]);"""
        pass

    def cancelClick(self):
        """JS_ARGS: NO ARGS"""
        pass

    def dateMouseOver(self, arg0, arg1):
        """JS_ARGS: types_1.CalendarEvents.dateMouseOver, [new Date(node.attrs._date), event]);"""
        pass

    def dateHover(self, arg0, arg1):
        """JS_ARGS: types_1.CalendarEvents.dateHover, [new Date(node.attrs._date), event]); // TODO: remove sute_7.0"""
        pass


class Chart:
    def __init__(self):
        self._unique_id = str(uuid4())

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

    def toggleSeries(self, arg0, arg1):
        """JS_ARGS: types_1.ChartEvents.toggleSeries, [id, pieLike]); }"""
        pass

    def chartMouseMove(self, arg0, arg1, arg2, arg3):
        """JS_ARGS: types_1.ChartEvents.chartMouseMove, [x, y, _this._left + left, _this._top + top]);"""
        pass

    def chartMouseLeave(self):
        """JS_ARGS: NO ARGS"""
        pass

    def resize(self, arg0):
        """JS_ARGS: types_1.ChartEvents.resize, [{width: _this._width,height: _this._height}]);"""
        pass

    def serieClick(self, arg0, arg1):
        """JS_ARGS: types_1.ChartEvents.serieClick, [id, value]); }"""
        pass


class Colorpicker:
    def __init__(self):
        self._unique_id = str(uuid4())

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

    def change(self, arg0):
        """JS_ARGS: types_1.ColorpickerEvents.change, [this._selected]);"""
        pass

    def apply(self):
        """JS_ARGS: NO ARGS"""
        pass

    def cancelClick(self):
        """JS_ARGS: NO ARGS"""
        pass

    def modeChange(self, arg0):
        """JS_ARGS: types_1.ColorpickerEvents.modeChange, [mode]);"""
        pass

    def selectClick(self):
        """JS_ARGS: NO ARGS"""
        pass

    def colorChange(self, arg0):
        """JS_ARGS: types_1.ColorpickerEvents.colorChange, [this._selected]); // TODO: remove sute_7.0"""
        pass

    def viewChange(self, arg0):
        """JS_ARGS: types_1.ColorpickerEvents.viewChange, [mode]); // TODO: remove sute_7.0"""
        pass


class Combobox:
    def __init__(self):
        self._unique_id = str(uuid4())

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

    def change(self):
        """JS_ARGS: NO ARGS"""
        pass

    def open(self):
        """JS_ARGS: NO ARGS"""
        pass

    def input(self, arg0):
        """JS_ARGS: types_1.ComboboxEvents.input, [value]);"""
        pass

    def beforeClose(self):
        """JS_ARGS: NO ARGS"""
        pass

    def afterClose(self):
        """JS_ARGS: NO ARGS"""
        pass

    def close(self):
        """JS_ARGS: NO ARGS"""
        pass


class DataView:
    def __init__(self):
        self._unique_id = str(uuid4())

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

    def click(self, arg0, arg1):
        """JS_ARGS: types_2.DataViewEvents.click, [id, e]);"""
        pass

    def doubleClick(self, arg0, arg1):
        """JS_ARGS: types_2.DataViewEvents.doubleClick, [id, e]);"""
        pass

    def focusChange(self, arg0, arg1):
        """JS_ARGS: types_2.DataViewEvents.focusChange, [this._focusIndex, this.data.getId(this._focusIndex)]);"""
        pass

    def beforeEditStart(self, arg0):
        """JS_ARGS: types_2.DataViewEvents.beforeEditStart, [id])) {"""
        pass

    def afterEditStart(self, arg0):
        """JS_ARGS: types_2.DataViewEvents.afterEditStart, [id]);"""
        pass

    def beforeEditEnd(self, arg0, arg1):
        """JS_ARGS: types_1.DataViewEvents.beforeEditEnd, [value, this._item.id])) {"""
        pass

    def afterEditEnd(self, arg0, arg1):
        """JS_ARGS: types_1.DataViewEvents.afterEditEnd, [value, this._item.id]);"""
        pass

    def itemRightClick(self, arg0, arg1):
        """JS_ARGS: types_2.DataViewEvents.itemRightClick, [id, e]);"""
        pass

    def itemMouseOver(self, arg0, arg1):
        """JS_ARGS: types_2.DataViewEvents.itemMouseOver, [id, e]);"""
        pass

    def contextmenu(self, arg0, arg1):
        """JS_ARGS: types_2.DataViewEvents.contextmenu, [id, e]); // TODO: remove sute_7.0"""
        pass


class Form:
    def __init__(self):
        self._unique_id = str(uuid4())

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
    def disable(self):
        pass

    @function_wrapper
    def enable(self):
        pass

    @function_wrapper
    def isDisabled(self):
        pass

    @function_wrapper
    def clear(self):
        pass

    @function_wrapper
    def getValue(self):
        pass

    @function_wrapper
    def setValue(self, value):
        pass

    @function_wrapper
    def validate(self):
        pass

    @function_wrapper
    def getWidget(self):
        pass

    @function_wrapper
    def setConfig(self, config):
        pass

    def change(self, arg0, arg1):
        """JS_ARGS: types_1.FormEvents.change, [name, value]);"""
        pass

    def buttonClick(self, arg0, arg1):
        """JS_ARGS: types_1.FormEvents.buttonClick, [id, e]);"""
        pass

    def validationFail(self, arg0, arg1):
        """JS_ARGS: types_1.FormEvents.validationFail, [id, component]);"""
        pass

    def beforeSend(self):
        """JS_ARGS: NO ARGS"""
        pass

    def afterSend(self):
        """JS_ARGS: NO ARGS"""
        pass


class Grid:
    def __init__(self):
        self._unique_id = str(uuid4())

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

    def scroll(self, arg0):
        """JS_ARGS: types_1.GridEvents.scroll, [{y: e.target.scrollTop,x: e.target.scrollLeft}]);"""
        pass

    def sort(self, arg0):
        """JS_ARGS: types_1.GridEvents.sort, [item]);"""
        pass

    def expand(self, arg0):
        """JS_ARGS: types_1.GridEvents.expand, [item]);"""
        pass

    def filterChange(self, arg0, arg1, arg2):
        """JS_ARGS: types_1.GridEvents.filterChange, ["", colId, "comboFilter"]);"""
        pass

    def beforeResizeStart(self, arg0, arg1):
        """JS_ARGS: types_1.GridEvents.beforeResizeStart, [col, e])) {"""
        pass

    def resize(self, arg0):
        """JS_ARGS: types_1.GridEvents.resize, [grid.config.columns[i], e]);"""
        pass

    def afterResizeEnd(self, arg0, arg1):
        """JS_ARGS: types_1.GridEvents.afterResizeEnd, [col, e]);"""
        pass

    def cellClick(self):
        """JS_ARGS: NO ARGS"""
        pass

    def cellRightClick(self):
        """JS_ARGS: NO ARGS"""
        pass

    def cellMouseOver(self):
        """JS_ARGS: NO ARGS"""
        pass

    def cellMouseDown(self):
        """JS_ARGS: NO ARGS"""
        pass

    def cellDblClick(self):
        """JS_ARGS: NO ARGS"""
        pass

    def headerCellClick(self):
        """JS_ARGS: NO ARGS"""
        pass

    def footerCellClick(self):
        """JS_ARGS: NO ARGS"""
        pass

    def headerCellMouseOver(self):
        """JS_ARGS: NO ARGS"""
        pass

    def footerCellMouseOver(self):
        """JS_ARGS: NO ARGS"""
        pass

    def headerCellMouseDown(self):
        """JS_ARGS: NO ARGS"""
        pass

    def footerCellMouseDown(self):
        """JS_ARGS: NO ARGS"""
        pass

    def headerCellDblClick(self):
        """JS_ARGS: NO ARGS"""
        pass

    def footerCellDblClick(self):
        """JS_ARGS: NO ARGS"""
        pass

    def headerCellRightClick(self):
        """JS_ARGS: NO ARGS"""
        pass

    def footerCellRightClick(self):
        """JS_ARGS: NO ARGS"""
        pass

    def beforeEditStart(self, arg0, arg1, arg2):
        """JS_ARGS: types_1.GridEvents.beforeEditStart, [row, col, editorType])) {"""
        pass

    def afterEditStart(self, arg0, arg1, arg2):
        """JS_ARGS: types_1.GridEvents.afterEditStart, [row, col, editorType]);"""
        pass

    def beforeEditEnd(self, arg0, arg1, arg2):
        """JS_ARGS: types_1.GridEvents.beforeEditEnd, [value, this._cell.row, this._cell.col])) {"""
        pass

    def afterEditEnd(self, arg0, arg1, arg2):
        """JS_ARGS: types_1.GridEvents.afterEditEnd, [value, this._cell.row, this._cell.col]);"""
        pass

    def beforeKeyDown(self, arg0):
        """JS_ARGS: types_1.GridEvents.beforeKeyDown, [e])) {"""
        pass

    def afterKeyDown(self, arg0):
        """JS_ARGS: types_1.GridEvents.afterKeyDown, [e]);"""
        pass

    def headerInput(self, arg0, arg1, arg2):
        """JS_ARGS: types_1.GridEvents.headerInput, ["", colId, "comboFilter"]); // TODO: remove sute_7.0"""
        pass


class Layout:
    def __init__(self):
        self._unique_id = str(uuid4())

    @function_wrapper
    def toVDOM(self):
        pass

    @function_wrapper
    def removeCell(self, id):
        pass

    @function_wrapper
    def addCell(self, config,  index):
        pass

    @function_wrapper
    def getId(self, index):
        pass

    @function_wrapper
    def getRefs(self, name):
        pass

    @function_wrapper
    def getCell(self, id):
        pass

    @function_wrapper
    def forEach(self, cb,  parent,  level):
        pass

    @function_wrapper
    def cell(self, id):
        pass

    def beforeShow(self, arg0):
        """JS_ARGS: types_1.LayoutEvents.beforeShow, [this.id])) {"""
        pass

    def afterShow(self):
        """JS_ARGS: NO ARGS"""
        pass

    def beforeHide(self, arg0):
        """JS_ARGS: types_1.LayoutEvents.beforeHide, [this.id])) {"""
        pass

    def afterHide(self, arg0):
        """JS_ARGS: types_1.LayoutEvents.afterHide, [this.id]);"""
        pass

    def beforeResizeStart(self, arg0):
        """JS_ARGS: types_1.LayoutEvents.beforeResizeStart, [_this.id])) {"""
        pass

    def resize(self, arg0):
        """JS_ARGS: types_1.LayoutEvents.resize, [_this.id]);"""
        pass

    def afterResizeEnd(self, arg0):
        """JS_ARGS: types_1.LayoutEvents.afterResizeEnd, [_this.id]);"""
        pass

    def beforeAdd(self, arg0):
        """JS_ARGS: types_1.LayoutEvents.beforeAdd, [config.id])) {"""
        pass

    def afterAdd(self, arg0):
        """JS_ARGS: types_1.LayoutEvents.afterAdd, [config.id])) {"""
        pass

    def beforeRemove(self, arg0):
        """JS_ARGS: types_1.LayoutEvents.beforeRemove, [id])) {"""
        pass

    def afterRemove(self, arg0):
        """JS_ARGS: types_1.LayoutEvents.afterRemove, [id]);"""
        pass

    def beforeCollapse(self, arg0):
        """JS_ARGS: types_1.LayoutEvents.beforeCollapse, [this.id])) {"""
        pass

    def afterCollapse(self, arg0):
        """JS_ARGS: types_1.LayoutEvents.afterCollapse, [this.id]);"""
        pass

    def beforeExpand(self, arg0):
        """JS_ARGS: types_1.LayoutEvents.beforeExpand, [this.id])) {"""
        pass

    def afterExpand(self, arg0):
        """JS_ARGS: types_1.LayoutEvents.afterExpand, [this.id]);"""
        pass


class List:
    def __init__(self):
        self._unique_id = str(uuid4())

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

    def click(self, arg0, arg1):
        """JS_ARGS: types_2.ListEvents.click, [id, e]);"""
        pass

    def doubleClick(self, arg0, arg1):
        """JS_ARGS: types_2.ListEvents.doubleClick, [id, e]);"""
        pass

    def focusChange(self, arg0, arg1):
        """JS_ARGS: types_2.ListEvents.focusChange, [this._focusIndex, this.data.getId(this._focusIndex)]);"""
        pass

    def beforeEditStart(self, arg0):
        """JS_ARGS: types_2.ListEvents.beforeEditStart, [id])) {"""
        pass

    def afterEditStart(self, arg0):
        """JS_ARGS: types_2.ListEvents.afterEditStart, [id]);"""
        pass

    def beforeEditEnd(self, arg0, arg1):
        """JS_ARGS: types_1.ListEvents.beforeEditEnd, [value, this._item.id])) {"""
        pass

    def afterEditEnd(self, arg0, arg1):
        """JS_ARGS: types_1.ListEvents.afterEditEnd, [value, this._item.id]);"""
        pass

    def itemRightClick(self, arg0, arg1):
        """JS_ARGS: types_2.ListEvents.itemRightClick, [id, e]);"""
        pass

    def itemMouseOver(self, arg0, arg1):
        """JS_ARGS: types_2.ListEvents.itemMouseOver, [id, e]);"""
        pass

    def contextmenu(self, arg0, arg1):
        """JS_ARGS: types_2.ListEvents.contextmenu, [id, e]); // TODO: remove sute_7.0"""
        pass


class Menu:
    def __init__(self):
        self._unique_id = str(uuid4())

    @function_wrapper
    def showAt(self, elem,  showAt):
        pass


class Popup:
    def __init__(self):
        self._unique_id = str(uuid4())

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

    def beforeHide(self, arg0, arg1):
        """JS_ARGS: types_1.PopupEvents.beforeHide, [fromOuterClick, e])) {"""
        pass

    def beforeShow(self, arg0):
        """JS_ARGS: types_1.PopupEvents.beforeShow, [node])) {"""
        pass

    def afterHide(self, arg0):
        """JS_ARGS: types_1.PopupEvents.afterHide, [e]);"""
        pass

    def afterShow(self, arg0):
        """JS_ARGS: types_1.PopupEvents.afterShow, [node]);"""
        pass

    def click(self, arg0):
        """JS_ARGS: types_1.PopupEvents.click, [e]); };"""
        pass


class Ribbon:
    def __init__(self):
        self._unique_id = str(uuid4())

    @function_wrapper
    def getState(self):
        pass

    @function_wrapper
    def setState(self, state):
        pass


class Sidebar:
    def __init__(self):
        self._unique_id = str(uuid4())

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

    def beforeCollapse(self):
        """JS_ARGS: NO ARGS"""
        pass

    def afterCollapse(self):
        """JS_ARGS: NO ARGS"""
        pass

    def beforeExpand(self):
        """JS_ARGS: NO ARGS"""
        pass

    def afterExpand(self):
        """JS_ARGS: NO ARGS"""
        pass

    def toggle(self, arg0):
        """JS_ARGS: types_1.SidebarEvents.toggle, [this.config.collapsed]); // TODO: remove sute_7.0"""
        pass


class Slider:
    def __init__(self):
        self._unique_id = str(uuid4())

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

    def change(self, arg0, arg1, arg2):
        """JS_ARGS: types_1.SliderEvents.change, [newValue, oldValue, extra]);"""
        pass

    def mousedown(self, arg0):
        """JS_ARGS: types_1.SliderEvents.mousedown, [e]);"""
        pass

    def mouseup(self, arg0):
        """JS_ARGS: types_1.SliderEvents.mouseup, [e]);"""
        pass


class Tabbar:
    def __init__(self):
        self._unique_id = str(uuid4())

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

    def change(self, arg0, arg1):
        """JS_ARGS: types_1.TabbarEvents.change, [_this.config.activeView, prev]);"""
        pass

    def beforeClose(self, arg0):
        """JS_ARGS: types_1.TabbarEvents.beforeClose, [id])) {"""
        pass

    def afterClose(self, arg0):
        """JS_ARGS: types_1.TabbarEvents.afterClose, [id]);"""
        pass

    def close(self, arg0):
        """JS_ARGS: types_1.TabbarEvents.close, [id]); // TODO: remove sute_7.0"""
        pass


class Timepicker:
    def __init__(self):
        self._unique_id = str(uuid4())

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

    def change(self, arg0):
        """JS_ARGS: types_1.TimepickerEvents.change, [_this.getValue()]);"""
        pass

    def apply(self, arg0):
        """JS_ARGS: types_1.TimepickerEvents.apply, [_this._time]);"""
        pass

    def beforeClose(self):
        """JS_ARGS: NO ARGS"""
        pass

    def afterClose(self):
        """JS_ARGS: NO ARGS"""
        pass

    def close(self):
        """JS_ARGS: NO ARGS"""
        pass

    def save(self, arg0):
        """JS_ARGS: types_1.TimepickerEvents.save, [_this._time]); // TODO: remove sute_7.0"""
        pass


class Toolbar:
    def __init__(self):
        self._unique_id = str(uuid4())

    @function_wrapper
    def getState(self):
        pass

    @function_wrapper
    def setState(self, state):
        pass


class Tree:
    def __init__(self):
        self._unique_id = str(uuid4())

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

    def itemClick(self, arg0, arg1):
        """JS_ARGS: types_2.TreeEvents.itemClick, [id, e]);"""
        pass

    def itemDblClick(self, arg0, arg1):
        """JS_ARGS: types_2.TreeEvents.itemDblClick, [id, e]);"""
        pass

    def itemRightClick(self, arg0, arg1):
        """JS_ARGS: types_2.TreeEvents.itemRightClick, [id, e]);"""
        pass

    def beforeCollapse(self, arg0):
        """JS_ARGS: types_2.TreeEvents.beforeCollapse, [id])) {"""
        pass

    def afterCollapse(self, arg0):
        """JS_ARGS: types_2.TreeEvents.afterCollapse, [id]);"""
        pass

    def beforeExpand(self, arg0):
        """JS_ARGS: types_2.TreeEvents.beforeExpand, [id])) {"""
        pass

    def afterExpand(self, arg0):
        """JS_ARGS: types_2.TreeEvents.afterExpand, [id]);"""
        pass

    def itemContextMenu(self, arg0, arg1):
        """JS_ARGS: types_2.TreeEvents.itemContextMenu, [id, e]); // TODO: remove sute_7.0"""
        pass


class Window:
    def __init__(self):
        self._unique_id = str(uuid4())

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

    def resize(self, arg0, arg1, arg2):
        """JS_ARGS: types_1.WindowEvents.resize, [size, { left: left, top: top, height: height, width: width }, resizeConfig]);"""
        pass

    def headerDoubleClick(self):
        """JS_ARGS: NO ARGS"""
        pass

    def move(self, arg0, arg1, arg2):
        """JS_ARGS: types_1.WindowEvents.move, [position,oldposition,{ left: true, top: true, bottom: true, right: true }]);"""
        pass

    def afterShow(self):
        """JS_ARGS: NO ARGS"""
        pass

    def afterHide(self):
        """JS_ARGS: NO ARGS"""
        pass

    def beforeShow(self, arg0, arg1):
        """JS_ARGS: types_1.WindowEvents.beforeShow, [left, top])) {"""
        pass

    def beforeHide(self):
        """JS_ARGS: NO ARGS"""
        pass
