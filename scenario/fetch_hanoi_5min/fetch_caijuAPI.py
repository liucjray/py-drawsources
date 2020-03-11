import time
from lib.sources.SourceCaiJuAPI import *

for day in range(0, 30):
    target_day = datetime.datetime.now() - datetime.timedelta(10) - datetime.timedelta(day)
    date = datetime.datetime.strftime(target_day, '%Y-%m-%d')
    print("############### {} #################".format(date))
    au8 = SourceCaiJuAPI({
        'resource': 'caijuapi',
        'type': 'ssc',
        'area': 'hanoi5min',
        'uri': 'api/get_histcodes?date={}&code=viffc5'.format(date),
        'view_uri': 'history/viffc5'
    })
    au8.handle()
    time.sleep(30)
