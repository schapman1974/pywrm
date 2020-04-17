from pywrm_widgets.layout import Layout
from pywrm_widgets.grid import Grid

class module(Layout):
    def build_ui(self):
        self.layout1 = Layout()
        self.form1 = Form()
        self.form1 = {}
        self.layout1.add_widget(self.form1)
        self.toolbar1 = Toolbar()
        self.toolbar1.set_orientation("top")
        self.add_widget(self.toolbar1)
        self.grid1 = Grid()

    def init_main(self):
        self.build_ui()
        self.grid1.on_row_dbl_click(self.handle_click, return_values=[self.form1, self.form2])
        self.add_widget(self.grid1, "1")
        self.fill_grid()

    def fill_grid(self):
        self.grid1.clear()
        self.grid1.set_headers(["header1", "header2"])
        self.grid1.load([["key1", "test", "test"],
                         ["key2", "test", "test"]])

    def handle_click(self, row, row_key):
        self.message_box(f"Row {row}")
        self.form1.edit_box1 = "test"
        self.form1.edit_box2 = "test2"
        self.flush_ui()
        self.form1.edit_box1 - self.form1.edit_box2
        #invisible flush

