import time
from lib.sources.SourceCaim8 import *

for day in range(0, 30):
    for page in range(1, 4):
        target_day = datetime.datetime.now() - datetime.timedelta(1) - datetime.timedelta(day)
        date = datetime.datetime.strftime(target_day, '%Y%m%d')
        print("############### {} #################".format(date))
        uri = 'index.php?s=/Abroad/open_ssc/cz/hnwfc/dt/{}/p/{}.html'.format(date, page)
        au8 = SourceCaim8({
            'resource': 'caim8',
            'type': 'ssc',
            'area': 'hanoi5min',
            'uri': uri
        })
        # http://www.caim8.com/index.php?s=/Abroad/open_ssc/cz/hnwfc/dt/20200214/p/2.html
        au8.handle()
        time.sleep(0.3)
