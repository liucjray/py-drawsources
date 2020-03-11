import time
from lib.sources.Source163v2 import *

for day in range(0, 30):
    # 不抓今天
    target_day = datetime.datetime.now() - datetime.timedelta(1) - datetime.timedelta(day)
    date = datetime.datetime.strftime(target_day, '%Y-%m-%d')
    print("############### {} #################".format(date))
    au8 = Source163v2({
        'resource': '163v2',
        'type': 'pk10',
        'area': 'au',
        'url': 'api/complex/selDataByGameIdAndDate?iGameId=33&date={}'.format(date)
    })
    au8.handle()
    time.sleep(0.3)
