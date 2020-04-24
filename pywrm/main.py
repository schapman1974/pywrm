import logging
import os
import platform
import sys
import yaml

import uvicorn

from app import main
from pywrm_spool import spooler


uvicorn.run(
    main.app,
    host="localhost", 
    port=8080, 
    log_level="debug",
    access_log="access.log",
    reload=False
)