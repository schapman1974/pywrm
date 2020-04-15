from external_widgets.dhx.dhx_layout import Layout as dhx_layout
w2ui_layout = object
#from external_widgets.w2ui.w2ui_layout import Layout as w2ui_layout

class Layout(object):
     widget_class = "default"

     def __new__(cls, *args, **kwargs):
        if cls.widget_class in ["dhx", "default"]:
            class selected(cls, dhx_layout):
                pass
        elif cls.widget_class == "w2ui":
            class selected(cls, w2ui_layout):
                pass
        else:
            raise Exception("Invalid widgetset selected")
        selected.__name__ = cls.__name__
        return object.__new__(selected, *args, **kwargs)
     
     def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
