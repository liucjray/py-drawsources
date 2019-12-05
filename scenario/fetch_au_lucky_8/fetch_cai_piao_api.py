import time
from datetime import timedelta, datetime
from lib.sources.SourceCaiPiaoAPI import *

for x in range(0, 365):
    for page in range(1, 7):
        date = datetime.strftime(datetime.now() - timedelta(x), '%Y-%m-%d')
        print("############### date:{} / page:{} #################".format(date, page))
        au8 = SourceCaiPiaoAPI({
            'date': date,
            'gameid': 119,
            'pagenum': page,

            'resource': 'caipiaoapi',
            'type': 'kl8',
            'area': 'au',
            'url': 'hall/hallhistory/ajax_detail'
        })
        au8.handle()
        time.sleep(1)
