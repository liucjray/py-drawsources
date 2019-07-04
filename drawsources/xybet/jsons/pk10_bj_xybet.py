from lib.sources.SourceXYBET import *


def get_instance():
    return SourceXYBET({
        'url': 'dscagamesclient/issue.do?method=recentlyCode',
        'resource': 'xybet',
        'area': 'cn',
        'type': 'pk10',
        'raw_body': 'gameid=13&pageNum=1&size=30',
    })
