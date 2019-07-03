from apscheduler.schedulers.blocking import BlockingScheduler
from drawsources.ah_upload_cn.html import k3_ah_html

if __name__ == '__main__':
    try:
        scheduler = BlockingScheduler()
        for job in [
            # k3
            k3_ah_html.get_instance(),
        ]:
            scheduler.add_job(job.handle, 'interval', seconds=10)
            # scheduler.add_job(job.handle, 'cron', second='*/5')

        scheduler.start()
    except Exception as e:
        print(e)
