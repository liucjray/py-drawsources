from lib.sources.SourceAHFC import *


def get_instance():
    return SourceAHFC({
        'resource': 'ahfc',
        'area': 'ah',
        'type': 'k3',
    })
