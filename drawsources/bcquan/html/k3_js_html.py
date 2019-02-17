from lib.sources.SourceBCQ import *


def get_instance():
    return SourceBCQ({
        'resource': 'bcq',
        'area': 'js',
        'type': 'k3',
        'payload': {"page": 1, "actionType": "Jsk3"}
    })
