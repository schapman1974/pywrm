from external_widgets.dhx.dhx_layout import Layout as dhx_layout
from external_widgets.w2ui.w2ui_layout import Layout as w2ui_layout

class Layout:
    widget_set = None

    def __init__(self, layout_id, parent=None, html="", height="100vh"):
        widget_set = self.widget_set if self.widget_set else (parent.widget_set if parent else None)
        self._initialized = False
        self.name = layout_id

        if widget_set == "dhx":
            self._base_layout = dhx_layout(layout_id, html=html, height=height)
        elif widget_set == "w2ui":
            self._base_layout = w2ui_layout(layout_id, html=html, height=height)
        else:
            raise ValueError("Widgetset is not defined")
        if self.name == "mainwindow":
            self.init_widget()

        self.on_panel_show_callable = None

    def init_widget(self):
        self._base_layout.init_layout()
        self._initialized = True

    def add_panel(self, panel_type, panel_id, panel_size, html=""):
        """Add panel to layout top_header, bottom_footer, left_sidebar, right_sidebar, content_bottom"""
        add_function = getattr(self._base_layout, f"add_{panel_type}")
        add_function(panel_id, panel_size, html)

    def on_panel_show(self, callable, ret_widget_values=[], block_signal = False):
        ret_id_list = [widget._unique_id for widget in ret_widget_values]
        self.on_panel_show_callable = callable
        self._base_layout.on_panel_show(self.on_panel_show_return, ret_id_list, block_signal)

    def on_panel_show_return(self, panel_id):
        self.on_panel_show_callable(panel_id)

    def attach_widget(self, widget, panel_id=""):
        uid = widget._base_layout._raw_layout._unique_id
        config = widget._base_layout._build_config()
        self._base_layout.attach_widget(uid, panel_id or self.name, config)
