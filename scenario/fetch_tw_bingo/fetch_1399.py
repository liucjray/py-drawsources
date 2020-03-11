import time
from datetime import timedelta, datetime
from lib.sources.Source1399 import *

for x in range(0, 100):
    date = datetime.datetime.strftime(datetime.datetime.now() - timedelta(1) - timedelta(x), '%Y-%m-%d')
    print("############### {} #################".format(date))
    s = Source1399({
        'resource': '1399',
        'type': 'bingo',
        'area': 'tw',
        'url': 'issuehistory/historyList?lotteryCode=taiwan&issue_no=0&date={}&pageIndex=1&pageSize=100'.format(date)
    })
    s.handle()
    time.sleep(1)
