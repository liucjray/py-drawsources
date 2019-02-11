from lib.sources.Source168 import *


def get_instance():
    return Source168({
        'url': 'CQShiCai/getBaseCQShiCaiList.do?lotCode=10002',
        'resource': '168',
        'area': 'cq',
        'type': 'ssc',
    })
