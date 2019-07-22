from lib.sources.SourceXYBET import *


def get_instance():
    return SourceXYBET({
        'url': 'dscagamesclient/issue.do?method=recentlyCode',
        'resource': 'xybet',
        'area': 'bj',
        'type': 'kl8',
        'raw_body': 'gameid=27&pageNum=1&size=30',
    })
