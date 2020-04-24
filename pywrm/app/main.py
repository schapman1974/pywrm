"""
PyWRM ASGI endpoints
"""
from importlib import import_module
import json
import logging
import os
import sys
from uuid import uuid4

from fastapi.requests import Request
from fastapi.responses import (FileResponse,
                               HTMLResponse,
                               PlainTextResponse,
                               JSONResponse,
                               Response)

from fastapi.encoders import jsonable_encoder

from fastapi.staticfiles import StaticFiles
from fastapi import Depends, FastAPI, Header, HTTPException

from pywrm_spool import spooler

logging = logging.getLogger('main_logger')

app = FastAPI()

MODULE_PATH = os.path.join(os.path.dirname(__file__),"../modules/")
STATIC_PATH = os.path.join(os.path.dirname(__file__),"../static/")

sys.path.append(MODULE_PATH)

global_cache = {}

@app.get("/", response_class=HTMLResponse)
def modulelist():
    """ Get a module list from the modules folder and display them."""
    module_files = os.listdir(MODULE_PATH)
    python_files = [f'<a href="/{afile.replace(".py","")}">'+afile+"<a>"
                    for afile in module_files
                    if "py" in afile[-2:]]
    modules = '<br>'.join(python_files)
    return f"<html>{modules}</html>"
    
@app.get("/{moduleName}", response_class=HTMLResponse)
def entrypoint(template: str = "main"):
    """ Main template entrypoint"""
    template_file = os.path.join(STATIC_PATH , f"pywrm/{template}.html")
    main_template = open(template_file, "r").read()
    upd_template = main_template.replace("|UPDATEID|", str(uuid4()))
    return upd_template

@app.post("/initmodule", response_class=JSONResponse)
def initmodule(uid: str, location: str, utcoffset: str):
    module = location.split("/")[-1]
    global_cache[uid] = import_module(module)
    mainwindow = global_cache[uid].module("mainwindow", None)
    mainwindow.init_main()
    
    response = spooler.get_spool()
    print(response)
    return jsonable_encoder(response)

@app.get("/runfunction", response_class=JSONResponse)
def runfunction():
    """ Run function"""
    return ""

app.mount("/static", StaticFiles(directory=STATIC_PATH), name="static")