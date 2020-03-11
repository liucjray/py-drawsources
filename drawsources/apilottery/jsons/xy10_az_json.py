from lib.sources.SourceApiLottery import *


def get_instance():
    return SourceApiLottery({
        'url': 'his/azxy10',
        'resource': 'apilottery',
        'area': 'az',
        'type': 'xy10',
    })
