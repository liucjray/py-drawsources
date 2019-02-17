from lib.sources.SourceBCQ import *


def get_instance():
    return SourceBCQ({
        'resource': 'bcq',
        'area': 'bj',
        'type': 'pk10',
        'payload': {"page": 1, "actionType": "Bjpk10"}
    })
