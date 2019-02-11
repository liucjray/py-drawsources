from lib.sources.Source168 import *


def get_instance():
    return Source168({
        'url': 'http://api.api68.com/ElevenFive/getElevenFiveList.do?date=&lotCode=10006',
        'resource': '168',
        'area': 'gd',
        'type': 'n115',
    })
