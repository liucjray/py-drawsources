import time
from datetime import timedelta, datetime
from lib.sources.Source168 import *

for x in range(0, 100):
    date = datetime.strftime(datetime.now() - timedelta(1) - timedelta(x), '%Y-%m-%d')
    print("############### {} #################".format(date))
    au8 = Source168({
        'resource': '168',
        'type': 'ssc',
        'area': 'tw',
        'url': 'LotteryPlan/getSscPlanList.do?lotCode=10064&rows=0&date={}'.format(date)
    })
    au8.handle()
    time.sleep(1)
