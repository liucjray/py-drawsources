from lib.sources.SourceKyzqfqgg import *

s = SourceKyzqfqgg({
    'url': 'auto/history',
    'resource': 'kyzqfqgg',
    'area': 'macau',
    'type': 'marksix',
    'raw_data': {'limit': '1000', 'page': 1}
})
s.handle()
