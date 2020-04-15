import ast
from io import BytesIO
import json
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
        self._event_list = []
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
                self._classes[classname] = {"functions": [], "events": {}}
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
        """ Get the javascript events """
        events = []
        for jsline in self._js_lib:
            if "var" in jsline and "Events;" in jsline:
                eventname = jsline.split("var ")[1].split(";")[0]
                events.append(eventname)
                classname = eventname.replace("Events", "")

            for event in events:
                if event+"[" in jsline and "=" in jsline:
                    eventtype = jsline.split('"')[1]
                    classname = event.replace("Events", "")
                    if classname in self._classes:
                        self._classes[classname]["events"][eventtype] = {"argslen": 0, "argstr": "NO ARGS"}
                    event_and_class = f"{event}.{eventtype}"
                    if not event_and_class in self._event_list:
                        self._event_list.append(event_and_class)

    def get_js_event_args(self):
        """ Get event argument lengths"""
        for row, jsline in enumerate(self._js_lib):
            for event_and_class in self._event_list:
                if event_and_class in jsline and ".fire" in jsline:
                    if ".fire" in jsline and "[]" not in jsline:
                        parse = jsline.split(".fire(")[1]
                        if parse.strip().endswith("[") or parse.strip().endswith("[{"):
                            inread = row + 1
                            while True:
                                injsrow = self._js_lib[inread]
                                parse += injsrow.strip()
                                if "]" in parse:
                                    break
                                elif (inread -row) < 10:
                                    inread += 1
                                else:
                                    break
                        
                        if "[" in parse:
                            tparse = str(parse)
                            if "{" in parse and "}" in parse:
                                parse = parse.split("{")[0]+"argz"+parse.split("}")[1]
                            parseparams = "['"+"','".join((parse.split("[", 1)[1].split("]")[0]).replace(" ", "").split(","))+"']"
                            parselen = len(ast.literal_eval(parseparams))
                            classname = event_and_class.split(".")[0].replace("Events", "")
                            eventtype = event_and_class.split(".")[1]
                            if classname in self._classes:
                                self._classes[classname]["events"][eventtype]["argslen"] = parselen
                                self._classes[classname]["events"][eventtype]["argstr"] = tparse


    def build_widget_info(self):
        self._get_suite_zipfile()
        self.get_js_classes()
        self.get_js_functions()
        self.get_js_events()
        self.get_js_event_args()
