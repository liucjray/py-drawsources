from lib.sources.SourceYHZ import *


def get_instance():
    return SourceYHZ({
        'url': '?controller=game&action=bonuscode&lotteryid=9&issuecount=30',
        'resource': 'yhz',
        'area': 'bj',
        'type': 'kl8',
    })
