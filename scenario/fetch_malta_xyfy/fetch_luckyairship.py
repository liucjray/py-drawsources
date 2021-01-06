import time
from datetime import timedelta, datetime
from lib.sources.SourceLuckyAirShip import *

for x in range(0, 365 * 15):
    date = datetime.datetime.strftime(datetime.datetime.now() - timedelta(x), '%Y-%m-%d')
    for page in range(1, 18):
        s = SourceLuckyAirShip({
            'resource': 'luckyairship',
            'type': 'xyft',
            'area': 'malta',
            'url': 'history.html?date={}&page={}'.format(date, page)
        })
        s.handle()
        # time.sleep(0.3)
