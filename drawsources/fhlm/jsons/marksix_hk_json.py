from lib.sources.SourceFHLM import *


def get_instance():
    return SourceFHLM({
        'url': 'lhc.json',
        'resource': 'fhlm',
        'area': 'hk',
        'type': 'marksix',
    })
