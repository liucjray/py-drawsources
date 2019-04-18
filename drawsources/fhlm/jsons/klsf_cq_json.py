from lib.sources.SourceFHLM import *


def get_instance():
    return SourceFHLM({
        'url': 'cq10f.json',
        'resource': 'fhlm',
        'area': 'cq',
        'type': 'klsf',
    })
