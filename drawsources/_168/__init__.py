import os
import requests
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
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
    scheduler = BlockingScheduler()
    # k3
    scheduler.add_job(k3_ah_json.job, 'interval', seconds=10)
    scheduler.add_job(k3_bj_json.job, 'interval', seconds=10)
    scheduler.add_job(k3_gx_json.job, 'interval', seconds=10)
    scheduler.add_job(k3_hb_json.job, 'interval', seconds=10)
    scheduler.add_job(k3_jx_json.job, 'interval', seconds=10)
    # klsf
    scheduler.add_job(klsf_cq_json.job, 'interval', seconds=10)
    scheduler.add_job(klsf_gd_json.job, 'interval', seconds=10)
    # n115
    scheduler.add_job(n115_sd_json.job, 'interval', seconds=10)
    scheduler.add_job(n115_jx_json.job, 'interval', seconds=10)
    scheduler.add_job(n115_gd_json.job, 'interval', seconds=10)
    # pk10
    scheduler.add_job(pk10_bj_json.job, 'interval', seconds=10)
    # ssc
    scheduler.add_job(ssc_cq_json.job, 'interval', seconds=10)
    scheduler.add_job(ssc_xj_json.job, 'interval', seconds=10)

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
