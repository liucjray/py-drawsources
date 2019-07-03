from lib.sources.SourceBBIN import *


def get_instance():
    return SourceBBIN({
        'url': '',
        'resource': 'bbin',
        'area': 'cn',
        'type': 'bjkl8',
    })
