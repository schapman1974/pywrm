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
