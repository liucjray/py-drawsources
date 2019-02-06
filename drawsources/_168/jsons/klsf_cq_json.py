from lib.sources.Source168 import *


def get_instance():
    return Source168({
        'url': 'https://api.api68.com/klsf/getHistoryLotteryInfo.do?date=&lotCode=10009',
        'resource': '168',
        'area': 'cq',
        'type': 'klsf',
    })
