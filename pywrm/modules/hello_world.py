import os

from pywrm_widgets.layout import Layout, LayoutType


class module(Layout):
    widget_set = "dhx"

    def build_ui(self):
        self.layout1 = Layout("layout1", parent=self, html="Content", height="65vh")
        self.top1 = self.layout1.add_panel(LayoutType.top_header, panel_id="top1", panel_size="10vh", html="Top")
        assert self.top1 == self.layout1.top1
        self.layout1.add_panel(LayoutType.content_bottom, panel_id="content2", panel_size="15vh", html="Content Bottom")
        self.layout1.add_panel(LayoutType.left_side, panel_id="left1", panel_size="100", html="Left")
        self.layout1.add_panel(LayoutType.right_side, panel_id="right1", panel_size="100", html="Right")
        self.layout1.add_panel(LayoutType.bottom_footer, panel_id="bottom1", panel_size="100", html="Bottom")
        self.attach_widget(self.layout1)

    def init_main(self):
        print(self.name)
        self.build_ui()
        self.layout1.on_panel_show(self.panel_showing)
        print(self.layout1.name)

    def panel_showing(self, panel_id):
        print(f"panel {panel_id} is showing")


