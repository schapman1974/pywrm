from io import BytesIO
import requests
from zipfile import ZipFile


class parser:
    def __init__(self):
        self._classes = {}
        self._js_lib = []
        self.version = "6.4.2"
        self.js_zip_source = "https://dhtmlx.com/x/download/suite/suite_gpl.zip"
        self.js_source_file = "codebase/suite.js"
        self.widget_code = "dhx"
        self.widget_list = [
            "Calendar",
            "Chart",
            "Colorpicker",
            "Combobox",
            "DataView",
            "Form",
            "Grid",
            "Layout",
            "List",
            "Menu",
            "Popup",
            "Ribbon",
            "Sidebar",
            "Slider",
            "Tabbar",
            "Timepicker",
            "Toolbar",
            "Tree",
            "Window"
        ]

    def _get_suite_zipfile(self):
        response = requests.get(self.js_zip_source).content
        zipfile = ZipFile(BytesIO(response))
        self._js_lib = zipfile.read(self.js_source_file).decode().split("\n")

    def get_js_classes(self):
        for jsline in self._js_lib:
            if "@class" in jsline:
                classname = jsline.split("var ")[1].split(" =")[0]
                self._classes[classname] = {"functions": [], "events": []}
        for widget in self.widget_list:
            if not widget in self._classes:
                raise Exception(f"Missing class for {widget} from {self.js_source_file}")

    def get_js_functions(self):
        for jsline in self._js_lib:
            for class_entry in self._classes:
                if class_entry+".prototype" in jsline and "function" in jsline:
                    if "prototype._" not in jsline:
                        function =  jsline.split("prototype.")[1].split(" ")[0]
                        params = jsline.split("(")[1].split(")")[0]
                        self._classes[class_entry]["functions"].append({
                            "name":function,
                            "params": params.split(",") 
                                if params else []
                            }
                        )

    def get_js_events(self):
        events = []
        for jsline in self._js_lib:
            if "var" in jsline and "Events;" in jsline:
                eventname = jsline.split("var ")[1].split(";")[0]
                events.append(eventname)

            for event in events:
                if event+"[" in jsline and "=" in jsline:
                    eventtype = jsline.split('"')[1]
                    classname = event.replace("Events", "")
                    if classname in self._classes:
                        self._classes[classname]["events"].append(eventtype)

    def build_widget_info(self):
        self._get_suite_zipfile()
        self.get_js_classes()
        self.get_js_functions()
        self.get_js_events()
