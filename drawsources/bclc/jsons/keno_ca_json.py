from lib.sources.SourceBclc import *


def get_instance():
    return SourceBclc({
        'resource': 'bclc',
        'url': 'services2/keno/draw/latest/today',
        'area': 'ca',
        'type': 'keno',
        'proxies': {
            'https': '149.56.102.220:3128'
        }
    })
