from lib.sources.SourceBCQ import *


def get_instance():
    return SourceBCQ({
        'resource': 'bcq',
        'area': 'tj',
        'type': 'ssc',
        'payload': {"page": 1, "actionType": "Tjssc"}
    })
