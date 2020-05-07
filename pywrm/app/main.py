"""
PyWRM ASGI endpoints
"""
from importlib import import_module
import json
import logging
import os
import sys
import threading
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

from decorators.decorators import spool_wrapper
from pywrm_spool import spooler

logging = logging.getLogger('main_logger')

app = FastAPI()

MODULE_PATH = os.path.join(os.path.dirname(__file__),"../modules/")
STATIC_PATH = os.path.join(os.path.dirname(__file__),"../static/")

sys.path.append(MODULE_PATH)

global_cache = {
    "threads": {}
}

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

def mainwindow(session_id, location):
    """Handle mainwindow initialization from event for opening application."""
    module = location.split("/")[-1]
    mainmodule = import_module(module).module
    mainmodule("mainwindow", None, session_id=session_id).init_main()

def get_thread_response(session_id, function, args):
    """ Create a thread and get the response from a triggered event"""
    function = spool_wrapper(session_id)(function)
    t = threading.Thread(target=function, args=args)
    t.start()
    thread_id = str(t.ident)
    global_cache["threads"][thread_id] = t
    response = []
    while True:
        res = spooler.get_spool_item(session_id, thread_id)
        if res:
            response.append(res)
            if res["type"] in ["blocking_function", "done"]:
                break
    return response

@app.post("/initmodule", response_class=JSONResponse)
async def initmodule(session_id: str, location: str, utcoffset: str):
    """ Initialize a module or an application and start a new session"""
    response = get_thread_response(session_id, mainwindow, (session_id, location, ))
    return jsonable_encoder(response)

@app.post("/runfunction", response_class=JSONResponse)
async def runfunction(args, session_id, widget_id, return_event):
    """ Run a function for an already initialized session"""
    widget = spooler.get_widget(session_id, widget_id)
    function = getattr(widget, return_event)
    response = get_thread_response(session_id, function, (args,))
    return jsonable_encoder(response)

@app.post("/returnthread", response_class=JSONResponse)
def returnthread(args, session_id, thread_id):
    """ return data from blocking call"""

    spooler.return_thread(session_id, thread_id, args)
    pass
    
app.mount("/static", StaticFiles(directory=STATIC_PATH), name="static")