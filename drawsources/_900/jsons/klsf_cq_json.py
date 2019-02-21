from lib.sources.Source900 import *


def get_instance():
    return Source900({
        'url': '?r=home/history/xync',
        'resource': '900',
        'area': 'cq',
        'type': 'klsf',
    })
