from lib.sources.SourceYHZ import *


def get_instance():
    return SourceYHZ({
        'url': '?controller=game&action=bonuscode&lotteryid=1&issuecount=30',
        'resource': 'yhz',
        'area': 'cq',
        'type': 'ssc',
    })
