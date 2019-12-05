import time
from datetime import timedelta, datetime
from lib.sources.SourceAuLuckyLottery8 import *

# 爬一年
for x in range(0, 365):
    date = datetime.strftime(datetime.now() - timedelta(x), '%Y-%m-%d')
    au8 = SourceAuLuckyLottery8({
        'resource': 'auluckylottery',
        'type': 'kl8',
        'area': 'au',
        'url': '?date={}'.format(date)
    })
    au8.handle()
    time.sleep(0.01)
