import os

from pywrm_widgets.layout import Layout


class module(Layout):
    widget_set = "dhx"

    def build_ui(self):
        self.layout1 = Layout("layout1", parent=self, html="Content", height="65vh")
        self.layout1.add_panel("top_header", "top1", "10vh", "Top")
        self.layout1.add_panel("content_bottom", "layout2", "15vh", "Content Bottom")
        self.layout1.add_panel("left_side", "left1", "100", "Left")
        self.layout1.add_panel("right_side", "right1", "100", "Right")
        self.layout1.add_panel("bottom_footer", "bottom1", "100", "Bottom")
        self.toolbar = Toolbar()
        self.toolbar.add_button("Press Me", icon="pressme.png")
        self.attach_widget(self.toolbar)
        self.attach_widget(self.layout1)

    def init_main(self):
        print(self.name)
        self.build_ui()
        self.layout1.on_panel_show(self.panel_showing)
        print(self.layout1.name)

    def panel_showing(self, panel_id):
        print(f"panel {panel_id} is showing")


