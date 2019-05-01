from apscheduler.schedulers.blocking import BlockingScheduler

from drawsources.fhlm.jsons import klsf_cq_json
from drawsources.fhlm.jsons import xyft_malta_json
from drawsources.fhlm.jsons import ssc_cq_json
from drawsources.fhlm.jsons import pk10_bj_json
from drawsources.fhlm.jsons import kl8_bj_json
from drawsources.fhlm.jsons import k3_bj_json
from drawsources.fhlm.jsons import n115_gd_json
from drawsources.fhlm.jsons import marksix_hk_json

if __name__ == '__main__':
    try:
        scheduler = BlockingScheduler()
        for job in [
            klsf_cq_json.get_instance(),
            xyft_malta_json.get_instance(),
            ssc_cq_json.get_instance(),
            pk10_bj_json.get_instance(),
            kl8_bj_json.get_instance(),
            k3_bj_json.get_instance(),
            n115_gd_json.get_instance(),
            marksix_hk_json.get_instance(),
        ]:
            scheduler.add_job(job.handle, 'interval', seconds=10)

        scheduler.start()
    except Exception as e:
        print(e)
