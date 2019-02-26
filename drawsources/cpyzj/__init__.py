from apscheduler.schedulers.blocking import BlockingScheduler
from drawsources.cpyzj.html import klsf_cq_html

if __name__ == '__main__':
    try:
        scheduler = BlockingScheduler()
        for job in [
            # klsf
            klsf_cq_html.get_instance(),
        ]:
            scheduler.add_job(job.handle, 'interval', seconds=20)
            # scheduler.add_job(job.handle, 'cron', second='*/5')

        scheduler.start()
    except Exception as e:
        print(e)
