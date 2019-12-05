import time
from datetime import timedelta, datetime
from lib.sources.Source168 import *

for x in range(0, 100):
    date = datetime.strftime(datetime.now() - timedelta(190) - timedelta(x), '%Y-%m-%d')
    print("############### {} #################".format(date))
    au8 = Source168({
        'resource': '168',
        'type': 'kl8',
        'area': 'au',
        'url': 'klsf/getHistoryLotteryInfo.do?date={}&lotCode=10011'.format(date)
    })
    au8.handle()
    time.sleep(0.3)
