"""
DHX Toolbar Widget Implementation
"""

from .raw_dhx_toolbar import Toolbar as dhx_raw_toolbar


class Toolbar:
    """DHX Toolbar class"""
    def __init__(self, toolbar_id, style, session_id, parent):
        self._raw_toolbar = dhx_raw_toolbar(parent, session_id)
        self.name = toolbar_id
        self.session_id = session_id
        self.config = None
        self.items = []
        self.style = style

        self.item_type_info = {}

        # map pywrm properties to dhx properties
        self.item_property_map = {
            "type": "type",
            "id": "id",
            "style": "css",
            "icon": "src",
            "text": "value",
            "html": "html",
            "count": "count",
            "tooltip": "tooltip",
            "items": "items"
        }

        # map pywrm item types to dhx item types
        self.type_mapping = {
            "button": "button",
            "menu": "selectButton",
            "item": "SelectButton.Item",
            "html": "customHTML",
            "seperator": "seperator",
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
            "css": self.style
        }
        return self.config

    @property
    def raw_widget(self):
        return self._raw_toolbar
    
    def init_widget(self):
        """Initialize the widget for the first time"""
        self._build_config()
        self._raw_toolbar.initToolbar(self.config)
        self._raw_toolbar.parse(self.config)

    def add_toolbar_items(self, *toolbar_items):
        """Add toolbar items to toolbar"""
        self.items += [self._map_item(item) for item in toolbar_items]
        print("ADDED", toolbar_items)
        print(self.items)

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
        self._raw_toolbar.click(
            self.on_click_return,
            ret_widget_values=ret_widget_values,
            block_signal=block_signal
        )

    def on_click_return(self, id, event):
        """On click event return data"""
        self.on_click_callable(id)
    