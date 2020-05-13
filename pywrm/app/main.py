"""
PyWRM ASGI endpoints
"""
from base64 import b64decode
from importlib import import_module
import json
import logging
import os
import sys
import time
import threading
from uuid import uuid4

from fastapi.responses import (HTMLResponse,
                               JSONResponse)

from fastapi.encoders import jsonable_encoder

from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI

from pywrm_decorators.decorators import spool_wrapper
from pywrm_spool import spooler

LOGGING = logging.getLogger('main_logger')

APP = FastAPI()

MODULE_PATH = os.path.join(os.path.dirname(__file__), "../modules/")
STATIC_PATH = os.path.join(os.path.dirname(__file__), "../static/")

sys.path.append(MODULE_PATH)

GLOBAL_CACHE = {
    "threads": {}
}

@APP.get("/", response_class=HTMLResponse)
def modulelist():
    """ Get a module list from the modules folder and display them."""
    module_files = os.listdir(MODULE_PATH)
    python_files = [f'<a href="/{afile.replace(".py","")}">'+afile+"<a>"
                    for afile in module_files
                    if "py" in afile[-2:]]
    modules = '<br>'.join(python_files)
    return f"<html>{modules}</html>"

@APP.get("/{moduleName}", response_class=HTMLResponse)
def entrypoint(template: str = "main"):
    """ Main template entrypoint"""
    template_file = os.path.join(STATIC_PATH, f"pywrm/{template}.html")
    main_template = open(template_file, "r").read()
    upd_template = main_template.replace("|UPDATEID|", str(uuid4()))
    return upd_template

def mainwindow(session_id, location):
    """Handle mainwindow initialization from event for opening application."""
    module = location.split("/")[-1]
    mainmodule = import_module(module).module
    mainmodule("mainwindow", None, session_id=session_id).init_main()

def get_thread_response(session_id, function, args):
    """ Create a thread and get the response from a triggered event"""
    function = spool_wrapper(session_id)(function)
    spool_thread = threading.Thread(target=function, args=args)
    spool_thread.start()
    thread_id = spool_thread.ident
    GLOBAL_CACHE["threads"][thread_id] = spool_thread
    response = []
    for _ in range(0, 1000):
        res = spooler.get_spool_item(session_id, thread_id)
        if res:
            response.append(res)
            if res["type"] in ["blocking_function", "done"]:
                break
        time.sleep(0.2)
    else:
        raise TimeoutError("Never got done or blocking_function from spool")
    return response

@APP.post("/initmodule", response_class=JSONResponse)
async def initmodule(session_id: str, location: str, utcoffset: str):
    """ Initialize a module or an application and start a new session"""
    #TODO implement the passing of utcoffset into module during init
    response = get_thread_response(session_id, mainwindow, (session_id, location, ))
    return jsonable_encoder(response)

@APP.post("/runfunction", response_class=JSONResponse)
async def runfunction(args: str, session_id: str, widget_id: str, return_event: str):
    """ Run a function for an already initialized session"""
    widget = spooler.get_widget(session_id, widget_id)
    function = getattr(widget, return_event)
    arguments = json.loads(b64decode(args).decode())
    response = get_thread_response(session_id, function, arguments)
    return jsonable_encoder(response)

@APP.post("/returnthread", response_class=JSONResponse)
def returnthread(args: str, session_id: str, thread_id: str):
    """ return data from blocking call"""
    spooler.return_thread(session_id, thread_id, args)

APP.mount("/static", StaticFiles(directory=STATIC_PATH), name="static")
