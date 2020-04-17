from .raw_widgets_dhx import Layout as dhx_raw_layout

class Layout:
    def __init__(self, *args, **kwargs):
        self._raw_layout = dhx_raw_layout()

    def to_vdom(self):
        self._raw_layout.toVDOM()

    def remove_cell(self, id):
        self._raw_layout.removeCell(id)

    def add_cell(self, config,  index):
        self._raw_layout.addCell(config, index)

    def get_id(self, index):
        self._raw_layout.getId()

    def get_refs(self, name):
        pass

    def get_cell(self, id):
        pass

    def for_each(self, cb,  parent,  level):
        pass

    def cell(self, id):
        pass

    def before_show(self, callable):
        """JS_ARGS: types_1.LayoutEvents.beforeShow, [this.id])) {"""
        pass

    def after_show(self):
        """JS_ARGS: NO ARGS"""
        pass

    def beforeHide(self, arg0):
        """JS_ARGS: types_1.LayoutEvents.beforeHide, [this.id])) {"""
        pass

    def afterHide(self, arg0):
        """JS_ARGS: types_1.LayoutEvents.afterHide, [this.id]);"""
        pass

    def beforeResizeStart(self, arg0):
        """JS_ARGS: types_1.LayoutEvents.beforeResizeStart, [_this.id])) {"""
        pass

    def resize(self, arg0):
        """JS_ARGS: types_1.LayoutEvents.resize, [_this.id]);"""
        pass

    def afterResizeEnd(self, arg0):
        """JS_ARGS: types_1.LayoutEvents.afterResizeEnd, [_this.id]);"""
        pass

    def beforeAdd(self, arg0):
        """JS_ARGS: types_1.LayoutEvents.beforeAdd, [config.id])) {"""
        pass

    def afterAdd(self, arg0):
        """JS_ARGS: types_1.LayoutEvents.afterAdd, [config.id])) {"""
        pass

    def beforeRemove(self, arg0):
        """JS_ARGS: types_1.LayoutEvents.beforeRemove, [id])) {"""
        pass

    def afterRemove(self, arg0):
        """JS_ARGS: types_1.LayoutEvents.afterRemove, [id]);"""
        pass

    def beforeCollapse(self, arg0):
        """JS_ARGS: types_1.LayoutEvents.beforeCollapse, [this.id])) {"""
        pass

    def afterCollapse(self, arg0):
        """JS_ARGS: types_1.LayoutEvents.afterCollapse, [this.id]);"""
        pass

    def beforeExpand(self, arg0):
        """JS_ARGS: types_1.LayoutEvents.beforeExpand, [this.id])) {"""
        pass

    def afterExpand(self, arg0):
        """JS_ARGS: types_1.LayoutEvents.afterExpand, [this.id]);"""
        pass

