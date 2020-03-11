import time
from datetime import timedelta, datetime
from lib.sources.Source168 import *

for x in range(0, 100):
    date = datetime.strftime(datetime.now() - timedelta(1) - timedelta(x), '%Y-%m-%d')
    print("############### {} #################".format(date))
    s = Source168({
        'resource': '168',
        'type': 'bingo',
        'area': 'tw',
        'url': 'LuckTwenty/getBaseLuckTwentyList.do?date={}&lotCode=10047'.format(date)
    })
    s.handle()
    time.sleep(1)
