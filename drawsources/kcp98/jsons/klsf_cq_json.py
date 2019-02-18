from lib.sources.SourceKCP98 import *


def get_instance():
    return SourceKCP98({
        'uri': 'go/open.php',
        'method': 'post',
        'payload': {'my1': 10},
        'resource': 'kcp98',
        'area': 'cq',
        'type': 'klsf',
    })
