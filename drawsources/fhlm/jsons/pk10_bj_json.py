from lib.sources.SourceFHLM import *


def get_instance():
    return SourceFHLM({
        'url': 'bjpk10.json',
        'resource': 'fhlm',
        'area': 'bj',
        'type': 'pk10',
    })
