import os
from apscheduler.schedulers.blocking import BlockingScheduler

from drawsources.fhlm.jsons import klsf_cq_json as cq_klsf_fhlm
from drawsources._168.jsons import klsf_cq_json as cq_klsf_168
from drawsources.pk10me.jsons import klsf_cq_json as cq_klsf_pk10me
from drawsources.apilottery.jsons import klsf_cq_json as cq_klsf_apilottery

if __name__ == '__main__':
    try:
        scheduler = BlockingScheduler()
        for job in [
            cq_klsf_fhlm.get_instance(),
            cq_klsf_168.get_instance(),
            cq_klsf_pk10me.get_instance(),
            cq_klsf_apilottery.get_instance(),
        ]:
            scheduler.add_job(job.handle, 'interval', seconds=10)

        scheduler.start()
    except Exception as e:
        print(e)
