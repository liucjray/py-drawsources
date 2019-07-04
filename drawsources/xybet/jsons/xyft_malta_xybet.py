from lib.sources.SourceXYBET import *


def get_instance():
    return SourceXYBET({
        'url': 'dscagamesclient/issue.do?method=recentlyCode',
        'resource': 'xybet',
        'area': 'malta',
        'type': 'xyft',
        'raw_body': 'gameid=39&pageNum=1&size=30',
    })
