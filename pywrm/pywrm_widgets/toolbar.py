"""
PyWRM Toolbar implementation
"""

from external_widgets.w2ui.w2ui_toolbar import Toolbar as w2ui_toolbar
from external_widgets.dhx.dhx_toolbar import Toolbar as dhx_toolbar


class ToolbarItem:
    """Toolbar Item for placement into a Toolbar Widget"""
    def __init__(self, item_type, item_id, **kwargs):
        self.item_type = item_type
        self.item_id = item_id
        self.kwargs = kwargs
        self.item_type_info = None
        self.parent = None
        #TODO check kwargs against property setters and raise if not there
        self.config = {
            "id": item_id,
            "type": item_type,
            **kwargs
        }
        #TODO raise errors when parameters that are not supported on certain
        #TODO types get added for the below properties and setters

    def build_defaults(self, parent):
        """Apply toolbar item defaults to configuration"""
        self.parent = parent
        self.item_type_info = self.parent.base_widget.item_type_info.get(self.item_type)
        if self.item_type_info:
            item_defaults = {k.replace("item_default_", ""):v
                              for k, v in self.item_type_info.items()
                              if "item_default_" in k}
        else:
            item_defaults = {}

        # config should update item_defaults so user values take precedence
        item_defaults.update(self.config)
        self.config = item_defaults

    def disable(self):
        """Disable toolbar item"""
        self.parent.disable(self.item_id)

    def enable(self):
        """Enable toolbar item"""
        self.parent.enable(self.item_id)

    def hide(self):
        """Hide the toolbar item"""
        self.parent.hide(self.item_id)

    def show(self):
        """Show the toolbar item"""
        self.parent.show(self.item_id)

    @property
    def style(self) -> str:
        """get the name of a CSS class(es) applied to toolbar item"""
        return self.config.get("css", "")

    @style.setter
    def style(self, value: str):
        """set the name of a CSS class(es) applied to toolbar item"""
        self.config["css"] = value

    @property
    def icon(self) -> str:
        """get the name of icon applied to toolbar item"""
        return self.config.get("icon", "")

    @icon.setter
    def icon(self, value: str):
        """set the name of the icon to be applied to the toolbar item"""
        self.config["icon"] = value

    @property
    def text(self) -> str:
        """get the text applied to toolbar item"""
        return self.config.get("text", "")

    @text.setter
    def text(self, value: str):
        """set the text to be applied to the toolbar item"""
        self.config["text"] = value

    @property
    def tooltip(self) -> str:
        """get the tooltip to be applied to toolbar item"""
        return self.config.get("tooltip", "")

    @tooltip.setter
    def tooltip(self, value: str):
        """set the name of the  to be applied to the toolbar item"""
        self.config["tooltip"] = value

    @property
    def html(self) -> str:
        """get the html to be applied to toolbar item"""
        return self.config.get("html", "")

    @html.setter
    def html(self, value: str):
        """set the name of the  to be applied to the toolbar item"""
        self.config["html"] = value

    @property
    def count(self) -> str:
        """get the name of  applied to toolbar item"""
        return self.config.get("count", "")

    @count.setter
    def count(self, value: str):
        """set the name of the  to be applied to the toolbar item"""
        self.config["count"] = value

    @property
    def items(self) -> list:
        """get the name of  applied to toolbar item"""
        return self.config.get("", "")

    @items.setter
    def items(self, value: list):
        """set the name of the  to be applied to the toolbar item"""
        self.config["items"] = value


class ToolbarItemType:
    """Toolbar Item Types"""
    button = "button"
    menu = "menu"
    menu_item = "menu_item"
    html = "html"
    seperator = "seperator"
    spacer = "spacer"


class Toolbar:
    """Toolbar widget implementation"""
    widget_set = None

    def __init__(self, toolbar_id, parent=None, style="", session_id=""):
        widget_set = self.widget_set if self.widget_set else (parent.widget_set if parent else None)
        self.parent = parent
        self.session_id = session_id or self.parent.session_id
        self.name = toolbar_id
        self.style = style

        if widget_set == "dhx":
            self._base_toolbar = dhx_toolbar(toolbar_id, style=self.style, session_id=self.session_id, parent=parent)
        elif widget_set == "w2ui":
            self._base_toolbar = w2ui_toolbar(toolbar_id, style=self.style, session_id=self.session_id, parent=parent)
        else:
            raise ValueError("Widgetset is not defined")

        self.on_click_callable = None

    @property
    def base_widget(self):
        """Returns protected base toolbar class"""
        return self._base_toolbar

    def init_widget(self):
        """Initialize the widget for the first time"""
        self._base_toolbar.init_toolbar(self.name, self.style)

    def add_toolbar_items(self, *toolbar_items):
        """Add toolbar items to toolbar"""
        for anitem in toolbar_items:
            anitem.build_defaults(self)
            self._base_toolbar.add_toolbar_items(anitem.config)
            setattr(self, anitem.item_id, anitem)

    def destroy(self):
        """Destroy toolbar widget"""
        self._base_toolbar.destroy()

    def disable(self, toolbar_item_id):
        """Disable toolbar item"""
        self._base_toolbar.disable(toolbar_item_id)

    def enable(self, toolbar_item_id):
        """Enable toolbar item"""
        self._base_toolbar.enable(toolbar_item_id)

    def hide(self, toolbar_item_id):
        """Hide the toolbar item"""
        self._base_toolbar.hide(toolbar_item_id)

    def show(self, toolbar_item_id):
        """Show the toolbar item"""
        self._base_toolbar.show(toolbar_item_id)

    def repaint(self):
        """Repaint the toolbar widget"""
        self._base_toolbar.repaint()

    def on_click(self, event_callable, ret_widget_values=None, block_signal=False):
        """Handle on click event for toolbar widget"""
        #TODO implement ret_widget_values
        #TODO implement block_signal if possible or remove
        ret_id_list = []
        self.on_click_callable = event_callable
        self._base_toolbar.on_click(self.on_click_return, ret_id_list, block_signal)

    def on_click_return(self, toolbar_item_id):
        """Toolbar on click event return"""
        self.on_click_callable(toolbar_item_id)