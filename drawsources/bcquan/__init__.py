from apscheduler.schedulers.blocking import BlockingScheduler
from drawsources.bcquan.html import k3_js_html
from drawsources.bcquan.html import n115_sd_html
from drawsources.bcquan.html import pk10_bj_html
from drawsources.bcquan.html import ssc_cq_html
from drawsources.bcquan.html import ssc_tj_html
from drawsources.bcquan.html import ssc_xj_html

if __name__ == '__main__':
    try:
        scheduler = BlockingScheduler()
        for job in [
            k3_js_html.get_instance(),
            n115_sd_html.get_instance(),
            pk10_bj_html.get_instance(),
            ssc_cq_html.get_instance(),
            ssc_tj_html.get_instance(),
            ssc_xj_html.get_instance(),
        ]:
            scheduler.add_job(job.handle, 'interval', seconds=15)

        scheduler.start()
    except Exception as e:
        print(e)
