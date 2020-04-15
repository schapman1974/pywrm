from .raw_widgets_dhx import Layout as dhx_raw_layout

class Layout(dhx_raw_layout):
    def __init__(self, *args, **kwargs):
        dhx_raw_layout.__init__(self, *args, **kwargs)