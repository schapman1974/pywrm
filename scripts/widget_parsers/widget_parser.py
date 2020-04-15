import argparse
from glob import glob
from importlib import import_module
import os
import sys

EIGHTSPC = " " * 8
FOURSPC = " " * 4

def build_raw_classes(parser, repo_folder):
    classes = parser.widget_list
    build_folder = os.path.join(repo_folder,
                                f"external_widgets{os.path.sep}",
                                parser.widget_code
                                )
    os.makedirs(build_folder, exist_ok=True)
    raw_file = os.path.join(build_folder,
                            f"raw_widgets_{parser.widget_code}.py"
                            )
    with open(raw_file, "w") as rfile:
        rfile.write(f'""" Auto Generated raw classes for {parser.widget_code}. """\n')
        for widget_class in classes:
            widget_info = parser._classes[widget_class]
            rfile.write(f"\n\nclass {widget_class}:\n")
            rfile.write(f"{FOURSPC}def __init__(self):\n")
            rfile.write(f"{EIGHTSPC}pass\n")
            for jsfunction in widget_info["functions"]:
                rfile.write(f"\n{FOURSPC}def {jsfunction['name']}(self")
                if jsfunction["params"]:
                    rfile.write(", " + (", ".join(jsfunction["params"])))
                rfile.write("):\n")
                rfile.write(f"{EIGHTSPC}pass\n")
            for jsevent, jsevent_info in widget_info["events"].items():
                rfile.write(f"\n{FOURSPC}def {jsevent}(self")
                for argnum in range(0, jsevent_info["argslen"]):
                    if argnum == 0:
                        rfile.write(", ")
                    rfile.write(f"arg{argnum}")
                    if argnum < jsevent_info["argslen"]-1:
                        rfile.write(", ")
                rfile.write("):\n")
                rfile.write(f'{EIGHTSPC}"""JS_ARGS: {jsevent_info["argstr"]}"""\n')
                rfile.write(f"{EIGHTSPC}pass\n")
        

def run_parsers(repo_folder):
    folder = os.path.join(
        os.path.dirname(__file__),
         f"parsers{os.path.sep}*.py"
    )
    files = glob(folder)
    for parse_file in files:
        file_only = parse_file.split(os.path.sep)[-1]
        sys.path.append(os.path.dirname(parse_file))
        parsemod = import_module(file_only.replace(".py", ""))
        parser = parsemod.parser()
        parser.build_widget_info()
        build_raw_classes(parser, repo_folder)


if __name__ == "__main__":
    #get and parse arguments
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        '--pywrm_project_path',
        help='path to pywrm project',
        default= f"pywrm/"
    )
    args = arg_parser.parse_args()
    run_parsers(args.pywrm_project_path)