import copy

SPOOLITEMS = []

def add_item(item):
    global SPOOLITEMS
    SPOOLITEMS.append(item)

def get_spool():
    global SPOOLITEMS
    spool = copy.deepcopy(SPOOLITEMS)
    SPOOLITEMS = []
    return spool