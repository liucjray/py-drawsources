import time
from lib.sources.SourceCaiPiaoAPIv3 import *

for day in range(0, 30):
    target_day = datetime.now() - timedelta(1) - timedelta(day)
    date = datetime.strftime(target_day, '%Y-%m-%d')
    print("############### date={} #################".format(date))
    s = SourceCaiPiaoAPIv3({
        'resource': 'caipiaoapiv3',
        'type': 'bingo',
        'area': 'tw',
        'uri': 'hall/hallajax/getLotteryList',
        'get_token_url': 'https://www.caipiaoapi.com/hall/halllucky/hist/twbg',
        'lotKey': 'twbg',
        'date': date,
    })
    s.handle()
    time.sleep(0.3)
