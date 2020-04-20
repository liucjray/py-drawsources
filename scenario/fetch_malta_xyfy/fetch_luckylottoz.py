import time
from lib.sources.SourceLuckyLottoz import *

for x in range(0, 30):
    date = datetime.strftime(datetime.now() - timedelta(x), '%Y-%m-%d')
    print("############### date:{} #################".format(date))
    s = SourceLuckyLottoz({
        'url': 'api/result/getPksHistoryList.do?lotCode=10057&date={}' . format(date),
        'resource': 'luckylottoz',
        'area': 'malta',
        'type': 'xyft',
    })
    s.handle()
