from lib.sources.SourceApiLottery import *


def get_instance():
    return SourceApiLottery({
        'url': 'free/cqkl10f',
        'resource': 'apilottery',
        'area': 'cq',
        'type': 'klsf',
    })
