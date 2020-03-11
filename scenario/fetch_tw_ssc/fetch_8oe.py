import time
from datetime import timedelta, datetime
from lib.sources.Source8oe import *

for x in range(0, 30):
    date = datetime.datetime.strftime(datetime.datetime.now() - timedelta(1) - timedelta(x), '%Y-%m-%d')
    print("############### {} #################".format(date))
    s = Source8oe({
        'resource': '8oe',
        'type': 'ssc',
        'area': 'tw',
        'url': 'index/get_histcodes1128.html'.format(date),
        'view_url': 'history/twssc.html'
    })
    s.handle()
    time.sleep(1)
