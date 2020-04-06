"""
PyWRM ASGI endpoints
"""
import os
import json
import logging

from starlette.requests import Request
from starlette.responses import (FileResponse,
                                 HTMLResponse,
                                 PlainTextResponse,
                                 Response)

from starlette.staticfiles import StaticFiles
from fastapi import Depends, FastAPI, Header, HTTPException

logging = logging.getLogger('main_logger')

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def modulelist(template: str, unique_id: str):
    """ Get a module list from the modules folder and display them."""
    files = os.listdir("modules")
    modules = ""
    for afile in files:
        modules += f"{afile}<br>"
    return f"<html>{modules}</html>"
    
@app.get("/{moduleName}", response_class=HTMLResponse)
def entrypoint(template: str = "main"):
    """ Main template entrypoint"""
    template_file = os.path.join("static" , "{template}.html")
    main_template = open(template_file, "r").read()
    return main_template