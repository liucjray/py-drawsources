import time
from datetime import timedelta, datetime
from lib.sources.Source4Dmoon import *

for x in range(0, 10):
    date = datetime.datetime.strftime(datetime.datetime.now() - timedelta(1) - timedelta(x), '%Y-%m-%d')
    print("############### {} #################".format(date))
    s = Source4Dmoon({
        'resource': '4dmoon',
        'type': 'ma',
        'area': 'ma',
        'url': 'past-results/{}'.format(date),
        'date': date
    })
    s.handle()
    # time.sleep(1)
