import time
from lib.sources.SourceCaiPiaoAPIv2 import *

for day in range(0, 30):
    for page in range(1, 7):
        target_day = datetime.now() - timedelta(1) - timedelta(day)
        date = datetime.strftime(target_day, '%Y-%m-%d')
        print("############### date={}, page={} #################".format(date, page))
        au8 = SourceCaiPiaoAPIv2({
            'resource': 'caipiaoapiv2',
            'type': 'ssc',
            'area': 'au',
            'url': 'hall/hallhistory/ajax_detail',
            'gameid': '99',
            'date': date,
            'pagenum': page
        })
        au8.handle()
        time.sleep(0.3)
