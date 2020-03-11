import time
from datetime import timedelta, datetime
from lib.sources.SourceLuckyAirShip import *

for page in range(1, 1000):

    s = SourceLuckyAirShip({
        'resource': 'luckyairship',
        'type': 'xyft',
        'area': 'malta',
        'url': 'history.html?page={}'.format(page)
    })
    s.handle()
    # time.sleep(0.3)
