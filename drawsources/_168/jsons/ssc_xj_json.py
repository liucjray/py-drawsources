from lib.sources.Source168 import *


def get_instance():
    return Source168({
        'url': 'https://api.api68.com/CQShiCai/getBaseCQShiCaiList.do?lotCode=10004',
        'resource': '168',
        'area': 'xj',
        'type': 'ssc',
    })
