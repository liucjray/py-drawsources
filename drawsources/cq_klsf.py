import os
from apscheduler.schedulers.blocking import BlockingScheduler

from drawsources.fhlm.jsons import klsf_cq_json as cq_klsf_fhlm
from drawsources._168.jsons import klsf_cq_json as cq_klsf_168
from drawsources.pk10me.jsons import klsf_cq_json as cq_klsf_pk10me
from drawsources.apilottery.jsons import klsf_cq_json as cq_klsf_apilottery
from drawsources._88icp.jsons import klsf_cq_json as cq_klsf_88icp
from drawsources._1396j.jsons import klsf_cq_json as cq_klsf_1396j

if __name__ == '__main__':
    try:
        scheduler = BlockingScheduler()
        for job in [
            cq_klsf_fhlm.get_instance(),
            cq_klsf_168.get_instance(),
            cq_klsf_pk10me.get_instance(),
            cq_klsf_apilottery.get_instance(),
            cq_klsf_88icp.get_instance(),
            cq_klsf_1396j.get_instance(),
        ]:
            scheduler.add_job(job.handle, 'interval', seconds=15)

        scheduler.start()
    except Exception as e:
        print(e)
