from lib.sources.Source168 import *


def get_instance():
    return Source168({
        'url': 'http://api.1680210.com/CQShiCai/getBaseCQShiCaiList.do?lotCode=10003',
        'resource': '168',
        'area': 'tj',
        'type': 'ssc',
    })
