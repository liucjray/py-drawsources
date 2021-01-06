from lib.sources.SourceThaihuay import *


def get_instance():
    return SourceThaihuay({
        'resource': 'thaihuay',
        'type': 'article',
        'area': 'thai',
        'url': 'tag/เลขเด็ดงวดนี้/',
    })
