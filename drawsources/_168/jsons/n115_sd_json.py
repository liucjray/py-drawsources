from lib.sources.Source168 import *


def get_instance():
    return Source168({
        'url': 'https://api.api68.com/ElevenFive/getElevenFiveList.do?date=&lotCode=10008',
        'resource': '168',
        'area': 'sd',
        'type': 'n115',
    })
