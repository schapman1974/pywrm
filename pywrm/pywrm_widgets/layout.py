import copy

from external_widgets.dhx.dhx_layout import Layout as dhx_layout
from external_widgets.w2ui.w2ui_layout import Layout as w2ui_layout


class Panel:
    def __init__(self, panel_type, panel_id, **kwargs):
        self.panel_type = panel_type
        self.panel_id = panel_id
        self.kwargs = kwargs
        self.panel_type_info = None
        self.parent = None
        #TODO check kwargs against property setters and raise if not there
        self.config = {
            "id": panel_id,
            **kwargs
        }

    def build_defaults(self, parent):
        self.parent = parent
        self.panel_type_info = self.parent._base_layout.panel_type_info[self.panel_type]
        panel_defaults = {k.replace("panel_default_", ""):v 
                          for k,v in self.panel_type_info.items() 
                          if "panel_default_" in k}
        
        # config should update panel_defaults so user values take precedence
        panel_defaults.update(self.config)
        self.config = panel_defaults

    def attach_widget(self, widget):
        """attach a widget to the panel"""
        self.parent.attach_widget(widget, self)

    def collapse(self):
        self.parent.collapse(self)

    def expand(self):
        self.parent.expand(self)

    def hide(self):
        self.parent.hide(self)

    def show(self):
        self.parent.show(self)

    def toggle(self):
        self.parent.toggle(self)

    @property
    def style(self) -> str:
        return self.config.get("css", "")

    @style.setter
    def style(self, value: str):
        """the name of a CSS class(es) applied to Layout"""
        self.config["css"] = value

    @property
    def title_text(self) -> str:
        return self.config.get("header", "")

    @title_text.setter
    def title_text(self, value: str):
        """adds a header with text for a cell"""
        self.config["header"] = value

    @property
    def height(self) -> str:
        return self.config.get("height", "")

    @height.setter
    def height(self, value: str):
        """sets the height of a cell depending on the panel type"""
        self.config["height"] = value

    @property
    def width(self) -> str:
        return self.config.get("width", "")

    @width.setter
    def width(self, value: str):
        """sets the width of a cell depending on the panel type"""
        self.config["width"] = value

    @property
    def hidden(self):
        return self.config.get("hidden", False)

    @hidden.setter
    def hidden(self, value: bool):
        """defines whether a cell is hidden"""
        self.config["hidden"] = value

    @property
    def html(self):
        return self.config.get("html", "")

    @html.setter
    def html(self, value: str):
        """sets HTML content for a cell"""
        self.config["html"] = value

    @property
    def resizable(self):
        return self.config.get("resizable", False)

    @resizable.setter
    def resizable(self, value: bool):
        """defines whether a cell can be resized"""
        self.config["resizable"] = value


class PanelType:
    content_top = "content_top"
    top_header = "top_header"
    bottom_footer = "bottom_footer"
    left_side = "left_side"
    right_side = "right_side"
    content_bottom = "content_bottom"


class Layout:
    widget_set = None

    def __init__(self, layout_id, parent=None, session_id=""):
        widget_set = self.widget_set if self.widget_set else (parent.widget_set if parent else None)
        self.parent = parent
        self.session_id = session_id or self.parent.session_id
        self.name = layout_id
        self._has_panel = False

        if widget_set == "dhx":
            self._base_layout = dhx_layout(layout_id, session_id=self.session_id, parent=parent)
        elif widget_set == "w2ui":
            self._base_layout = w2ui_layout(layout_id, session_id=self.session_id, parent=parent)
        else:
            raise ValueError("Widgetset is not defined")
        if self.name == "mainwindow":
            self.init_widget()
        else:
            self.widget_set = parent.widget_set

        self.on_panel_hide_callable = None
        self.on_panel_show_callable = None
        self.on_panel_resize_callable = None
        self.before_panel_resize_callable = None

    def init_widget(self):
        self._base_layout.init_layout(self._has_panel, self.name)

    def add_panels(self, *panels):
        """Add panel to layout top_header, bottom_footer, left_side, right_side, content_bottom"""
        for apanel in panels:
            apanel.build_defaults(self)
            add_function = getattr(self._base_layout, f"add_{str(apanel.panel_type)}")
            add_function(**apanel.config)
            setattr(self, apanel.panel_id, apanel)
            self._has_panel = True

    def hide(self, panel):
        self._base_layout.hide_panel(panel.panel_id)

    def repaint(self):
        self._base_layout.repaint()

    def show(self, panel):
        self._base_layout.show_panel(panel.panel_id)

    def toggle(self, panel):
        self._base_layout.top_header(panel.panel_id)

    def on_panel_hide(self, callable, ret_widget_values=[], block_signal = False):
        ret_id_list = [widget._unique_id for widget in ret_widget_values]
        self.on_panel_hide_callable = callable
        self._base_layout.on_panel_hide(self.on_panel_hide_return, ret_id_list, block_signal)

    def on_panel_hide_return(self, panel_id):
        self.on_panel_hide_callable(panel_id)

    def on_panel_show(self, callable, ret_widget_values=[], block_signal = False):
        ret_id_list = [widget._unique_id for widget in ret_widget_values]
        self.on_panel_show_callable = callable
        self._base_layout.on_panel_show(self.on_panel_show_return, ret_id_list, block_signal)

    def on_panel_show_return(self, panel_id):
        self.on_panel_show_callable(panel_id)

    def on_panel_resize(self, callable, ret_widget_values=[], block_signal = False):
        ret_id_list = [widget._unique_id for widget in ret_widget_values]
        self.on_panel_resize_callable = callable
        self._base_layout.on_panel_resize(self.on_panel_resize_return, ret_id_list, block_signal)

    def on_panel_resize_return(self, panel_id):
        self.on_panel_resize_callable(panel_id)

    def before_panel_resize(self, callable, ret_widget_values=[], block_signal = False):
        ret_id_list = [widget._unique_id for widget in ret_widget_values]
        self.before_panel_resize_callable = callable
        self._base_layout.before_panel_resize(self.before_panel_resize_return, ret_id_list, block_signal)

    def before_panel_resize_return(self, panel_id):
        self.before_panel_resize_callable(panel_id)

    def attach_widget(self, widget, panel=None):
        uid = widget._base_layout._raw_layout._unique_id
        panel_id = panel.panel_id if panel else None
        config = widget._base_layout._build_config()
        self._base_layout.attach_widget(uid, panel_id or self.name, config)


        
        

