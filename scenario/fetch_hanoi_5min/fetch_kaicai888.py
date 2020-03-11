import time
from lib.sources.SourceKaiCai888 import *

while True:
    print("############### {} #################")
    au8 = SourceKaiCai888({
        'resource': 'kaicai888',
        'type': 'ssc',
        'area': 'hanoi5min',
        'uri': 'api/lottery/list?lottery=t1s300&num=1&pageSize=300'
    })
    au8.handle()
    time.sleep(10)
