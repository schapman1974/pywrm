"""
W2UI Toolbar Widget Implementation
"""

from .raw_w2ui_toolbar import Toolbar as w2ui_raw_toolbar


class Toolbar:
    """W2UI Toolbar class"""
    def __init__(self, toolbar_id, style, session_id, parent):
        self._raw_toolbar = w2ui_raw_toolbar(parent, session_id)
        self.name = toolbar_id
        self.session_id = session_id
        self.config = None
        self.items = []
        self.style = style

        self.item_type_info = {}

        # map pywrm properties to w2ui properties
        self.item_property_map = {
            "type": "type",
            "id": "id",
            "style": "style",
            "icon": "img",
            "text": "text",
            "html": "html",
            "count": "count",
            "tooltip": "tooltip",
            "items": "items"
        }

        # map pywrm item types to w2ui item types
        self.type_mapping = {
            "button": "button",
            "menu": "menu",
            "item": "Menu.Item",
            "html": "html",
            "seperator": "break",
            "spacer": "spacer"
        }

        # callables for events
        self.on_click_callable = None

    def _map_item(self, item):
        remapped = {}
        for item_prop, item_value in item.items():
            new_prop = self.item_property_map[item_prop]
            remapped[new_prop] = self.type_mapping[item_value] if new_prop=="type" else item_value
        return remapped

    def _build_config(self):
        self.config = {
            "name": self.name,
            "items": self.items,
            "style": self.style
        }
        return self.config

    @property
    def raw_widget(self):
        return self._raw_toolbar
    
    def init_widget(self):
        """Initialize the widget for the first time"""
        self._build_config()
        self._raw_toolbar.initToolbar(self.config)

    def attach(self):
        pass

    def add_toolbar_items(self, *toolbar_items):
        """Add toolbar items to toolbar"""
        self.items += [self._map_item(item) for item in toolbar_items]

    def destroy(self):
        """Destroy the toolbar"""
        pass

    def disable(self, item_id):
        """Disable item on the toolbar"""
        pass

    def enable(self, item_id):
        """Enable items on the toolbar"""
        pass

    def hide(self, item_id):
        """Hide items on the toolbar"""
        pass

    def show(self, item_id):
        """Show items on the toolbar"""
        pass

    def repaint(self):
        """Repaint the toolbar widget"""
        pass

    def on_click(self, event_callable, ret_widget_values=None, block_signal=False):
        """Hook to click event for toolbar"""
        #TODO Implementation of ret_widget_values
        #TODO Implementation of block_signal?? or removal
        self.on_click_callable = event_callable
        self._raw_toolbar.onClick(
            self.on_click_return,
            ret_widget_values=ret_widget_values,
            block_signal=block_signal
        )

    def on_click_return(self, event):
        """On click event return data"""
        self.on_click_callable(event["target"])
    