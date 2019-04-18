from lib.sources.SourcePK10ME import *


def get_instance():
    return SourcePK10ME({
        'url': 'api/newest?code=xync',
        'resource': 'pk10me',
        'area': 'cq',
        'type': 'klsf',
        'headers': {
            'x-requested-with': 'XMLHttpRequest'
        }
    })
