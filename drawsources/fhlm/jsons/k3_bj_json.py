from lib.sources.SourceFHLM import *


def get_instance():
    return SourceFHLM({
        'url': 'bjk3.json',
        'resource': 'fhlm',
        'area': 'bj',
        'type': 'k3',
    })
