"""
Spooler library shared global sessions for pywrm
"""
import copy
import threading

GLOBAL_SESSIONS = {}
DEFAULT_THREAD = {"spool": [], "return_spool": []}

def _default_check(session_id: str, thread_id: int = None) -> bool:
    thread_id = thread_id or threading.currentThread().ident
    empty = True
    # create session if it does not exist
    if session_id not in GLOBAL_SESSIONS:
        GLOBAL_SESSIONS[session_id] = {}
    
    # create thread if it does not exits
    if thread_id not in GLOBAL_SESSIONS[session_id]:
        GLOBAL_SESSIONS[session_id][thread_id] = DEFAULT_THREAD
    else:
        # set empty to false if thread did exist
        empty = False
    return empty

def add_item(session_id: str, item: dict):
    """Add an item to the spool to be sent to javascript"""
    thread_id = threading.currentThread().ident
    _default_check(session_id)
    GLOBAL_SESSIONS[session_id][thread_id]["spool"].append(item)

async def get_spool_item(session_id: str, thread_id: int):
    """Get the next item out of the spool for processing"""
    _default_check(session_id, thread_id)
    if GLOBAL_SESSIONS[session_id][thread_id]["spool"]:
        spool = copy.deepcopy(GLOBAL_SESSIONS[session_id][thread_id]["spool"][0])
        GLOBAL_SESSIONS[session_id][thread_id]["spool"].pop(0)
    else:
        spool = []
    return spool

def spool_has_data(session_id: str, thread_id: int):
    """Check spool for data."""
    # if default check is not empty return true
    if not _default_check(session_id, thread_id):
        if len(GLOBAL_SESSIONS[session_id][thread_id]["spool"]) > 0:
            return True
    return False

def return_thread(session_id: str, thread_id: int, item: dict):
    """Return thread blocking call return data"""
    _default_check(session_id, thread_id)
    GLOBAL_SESSIONS[session_id][thread_id]["return_spool"].append(item)

def add_widget(session_id, widget_id, widget):
    """ Add a widget in memory to a session"""
    _default_check(session_id)
    GLOBAL_SESSIONS[session_id][widget_id] = widget

def get_widget(session_id, widget_id):
    """ Get a widget from memory from a session"""
    _default_check(session_id)
    return GLOBAL_SESSIONS[session_id][widget_id]
