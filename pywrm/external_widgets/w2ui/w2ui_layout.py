from .raw_widgets_w2ui import Layout as w2ui_raw_layout

class Layout:
    def __init__(self, layout_id, html="", resizable=False):
        self._raw_layout = w2ui_raw_layout()
        self.content_top_id = layout_id
        self.content_top_html = html
        self._resizable = resizable
        
        #set defaults for layout
        self.content_top = {
            "type": "main",
            "resizeable": self._resizable
        }
        self.top_header = {}
        self.content_bottom = {}
        self.left_sidebar = {}
        self.right_sidebar = {}
        self.bottom_footer = {}

    def init_layout(self):
        self.config = {
            "name": self.content_top_id,
            "panels": [
                self.top_header,
                self.content_top,
                self.content_bottom,
                self.left_sidebar,
                self.right_sidebar,
                self.bottom_footer
            ]
        }
        self._raw_layout.initLayout(self.config)

    def add_top_header(self, id="top_header", pixel_height=60, html=""):
        self.top_header = {
            "type": "top",
            "size": pixel_height
        }
        self._top_header_id = id
        if html:
            self._raw_layout.html("top", html)

    def add_bottom_footer(self, id="bottom_footer", pixel_height=60, html=""):
        self.bottom_footer = {
            "type": "bottom",
            "size": pixel_height
        }
        self._bottom_footer_id = id
        if html:
            self._raw_layout.html("bottom", html)

    def add_left_side(self, id="left_side", pixel_width=200, html=""):
        self.left_sidebar = {
            "type": "left",
            "size": pixel_width
        }
        self._left_sidebar_id = id
        if html:
            self._raw_layout.html("left", html)

    def add_right_side(self, id="right_side", pixel_width=200, html=""):
        self.right_sidebar = {
            "type": "right",
            "size": pixel_width
        }
        self._right_sidebar_id = id
        if html:
            self._raw_layout.html("right", html)

    def add_content_bottom(self, id="", pixel_height=200, html=""):
        self.content_bottom = {
            "type": "preview",
            "size": pixel_height
        }
        self._content_bottom_id = id
        if html:
            self._raw_layout.html("preview", html)

    def on_panel_hide(self, callable, ret_widget_values=[], block_signal = False):
        self._raw_layout.afterHide(
            callable,
            ret_widget_values=ret_widget_values,
            block_signal = block_signal
        )

    def on_panel_show(self, callable, ret_widget_values=[], block_signal = False):
        self._raw_layout.onShow(
            callable,
            ret_widget_values=ret_widget_values,
            block_signal = block_signal
        )

    def before_panel_resize(self, callable, ret_widget_values=[], block_signal = False):
        self._raw_layout.beforeResizeStart(
            callable,
            ret_widget_values=ret_widget_values,
            block_signal = block_signal
        )

    def on_panel_resize(self, callable, ret_widget_values=[], block_signal = False):
        self._raw_layout.resize(
            callable,
            ret_widget_values=ret_widget_values,
            block_signal = block_signal
        )

    def attach_widget(self, widget, panel):
        self._raw_layout.content(panel, widget, False)
