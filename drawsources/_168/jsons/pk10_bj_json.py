from lib.sources.Source168 import *


def get_instance():
    return Source168({
        'url': 'https://api.api68.com/pks/getPksHistoryList.do?lotCode=10001',
        'resource': '168',
        'area': 'bj',
        'type': 'pk10',
    })
