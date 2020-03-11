import time
from lib.sources.Source168 import *

for day in range(0, 30):
    # 不抓今天
    target_day = datetime.now() - timedelta(1) - timedelta(day)
    date = datetime.strftime(target_day, '%Y-%m-%d')
    print("############### {} #################".format(date))
    au8 = Source168({
        'resource': '500',
        'type': 'ssc',
        'area': 'au',
        'url': 'pks/GetPksHistoryList?date={}&lotCode=42'.format(date),
        'domain': 'https://kc.haoall.com/redisapi/index/results/',
    })
    au8.handle()
    time.sleep(0.3)
