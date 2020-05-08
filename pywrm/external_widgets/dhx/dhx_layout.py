"""
DHX Layout Widget Implementation
"""

import json
from .raw_widgets_dhx import Layout as dhx_raw_layout


class Layout:
    """ DHX Layout class"""
    def __init__(self, layout_id, session_id, parent):
        self._raw_layout = dhx_raw_layout(parent, session_id)
        self.name = layout_id
        self.session_id = session_id
        self.config = None

        # set empty settings for panels
        self.content_top = {}
        self.top_header = {}
        self.content_bottom = {}
        self.left_side = {}
        self.right_side = {}
        self.bottom_footer = {}

        # callables for events
        self.on_panel_show_callable = None
        self.on_panel_hide_callable = None
        self.on_panel_resize_callable = None
        self.before_panel_resize_callable = None

        # set the panel type information for dhx panels
        self.panel_type_info = {
            "content_top":{
                "panel_default_width": "100%",
                "panel_default_height": "100%",
                "panel_default_css": "dhx_layout-cell",
                "panel_default_gravity": False,
                "panel_default_resizable": False,
            },
            "bottom_footer": {
                "panel_default_height": "10%",
                "panel_default_css": "dhx_layout-cell--border_top",
                "panel_default_gravity": False,
                "panel_default_resizable": False,
            },
            "content_bottom": {
                "panel_default_height": "15%",
                "panel_default_css": "dhx_layout-cell--border_top",
                "panel_default_gravity": False,
                "panel_default_resizable": False,
            },
            "left_side": {
                "panel_default_width": "10%",
                "panel_default_css": "dhx_layout-cell--border_right",
                "panel_default_gravity": False,
                "panel_default_resizable": False,
            },
            "right_side": {
                "panel_default_width": "10%",
                "panel_default_css": "dhx_layout-cell--border_left",
                "panel_default_gravity": False,
                "panel_default_resizable": False,
            },
            "top_header": {
                "panel_default_height": "10%",
                "panel_default_css": "dhx_layout-cell--border_bottom",
                "panel_default_gravity": False,
                "panel_default_resizable": False,
            },
        }

    def _config_cleanup(self, config: dict) -> dict:
        """ Clean up config so that is has only needed items."""

        if not self.content_bottom:
            del config["rows"][1]["cols"][1]["rows"][1]
        if not self.content_top:
            del config["rows"][1]["cols"][1]["rows"][0]
        if not self.right_side:
            del config["rows"][1]["cols"][2]
        if not self.left_side:
            del config["rows"][1]["cols"][0]
        if not self.bottom_footer:
            del config["rows"][2]
        if not self.top_header:
            del config["rows"][0]
        if not self.content_bottom and not self.content_top:
            if not self.left_side and not self.right_side:
                config_row_num = 1 if self.top_header else 0
                del config["rows"][config_row_num]
            else:
                config_row = config["rows"][1] if self.top_header else config["rows"][0]
                rem_col = 1 if self.left_side else 0
                del config_row["cols"][rem_col]
        return config

    def _build_config(self):
        """Build the panel config for the layout"""
        config = {
            "css": "dhx_layout-cell",
            "rows": [
                self.top_header,
                {
                    "cols": [
                        self.left_side,
                        {
                            "rows": [self.content_top,
                                     self.content_bottom,
                                    ]
                        },
                        self.right_side,
                    ]
                },
                self.bottom_footer
            ]
        }

        self.config = self._config_cleanup(config)
        return config


    def init_layout(self, has_panel, layout_name):
        """Initialize the layout to be displayed"""
        if not has_panel:
            self.content_top = {
                "id": layout_name,
                "css": "",
                "height": "100vh",
                "width": "100vw",
                "html": "",
                "gravity": False,
                "resizable": False
            }
        self._build_config()
        self._raw_layout.initLayout(self.config)

    def attach_widget(self, widget_id, panel_id, config):
        """Attach a widget to a panel in the layout"""
        self._build_config()
        self._raw_layout.attach(
            cell_id=panel_id,
            widget_id=widget_id,
            config=config
        )

    def repaint(self):
        """Repaint the layout on the screen"""
        self._raw_layout.paint()

    def hide_panel(self, panel):
        """Hide a panel on the layout"""
        self._raw_layout.hide(panel)

    def show_panel(self, panel):
        """Show a hidden panel on the layout"""
        self._raw_layout.show(panel)

    def toggle_panel(self, panel):
        """Toggle between hiding and showing a layout"""
        self._raw_layout.toggle(panel)

    def add_top_header(self, **kwargs):
        """Add the top header panel to the layout"""
        self.top_header = kwargs

    def add_bottom_footer(self, **kwargs):
        """Add the bottom footer panel to the layout"""
        self.bottom_footer = kwargs

    def add_left_side(self, **kwargs):
        """Add the left side panel to the layout"""
        self.left_side = kwargs

    def add_right_side(self, **kwargs):
        """Add the right side palen to the layout"""
        self.right_side = kwargs

    def add_content_top(self, **kwargs):
        """Add the content top panel to the layout"""
        self.content_top = kwargs

    def add_content_bottom(self, **kwargs):
        """Add the content bottom panel to the layout"""
        self.content_bottom = kwargs

    def on_panel_hide(self, event_callable, ret_widget_values=None, block_signal=False):
        """Hook to the panel hide event"""
        #TODO Implementation of ret_widget_values
        #TODO Implementation of block_signal?? or removal
        self.on_panel_hide_callable = event_callable
        self._raw_layout.afterHide(
            self.on_panel_hide_return,
            ret_widget_values=ret_widget_values,
            block_signal=block_signal
        )

    def on_panel_hide_return(self, panel_id):
        """Panel hide event return"""
        self.on_panel_hide_callable(panel_id)

    def on_panel_show(self, event_callable, ret_widget_values=None, block_signal=False):
        """Hook to the panel show event"""
        #TODO Implementation of ret_widget_values
        #TODO Implementation of block_signal?? or removal
        self.on_panel_show_callable = event_callable
        self._raw_layout.afterShow(
            self.on_panel_show_return,
            ret_widget_values=ret_widget_values,
            block_signal=block_signal
        )

    def on_panel_show_return(self, panel_id):
        """Panel show event return"""
        self.on_panel_show_callable(panel_id)

    def on_panel_resize(self, event_callable, ret_widget_values=None, block_signal=False):
        """Hook to the panel resize event"""
        #TODO Implementation of ret_widget_values
        #TODO Implementation of block_signal?? or removal
        self.on_panel_resize_callable = event_callable
        self._raw_layout.resize(
            self.on_panel_resize_return,
            ret_widget_values=ret_widget_values,
            block_signal=block_signal
        )

    def on_panel_resize_return(self, panel_id):
        """Panel resize event return"""
        self.on_panel_resize_callable(panel_id)

    def before_panel_resize(self, event_callable, ret_widget_values=None, block_signal=False):
        """Hook to the Before panel resize event"""
        #TODO Implementation of ret_widget_values
        #TODO Implementation of block_signal?? or removal
        self.before_panel_resize_callable = event_callable
        self._raw_layout.beforeResizeStart(
            self.before_panel_resize_return,
            ret_widget_values=ret_widget_values,
            block_signal=block_signal
        )

    def before_panel_resize_return(self, panel_id):
        """Before Panel resize event return"""
        self.before_panel_resize_callable(panel_id)
