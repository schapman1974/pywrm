import copy

GLOBAL_SESSIONS = {}

def add_item(session_id, item):
    if session_id not in GLOBAL_SESSIONS:
        GLOBAL_SESSIONS[session_id] = {"spool": []}
    GLOBAL_SESSIONS[session_id]["spool"].append(item)

def get_spool(session_id):
    spool = copy.deepcopy(GLOBAL_SESSIONS[session_id]["spool"])
    GLOBAL_SESSIONS[session_id]["spool"] = []
    return spool

def add_widget(session_id, widget_id, widget):
    if session_id not in GLOBAL_SESSIONS:
        GLOBAL_SESSIONS[session_id] = {"spool": []}
    GLOBAL_SESSIONS[session_id][widget_id] = widget

def get_widget(session_id, widget_id):
    return GLOBAL_SESSIONS[session_id][widget_id]