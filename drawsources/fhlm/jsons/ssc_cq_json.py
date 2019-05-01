from lib.sources.SourceFHLM import *


def get_instance():
    return SourceFHLM({
        'url': 'cqssc.json',
        'resource': 'fhlm',
        'area': 'cq',
        'type': 'ssc',
    })
