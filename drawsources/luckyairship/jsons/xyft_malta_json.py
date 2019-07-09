from lib.sources.SourceLuckyAirShip import *


def get_instance():
    return SourceLuckyAirShip({
        'url': 'history.html',
        'resource': 'luckyairship',
        'area': 'malta',
        'type': 'xyft',
    })
