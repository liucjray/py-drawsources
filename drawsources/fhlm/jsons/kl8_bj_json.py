from lib.sources.SourceFHLM import *


def get_instance():
    return SourceFHLM({
        'url': 'bjkl8.json',
        'resource': 'fhlm',
        'area': 'bj',
        'type': 'kl8',
    })
