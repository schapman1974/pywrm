import copy
import threading

GLOBAL_SESSIONS = {}

def add_item(session_id, item):
    """ Add an item to the spool to be sent to javascript"""
    thread_id = str(threading.currentThread().ident)
    if session_id + thread_id not in GLOBAL_SESSIONS:
        GLOBAL_SESSIONS[session_id + thread_id] = {"spool": [], "return_spool": []}
    GLOBAL_SESSIONS[session_id + thread_id]["spool"].append(item)

def get_spool_item(session_id: str, thread_id: str):
    """ Get the next item out of the spool for processing"""
    if session_id + thread_id not in GLOBAL_SESSIONS:
        GLOBAL_SESSIONS[session_id + thread_id] = {"spool": [], "return_spool": []}
    if GLOBAL_SESSIONS[session_id + thread_id]["spool"]:
        spool = copy.deepcopy(GLOBAL_SESSIONS[session_id + thread_id]["spool"][0])
        GLOBAL_SESSIONS[session_id + thread_id]["spool"].pop(0)
    else:
        spool = None
    return spool

def return_thread(session_id: str, thread_id: str, item: dict):
    GLOBAL_SESSIONS[session_id + thread_id]["return_spool"].append(item)

def add_widget(session_id, widget_id, widget):
    """ Add a widget in memory to a session"""
    if session_id not in GLOBAL_SESSIONS:
        GLOBAL_SESSIONS[session_id] = {"spool": []}
    GLOBAL_SESSIONS[session_id][widget_id] = widget

def get_widget(session_id, widget_id):
    """ Get a widget from memory from a session"""
    return GLOBAL_SESSIONS[session_id][widget_id]