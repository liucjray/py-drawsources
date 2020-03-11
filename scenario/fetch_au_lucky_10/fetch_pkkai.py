import time
from lib.sources.Source168 import *

for day in range(0, 30):
    # 不抓今天
    target_day = datetime.now() - timedelta(1) - timedelta(day)
    date = datetime.strftime(target_day, '%Y-%m-%d')
    print("############### {} #################".format(date))
    url = 'klsf/getHistoryLotteryInfo.do?date={}&lotCode=10011'.format(date)
    au8 = Source168({
        'resource': 'pkkai',
        'type': 'pk10',
        'area': 'au',
        'domain': 'https://www.pkkai.com/',
        'url': 'pks/getPksHistoryList.do?date={}&lotCode=10012'.format(date)
    })
    au8.handle()
    time.sleep(0.3)
