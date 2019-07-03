from lib.sources.SourceFHLM import *


def get_instance():
    return SourceFHLM({
        'url': 'gd11y.json',
        'resource': 'fhlm',
        'area': 'gd',
        'type': 'n115',
    })
