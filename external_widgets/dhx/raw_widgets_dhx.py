""" Auto Generated raw classes for dhx. """


class Calendar:
    def __init__(self):
        pass

    def setValue(self, value):
        pass

    def getValue(self, asDateObject):
        pass

    def getCurrentMode(self):
        pass

    def showDate(self, date,  mode):
        pass

    def destructor(self):
        pass

    def clear(self):
        pass

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
        pass

    def getSeries(self, key):
        pass

    def eachSeries(self, handler):
        pass

    def destructor(self):
        pass

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
        pass

    def destructor(self):
        pass

    def clear(self):
        pass

    def setValue(self, value):
        pass

    def setFocus(self, value):
        pass

    def getValue(self):
        pass

    def getCustomColors(self):
        pass

    def setCustomColors(self, customColors):
        pass

    def setCurrentMode(self, mode):
        pass

    def getCurrentMode(self):
        pass

    def getView(self):
        pass

    def setView(self, mode):
        pass

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
        pass

    def focus(self):
        pass

    def enable(self):
        pass

    def disable(self):
        pass

    def isDisabled(self):
        pass

    def clear(self):
        pass

    def getValue(self, asArray):
        pass

    def setValue(self, ids):
        pass

    def destructor(self):
        pass

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
        pass

    def editItem(self, id):
        pass

    def getFocusItem(self):
        pass

    def setItemInRow(self, amount):
        pass

    def setFocus(self, id):
        pass

    def getFocus(self):
        pass

    def destructor(self):
        pass

    def getFocusIndex(self):
        pass

    def setFocusIndex(self, index):
        pass

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
        pass

    def send(self, url,  method,  asFormData):
        pass

    def clear(self, method):
        pass

    def setValue(self, obj):
        pass

    def getValue(self, asFormData):
        pass

    def getItem(self, id):
        pass

    def validate(self):
        pass

    def getRootView(self):
        pass

    def disable(self):
        pass

    def enable(self):
        pass

    def isDisabled(self, id):
        pass

    def forEach(self, callback):
        pass

    def destructor(self):
        pass

    def setConfig(self, config):
        pass

    def disable(self):
        pass

    def enable(self):
        pass

    def isDisabled(self):
        pass

    def clear(self):
        pass

    def getValue(self):
        pass

    def setValue(self, value):
        pass

    def validate(self):
        pass

    def getWidget(self):
        pass

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
        pass

    def destructor(self):
        pass

    def setColumns(self, columns):
        pass

    def addRowCss(self, id,  css):
        pass

    def removeRowCss(self, id,  css):
        pass

    def addCellCss(self, row,  col,  css):
        pass

    def removeCellCss(self, row,  col,  css):
        pass

    def showColumn(self, colId):
        pass

    def hideColumn(self, colId):
        pass

    def isColumnHidden(self, colId):
        pass

    def getScrollState(self):
        pass

    def scroll(self, x,  y):
        pass

    def scrollTo(self, row,  col):
        pass

    def adjustColumnWidth(self, id,  adjust):
        pass

    def getCellRect(self, row,  col):
        pass

    def getColumn(self, colId):
        pass

    def addSpan(self, spanObj):
        pass

    def getSpan(self, row,  col):
        pass

    def removeSpan(self, row,  col):
        pass

    def editCell(self, rowId,  colId,  editorType):
        pass

    def editEnd(self, withoutSave):
        pass

    def getSortingState(self):
        pass

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
        pass

    def toVDOM(self):
        pass

    def removeCell(self, id):
        pass

    def addCell(self, config,  index):
        pass

    def getId(self, index):
        pass

    def getRefs(self, name):
        pass

    def getCell(self, id):
        pass

    def forEach(self, cb,  parent,  level):
        pass

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
        pass

    def editItem(self, id):
        pass

    def getFocusItem(self):
        pass

    def setFocus(self, id):
        pass

    def getFocus(self):
        pass

    def destructor(self):
        pass

    def getFocusIndex(self):
        pass

    def setFocusIndex(self, index):
        pass

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
        pass

    def showAt(self, elem,  showAt):
        pass


class Popup:
    def __init__(self):
        pass

    def show(self, node,  config,  attached):
        pass

    def hide(self):
        pass

    def isVisible(self):
        pass

    def attach(self, name,  config):
        pass

    def attachHTML(self, html):
        pass

    def getWidget(self):
        pass

    def getContainer(self):
        pass

    def toVDOM(self):
        pass

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
        pass

    def getState(self):
        pass

    def setState(self, state):
        pass


class Sidebar:
    def __init__(self):
        pass

    def toggle(self):
        pass

    def collapse(self):
        pass

    def expand(self):
        pass

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
        pass

    def disable(self):
        pass

    def enable(self):
        pass

    def isDisabled(self):
        pass

    def focus(self, extra):
        pass

    def getValue(self):
        pass

    def setValue(self, value):
        pass

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
        pass

    def toVDOM(self):
        pass

    def destructor(self):
        pass

    def getWidget(self):
        pass

    def setActive(self, id):
        pass

    def getActive(self):
        pass

    def addTab(self, config,  index):
        pass

    def removeTab(self, id):
        pass

    def disableTab(self, id):
        pass

    def enableTab(self, id):
        pass

    def isDisabled(self, id):
        pass

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
        pass

    def getValue(self, asOBject):
        pass

    def setValue(self, value):
        pass

    def clear(self):
        pass

    def destructor(self):
        pass

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
        pass

    def getState(self):
        pass

    def setState(self, state):
        pass


class Tree:
    def __init__(self):
        pass

    def focusItem(self, id):
        pass

    def destructor(self):
        pass

    def editItem(self, id,  config):
        pass

    def getState(self):
        pass

    def setState(self, state):
        pass

    def toggle(self, id):
        pass

    def getChecked(self):
        pass

    def checkItem(self, id):
        pass

    def collapse(self, id):
        pass

    def collapseAll(self):
        pass

    def expand(self, id):
        pass

    def expandAll(self):
        pass

    def uncheckItem(self, id):
        pass

    def close(self, id):
        pass

    def closeAll(self):
        pass

    def open(self, id):
        pass

    def openAll(self):
        pass

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
        pass

    def paint(self):
        pass

    def setFullScreen(self):
        pass

    def setSize(self, width,  height):
        pass

    def getSize(self):
        pass

    def setPosition(self, left,  top):
        pass

    def getPosition(self):
        pass

    def show(self, left,  top):
        pass

    def hide(self):
        pass

    def isVisible(self):
        pass

    def getWidget(self):
        pass

    def getContainer(self):
        pass

    def attach(self, name,  config):
        pass

    def attachHTML(self, html):
        pass

    def getRootView(self):
        pass

    def destructor(self):
        pass

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
