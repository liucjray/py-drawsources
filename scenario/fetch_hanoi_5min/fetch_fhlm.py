import time
from lib.sources.SourceFHLM import *

while True:
    print("############### {} #################")
    au8 = SourceFHLM({
        'resource': 'fhlm',
        'type': 'ssc',
        'area': 'hanoi5min',
        'uri': '_data/hn5fc.json'
    })
    au8.handle()
    time.sleep(10)
