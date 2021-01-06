import time
import asyncio
from datetime import timedelta, datetime
from lib.sources.SourceLuckyAirShip import *


async def fetch(input_date, input_page):
    print(input_date, input_page)
    s = SourceLuckyAirShip({
        'resource': 'luckyairship',
        'type': 'xyft',
        'area': 'malta',
        'url': 'history.html?date={}&page={}'.format(input_date, input_page)
    })
    s.handle()


loop = asyncio.get_event_loop()
for x in range(0, 365 * 15):
    date = datetime.datetime.strftime(datetime.datetime.now() - timedelta(x), '%Y-%m-%d')
    jobs = []
    for page in range(1, 18):
        jobs.append(fetch(date, page))
    res = loop.run_until_complete(asyncio.wait(jobs))

loop.close()

