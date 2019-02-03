import os
import requests
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

from settings import env
from lib.IssueInfo import *

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

if __name__ == '__main__':
    retry168 = int(os.getenv("RETRY_168", 10))

    scheduler = BlockingScheduler()

    for job in [
        # k3
        k3_ah_json.job,
        k3_bj_json.job,
        k3_gx_json.job,
        k3_hb_json.job,
        k3_jx_json.job,
        # klsf
        klsf_cq_json.job,
        klsf_gd_json.job,
        # n115
        n115_sd_json.job,
        n115_jx_json.job,
        n115_gd_json.job,
        # pk10
        pk10_bj_json.job,
        # ssc
        ssc_cq_json.job,
        ssc_xj_json.job,
    ]:
        # scheduler.add_job(job, 'interval', seconds=retry168)
        scheduler.add_job(job, 'cron', second='*/5')

    try:
        scheduler.start()
    except ():
        pass
