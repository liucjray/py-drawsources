import time
from lib.sources.Source168 import *

for day in range(0, 30):
    # 不抓今天
    target_day = datetime.now() - timedelta(1) - timedelta(day)
    date = datetime.strftime(target_day, '%Y-%m-%d')
    print("############### {} #################".format(date))
    au8 = Source168({
        'resource': 'mingcai',
        'type': 'pk10',
        'area': 'au',
        'url': 'news/index.php/api/index/new_api?param=pks/getPksHistoryList.do?date={}&lotCode=10012'.format(date),
        'domain': 'https://www.mc185.com/',
    })
    au8.handle()
    time.sleep(0.3)
