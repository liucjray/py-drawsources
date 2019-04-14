import os
from apscheduler.schedulers.blocking import BlockingScheduler

from drawsources.bclc.jsons import keno_ca_json

if __name__ == '__main__':
    try:
        retry = 5
        scheduler = BlockingScheduler()
        for job in [
            keno_ca_json.get_instance(),
        ]:
            scheduler.add_job(job.handle, 'interval', seconds=retry)
            # scheduler.add_job(job.handle, 'cron', second='*/5')

        scheduler.start()
    except Exception as e:
        print(e)
