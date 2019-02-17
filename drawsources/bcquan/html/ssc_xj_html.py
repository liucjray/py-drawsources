from lib.sources.SourceBCQ import *


def get_instance():
    return SourceBCQ({
        'resource': 'bcq',
        'area': 'xj',
        'type': 'ssc',
        'payload': {"page": 1, "actionType": "Xjssc"}
    })
