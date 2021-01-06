from lib.sources.SourceMacauJC import *

s = SourceMacauJC({
    'url': 'api/HistoryOpenInfo',
    'resource': 'macaujc',
    'area': 'macau',
    'type': 'marksix',
    'raw_data': {"lotteryId": 2032, "issueNum": "2020-06-23"}
})
s.handle()
