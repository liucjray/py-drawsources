import time
from lib.sources.SourceEG import *

for day in range(0, 30):
    for page in range(1, 29):
        target_day = datetime.datetime.now() - datetime.timedelta(30) - datetime.timedelta(day)
        date = datetime.datetime.strftime(target_day, '%Y-%m-%d')
        print("############### {} #################".format(date))
        url = 'api/GetFcAutoToNum?fc_id=76&page={}&period=&stime={}&etime={}'.format(page, date, date)
        au8 = SourceEG({
            'resource': 'eg',
            'type': 'pk10',
            'area': 'au',
            'url': url
        })
        au8.handle()
        time.sleep(0.3)
