"""
PyWRM uvicorn launcher
"""

import uvicorn

from app import main


uvicorn.run(
    main.APP,
    host="0.0.0.0",
    port=8090,
    log_level="debug",
    access_log="access.log",
    reload=False
)
