from lib.sources.SourceBCQ import *


def get_instance():
    return SourceBCQ({
        'resource': 'bcq',
        'area': 'cq',
        'type': 'ssc',
        'payload': {"page": 1, "actionType": "Cqssc"}
    })
