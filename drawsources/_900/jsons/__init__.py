import os
from apscheduler.schedulers.blocking import BlockingScheduler

from drawsources._900.jsons import klsf_cq_json

if __name__ == '__main__':
    try:
        retry168 = int(os.getenv("RETRY_168", 10))
        scheduler = BlockingScheduler()
        for job in [
            klsf_cq_json.get_instance(),
        ]:
            scheduler.add_job(job.handle, 'interval', seconds=retry168)
            # scheduler.add_job(job.handle, 'cron', second='*/5')

        scheduler.start()
    except Exception as e:
        print(e)
