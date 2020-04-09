import argparse
from glob import glob
from importlib import import_module
import os
import sys


def run_parsers(write_folder):
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
        print(parser._classes)


if __name__ == "__main__":
    #get and parse arguments
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        '--pywrm_project_path',
        help='path to pywrm project',
        default= f"..{os.path.sep}..{os.path.sep}"
    )
    args = arg_parser.parse_args()
    run_parsers(args.pywrm_project_path)