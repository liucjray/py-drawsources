from lib.sources.Source168 import *


def get_instance():
    return Source168({
        'url': 'http://api.api68.com/klsf/getHistoryLotteryInfo.do?date=&lotCode=10005',
        'resource': '168',
        'area': 'gd',
        'type': 'klsf',
    })
