from lib.sources.SourceMacauLottery import *

s = SourceMacauLottery({
    'url': 'lhcwebsite/getNearLottory.do',
    'resource': 'macaulottery',
    'area': 'macau',
    'type': 'marksix',
    'raw_data': {'name': 'AMLHC', 'count': 50}
})
s.handle()
