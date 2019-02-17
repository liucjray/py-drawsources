from lib.sources.SourceBCQ import *


def get_instance():
    return SourceBCQ({
        'resource': 'bcq',
        'area': 'sd',
        'type': 'n115',
        'payload': {"page": 1, "actionType": "Sd11y"}
    })
