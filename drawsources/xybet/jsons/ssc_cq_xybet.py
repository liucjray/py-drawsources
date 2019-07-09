from lib.sources.SourceXYBET import *


def get_instance():
    return SourceXYBET({
        'url': 'dscagamesclient/issue.do?method=recentlyCode',
        'resource': 'xybet',
        'area': 'cq',
        'type': 'ssc',
        'raw_body': 'gameid=1&pageNum=1&size=30',
    })
