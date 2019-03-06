from lib.sources.SourceLuckyAirShip import *


def get_instance():
    return SourceLuckyAirShip({
        'url': 'api/getwiningnumbers.ashx',
        'resource': 'luckyairship',
        'area': 'malta',
        'type': 'xyft',
    })
