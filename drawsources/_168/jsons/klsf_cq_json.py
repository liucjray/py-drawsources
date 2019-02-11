from lib.sources.Source168 import *


def get_instance():
    return Source168({
        'url': 'klsf/getHistoryLotteryInfo.do?date=&lotCode=10009',
        'resource': '168',
        'area': 'cq',
        'type': 'klsf',
    })
