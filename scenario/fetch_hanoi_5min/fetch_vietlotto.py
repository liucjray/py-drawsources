import time
from lib.sources.SourceVietLotto import *

for days in range(0, 30):
    target_day = datetime.datetime.now() - datetime.timedelta(1) - datetime.timedelta(days)
    year = datetime.datetime.strftime(target_day, '%Y')
    month = datetime.datetime.strftime(target_day, '%m')
    day = datetime.datetime.strftime(target_day, '%d')

    for hour in range(0, 24):
        print("############### {}-{}-{} {} #################".format(year, month, day, hour))
        uri = 'analy.php?year={}&month={}&day={}&hour={}'.format(year, month, day, hour)
        s = SourceVietLotto({
            'resource': 'vietlotto',
            'type': 'ssc',
            'area': 'hanoi5min',
            'uri': uri
        })
        s.handle()
        time.sleep(1)
