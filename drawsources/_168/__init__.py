import os
from apscheduler.schedulers.blocking import BlockingScheduler

from drawsources._168.jsons import k3_ah_json
from drawsources._168.jsons import k3_bj_json
from drawsources._168.jsons import k3_gx_json
from drawsources._168.jsons import k3_hb_json
from drawsources._168.jsons import k3_jx_json
from drawsources._168.jsons import klsf_cq_json
from drawsources._168.jsons import klsf_gd_json
from drawsources._168.jsons import n115_gd_json
from drawsources._168.jsons import n115_jx_json
from drawsources._168.jsons import n115_sd_json
from drawsources._168.jsons import pk10_bj_json
from drawsources._168.jsons import ssc_xj_json
from drawsources._168.jsons import ssc_cq_json
from drawsources._168.jsons import ssc_tj_json

if __name__ == '__main__':
    try:
        retry168 = int(os.getenv("RETRY_168", 10))
        scheduler = BlockingScheduler()
        for job in [
            # k3
            # k3_ah_json.get_instance(),
            # k3_bj_json.get_instance(),
            # k3_gx_json.get_instance(),
            # k3_hb_json.get_instance(),
            # k3_jx_json.get_instance(),
            # klsf
            klsf_cq_json.get_instance(),
            # klsf_gd_json.get_instance(),
            # # n115
            # n115_sd_json.get_instance(),
            # n115_jx_json.get_instance(),
            # n115_gd_json.get_instance(),
            # # pk10
            # pk10_bj_json.get_instance(),
            # # ssc
            # ssc_cq_json.get_instance(),
            # ssc_xj_json.get_instance(),
            # ssc_tj_json.get_instance(),
        ]:
            scheduler.add_job(job.handle, 'interval', seconds=retry168)
            # scheduler.add_job(job.handle, 'cron', second='*/5')

        scheduler.start()
    except Exception as e:
        print(e)
