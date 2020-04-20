from importlib import import_module
import os
import sys

modpath = os.path.join(os.path.dirname(__file__), "modules")
sys.path.append(modpath)
parsemod = import_module("hello_world")
mainwindow = parsemod.module("mainwindow", None)
mainwindow.init_main()
mainwindow.layout1._base_layout._raw_layout.afterShow_return({"value": "top_header"})