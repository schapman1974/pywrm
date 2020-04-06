"""
PyWRM ASGI endpoints
"""
import os
import json
import logging

from fastapi.requests import Request
from fastapi.responses import (FileResponse,
                               HTMLResponse,
                               PlainTextResponse,
                               Response)

from fastapi.staticfiles import StaticFiles
from fastapi import Depends, FastAPI, Header, HTTPException

logging = logging.getLogger('main_logger')

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def modulelist(template: str, unique_id: str):
    """ Get a module list from the modules folder and display them."""
    modules = '<br>'.join(os.listdir("modules"))
    return f"<html>{modules}</html>"
    
@app.get("/{moduleName}", response_class=HTMLResponse)
def entrypoint(template: str = "main"):
    """ Main template entrypoint"""
    template_file = os.path.join("static" , f"{template}.html")
    main_template = open(template_file, "r").read()
    return main_template