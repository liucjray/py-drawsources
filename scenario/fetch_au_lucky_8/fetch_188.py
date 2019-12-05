import time
from datetime import timedelta, datetime
from lib.sources.Source188 import *

for x in range(0, 365):
    date = datetime.strftime(datetime.now() - timedelta(40) - timedelta(x), '%Y-%m-%d')
    print("############### {} #################".format(date))
    au8 = Source188({
        'resource': '188',
        'type': 'kl8',
        'area': 'au',
        'url': 'getDayData.ashx?date={}&lotCode=10011'.format(date)
    })
    au8.handle()
    time.sleep(1.5)
