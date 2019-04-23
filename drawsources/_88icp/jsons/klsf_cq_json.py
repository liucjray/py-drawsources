from lib.sources.Source88ICP import *


def get_instance():
    return Source88ICP({
        'url': 'xync/ajax?ajaxHandler=GetDrawData&_=1555664914698',
        'resource': '88icp',
        'area': 'cq',
        'type': 'klsf',
    })
