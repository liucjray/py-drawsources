import time
from lib.sources.SourceManyCai import *

while True:
    print("############### {} #################")
    s = SourceManyCai({
        'resource': 'manycai',
        'type': 'ssc',
        'area': 'hanoi5min',
        'uri': 'Issue/ajax_history',
        'lotterycode': 'HN300',
        'lotteryname': 'HN300',
    })
    s.handle()
    time.sleep(10)
