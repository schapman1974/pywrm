"""
W2UI Layout Widget Implementation
"""

from .raw_widgets_w2ui import Layout as w2ui_raw_layout

class Layout:
    """W2UI Layout class"""
    def __init__(self, layout_id, session_id, parent):
        self._raw_layout = w2ui_raw_layout(parent, session_id)
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
        style = ("background-color:white;padding:0px;color:rgba(0,0,0,0.7);"
                 "font-family:Roboto, Arial, Tahoma, Verdana, sans-serif;"
                 "font-weight:400;font-size:14px;line-height:20px;")
        self.border_top = "border-top:1px solid #e4e4e4;"
        self.border_bottom = "border-bottom:1px solid #e4e4e4;"
        self.border_left = "border-left:1px solid #e4e4e4;"
        self.border_right = "border-right:1px solid #e4e4e4;"
        self.panel_type_info = {
            "content_top":{
                "panel_default_type": "main",
                "panel_default_style": style,
                "panel_default_size": "100%",
                "panel_default_resizable": False,
            },
            "bottom_footer": {
                "panel_default_type": "bottom",
                "panel_default_style": style+self.border_top,
                "panel_default_size": "15%",
                "panel_default_resizable": False,
            },
            "content_bottom": {
                "panel_default_type": "preview",
                "panel_default_style": style+self.border_top,
                "panel_default_size": "15%",
                "panel_default_resizable": False,
            },
            "left_side": {
                "panel_default_type": "left",
                "panel_default_style": style+self.border_right,
                "panel_default_size": "10%",
                "panel_default_resizable": False,
            },
            "right_side": {
                "panel_default_type": "right",
                "panel_default_style": style+self.border_left,
                "panel_default_size": "10%",
                "panel_default_resizable": False,
            },
            "top_header": {
                "panel_default_type": "top",
                "panel_default_style": style+self.border_bottom,
                "panel_default_size": "10%",
                "panel_default_resizable": False,
            },
        }

    def _build_config(self):
        self.config = {
            "name": self.name,
            "panels": [
                self.top_header,
                self.content_top,
                self.content_bottom,
                self.left_side,
                self.right_side,
                self.bottom_footer
            ]
        }

        panel_cleanup = []
        for apanel in self.config["panels"]:
            if apanel:
                panel_cleanup.append(apanel)
        self.config["panels"] = panel_cleanup
        return self.config


    def init_layout(self, has_panel, layout_name):
        """Initialize the layout to be displayed"""
        if not has_panel:
            self.content_top = {
                "id": layout_name,
                "type": "main",
                "height": "100%",
                "resizable": False
            }
        self._build_config()
        self._raw_layout.initLayout(self.config)

    def attach_widget(self, widget_id, panel_id, config):
        """Attach a widget to a panel in the layout"""
        self._build_config()
        self._raw_layout.content(
            cell_id=self._get_type(panel_id),
            widget_id=widget_id,
            config=config
        )

    def repaint(self):
        """Repaint the layout on the screen"""
        self._raw_layout.refresh()

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
        if "html" in kwargs:
            kwargs["content"] = kwargs["html"]
        if "height" in kwargs:
            kwargs["size"] = kwargs["height"]
        if "size" in kwargs:
            kwargs["size"] = kwargs["size"].replace("vh", "%",).replace("vw", "%")
        self.top_header = kwargs

    def add_bottom_footer(self, **kwargs):
        """Add the bottom footer panel to the layout"""
        if "html" in kwargs:
            kwargs["content"] = kwargs["html"]
        if "height" in kwargs:
            kwargs["size"] = kwargs["height"]
        if "size" in kwargs:
            kwargs["size"] = kwargs["size"].replace("vw", "%",).replace("vw", "%")
        self.bottom_footer = kwargs

    def add_left_side(self, **kwargs):
        """Add the left side panel to the layout"""
        if "html" in kwargs:
            kwargs["content"] = kwargs["html"]
        if "width" in kwargs:
            kwargs["size"] = kwargs["width"]
        if "size" in kwargs:
            kwargs["size"] = kwargs["size"].replace("vh", "%",).replace("vw", "%")
        self.left_side = kwargs

    def add_right_side(self, **kwargs):
        """Add the right side palen to the layout"""
        if "html" in kwargs:
            kwargs["content"] = kwargs["html"]
        if "width" in kwargs:
            kwargs["size"] = kwargs["width"]
        if "size" in kwargs:
            kwargs["size"] = kwargs["size"].replace("vh", "%",).replace("vw", "%")
        self.right_side = kwargs

    def add_content_top(self, **kwargs):
        """Add the content top panel to the layout"""
        if "html" in kwargs:
            kwargs["content"] = kwargs["html"]
        if "height" in kwargs:
            kwargs["size"] = kwargs["height"]
        if "size" in kwargs:
            kwargs["size"] = kwargs["size"].replace("vh", "%",).replace("vw", "%")
        self.content_top = kwargs

    def add_content_bottom(self, **kwargs):
        """Add the content bottom panel to the layout"""
        if "html" in kwargs:
            kwargs["content"] = kwargs["html"]
        if "height" in kwargs:
            kwargs["size"] = kwargs["height"]
        if "size" in kwargs:
            kwargs["size"] = kwargs["size"].replace("vh", "%",).replace("vw", "%")
        self.content_bottom = kwargs

    def _get_type(self, panel_id):
        for panel_type in self.panel_type_info.keys():
            panel = self.__dict__[panel_type]
            if "id" in panel and panel["id"] == panel_id:
                return panel["type"]
        return None

    def _get_id(self, atype):
        for panel_type in self.panel_type_info.keys():
            panel = self.__dict__[panel_type]
            if "type" in panel and panel["type"] == atype:
                return panel["id"]
        return None

    def on_panel_hide(self, event_callable, ret_widget_values=None, block_signal=False):
        """Hook to the panel hide event"""
        #TODO Implementation of ret_widget_values
        #TODO Implementation of block_signal?? or removal
        self.on_panel_hide_callable = event_callable
        self._raw_layout.onHide(
            self.on_panel_hide_return,
            ret_widget_values=ret_widget_values,
            block_signal=block_signal
        )

    def on_panel_hide_return(self, event):
        """Panel hide event return"""
        self.on_panel_hide_callable(event["target"])

    def on_panel_show(self, event_callable, ret_widget_values=None, block_signal=False):
        """Hook to the panel show event"""
        #TODO Implementation of ret_widget_values
        #TODO Implementation of block_signal?? or removal
        self.on_panel_show_callable = event_callable
        self._raw_layout.onShow(
            self.on_panel_show_return,
            ret_widget_values=ret_widget_values,
            block_signal=block_signal
        )

    def on_panel_show_return(self, event):
        """Panel show event return"""
        self.on_panel_show_callable(event["target"])

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

    def on_panel_resize_return(self, event):
        """Panel resize event return"""
        self.on_panel_resize_callable(event["target"])

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

    def before_panel_resize_return(self, event):
        """Before Panel resize event return"""
        self.before_panel_resize_callable(event["target"])
