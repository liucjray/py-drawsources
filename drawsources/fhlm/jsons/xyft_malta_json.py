from lib.sources.SourceFHLM import *


def get_instance():
    return SourceFHLM({
        'url': 'xyft.json',
        'resource': 'fhlm',
        'area': 'malta',
        'type': 'pk10',
    })
