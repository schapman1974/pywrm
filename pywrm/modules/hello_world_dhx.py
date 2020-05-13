import os

from pywrm_widgets.layout import Layout, PanelType, Panel


class module(Layout):
    widget_set = "dhx"

    def build_ui(self):
        """ Build user interface"""

        # add layout with content LAYER 1
        self.layout1 = Layout("layout1", parent=self)
        self.content1 = Panel(panel_type=PanelType.content_top, panel_id="content1", html="Content Top")
        self.content2 = Panel(panel_type=PanelType.content_bottom, panel_id="content2", html="Content Bottom")
        self.top1 = Panel(panel_type=PanelType.top_header, panel_id="top1", html="Top")
        # Example of controling panel parameters from outside the panel
        self.top1.height = "15%"
        self.bottom1 = Panel(panel_type=PanelType.bottom_footer, panel_id="bottom1", html="Bottom")
        # Example of controling panel parameters from outside the panel
        self.bottom1.height = "15%"
        self.left1 = Panel(panel_type=PanelType.left_side, panel_id="left1", html="Left")
        self.right1 = Panel(panel_type=PanelType.right_side, panel_id="right1", html="Right")
        self.layout1.add_panels(self.content1, self.top1, self.content2, self.left1, self.right1, self.bottom1)
        self.attach_widget(self.layout1)

        # add layout2 to content1 panel LAYER 2
        # Parent of a layout should always be another layout
        self.layout2 = Layout("layout2", parent=self.layout1)
        self.l2top = Panel(panel_type=PanelType.top_header, panel_id="l2top", html="l2Top", height="50%")
        self.l2bottom = Panel(panel_type=PanelType.bottom_footer, panel_id="l2bottom", html="l2Bottom", height="50%", css="")
        self.layout2.add_panels(self.l2top, self.l2bottom)
        self.content1.attach_widget(self.layout2)

        # LAYER 3
        self.layout3 = Layout("layout3", parent=self.layout2)
        self.l3left = Panel(panel_type=PanelType.left_side, panel_id="l3left", html="l3left", width="50%", height="100%")
        self.l3right = Panel(panel_type=PanelType.right_side, panel_id="l3right", html="l3right", width="50%", height="100%", css="")
        self.layout3.add_panels(self.l3left, self.l3right)
        self.l2bottom.attach_widget(self.layout3)

        # LAYER 4
        self.layout4 = Layout("layout4", parent=self.layout3)
        self.l4top = Panel(panel_type=PanelType.top_header, panel_id="l4top", html="l4Top", height="50%")
        self.l4bottom = Panel(panel_type=PanelType.bottom_footer, panel_id="l4bottom", html="l4Bottom", height="50%", css="")
        self.layout4.add_panels(self.l4top, self.l4bottom)
        self.l3right.attach_widget(self.layout4)

    def init_main(self):
        """ Init main is a subclassed function run during startup of application"""
        self.build_ui()
        self.layout3.on_panel_hide(self.panel_hidden)
        self.l3right.hide()
        self.layout3.on_panel_show(self.panel_shown)

    def panel_shown(self, panel_id):
        """Triggered when the on panel show event happens"""
        print(f"panel {panel_id} is shown")

    def panel_hidden(self, panel_id):
        """Triggered when the on panel hide event happens"""
        print(f"panel {panel_id} is hidden")
        self.l3right.show()
