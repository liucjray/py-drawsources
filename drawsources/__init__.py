import os
from apscheduler.schedulers.blocking import BlockingScheduler

from drawsources.luckyairship.jsons import xyft_malta_json

if __name__ == '__main__':
    try:
        scheduler = BlockingScheduler()
        for job in [
            xyft_malta_json.get_instance(),
        ]:
            scheduler.add_job(job.handle, 'interval', seconds=5)

        scheduler.start()
    except Exception as e:
        print(e)
