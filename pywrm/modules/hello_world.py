import os

from pywrm_widgets.layout import Layout


class module(Layout):
    widget_set = "dhx"

    def build_ui(self):
        self.layout1 = Layout("layout1", parent=self)
        self.attach_widget(self.layout1, "content_top")

    def init_main(self):
        print(self.name)
        self.build_ui()
        self.layout1.on_panel_show(self.panel_showing)
        print(self.layout1.name)

    def panel_showing(self, panel_id):
        print(f"panel {panel_id} is showing")


