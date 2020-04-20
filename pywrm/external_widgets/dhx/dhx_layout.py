from .raw_widgets_dhx import Layout as dhx_raw_layout

class Layout:
    def __init__(self, layout_id, html="", resizable=False):
        self._raw_layout = dhx_raw_layout()
        self.content_top_id = layout_id
        self.content_top_html = html
        
        #set defaults for layout
        self.content_top = {
            "id": self.content_top_id,
            "css": "",
            "html": self.content_top_html,
            "resizable": self._raw_layout._resizable
        }
        self.top_header = {}
        self.content_bottom = {}
        self.left_sidebar = {}
        self.right_sidebar = {}
        self.bottom_footer = {}

    def init_layout(self):
        self.config = {
			"css": "dhx_layout-cell--bordered",
			"rows": [
				self.top_header,
				{
					"cols": [
						self.left_sidebar,
						{
                            "rows": [self.content_top,
                                     self.content_bottom
                                    ]
						},
						self.right_sidebar,
					]
				},
                self.bottom_footer
			]
		}
        self._raw_layout.initLayout(self.config)

    def add_top_header(self, id="top_header", pixel_height=60, html=""):
        self.top_header = {
            "id": f"{id}",
            "html": f"{html}",
            "css": "dhx_layout-cell--border_bottom",
            "gravity": False,
            "height": f"{pixel_height}px",
            "resizable": self._raw_layout._resizable
        }

    def add_bottom_footer(self, id="bottom_footer", pixel_height=60, html=""):
        self.bottom_footer = {
            "id": id,
            "html": html,
            "css": "dhx_layout-cell--border_top",
            "gravity": False,
            "height": f"{pixel_height}px",
            "resizable": self._raw_layout._resizable
        }

    def add_left_side(self, id="left_side", pixel_width=200, html=""):
        self.left_sidebar = {
            "id": id,
            "html": html,
            "gravity": False,
            "css": "dhx_layout-cell--border_right",
            "width": f"{pixel_width}px",
            "resizable": self._raw_layout._resizable
		}

    def add_right_side(self, id="right_side", pixel_width=200, html=""):
        self.right_sidebar = {
            "id": id,
            "html": html,
            "gravity": False,
            "css": "dhx_layout-cell--border_right",
            "width": f"{pixel_width}px",
            "resizable": self._raw_layout._resizable
		}

    def add_content_bottom(self, id="", pixel_height=200, html=""):
        self.content_bottom = {
            "id": id,
            "html": html,
            "css": "dhx_layout-cell--border_top",
            "gravity": False,
            "height": f"{pixel_height}px",
            "resizable": self._raw_layout._resizable
        }
        

    def on_panel_hide(self, callable, ret_widget_values=[], block_signal = False):
        self._raw_layout.afterHide(
            callable.__name__,
            ret_widget_values=ret_widget_values,
            block_signal = block_signal
        )

    def on_panel_show(self, callable, ret_widget_values=[], block_signal = False):
        self.on_panel_show_callable = callable
        self._raw_layout.afterShow(
            self.on_panel_show_return,
            ret_widget_values=ret_widget_values,
            block_signal = block_signal
        )

    def on_panel_show_return(self, panel_id):
        self.on_panel_show_callable(panel_id)

    def before_panel_resize(self, callable, ret_widget_values=[], block_signal = False):
        self._raw_layout.beforeResizeStart(
            callable.__name__,
            ret_widget_values=ret_widget_values,
            block_signal = block_signal
        )

    def on_panel_resize(self, callable, ret_widget_values=[], block_signal = False):
        self._raw_layout.resize(
            callable.__name__,
            ret_widget_values=ret_widget_values,
            block_signal = block_signal
        )

    def attach_widget(self, widget, panel, config={}):
        self._raw_layout.attach(panel, widget, config)
