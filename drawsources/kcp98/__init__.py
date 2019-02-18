from apscheduler.schedulers.blocking import BlockingScheduler
from drawsources.kcp98.jsons import klsf_cq_json

if __name__ == '__main__':
    try:
        scheduler = BlockingScheduler()
        for job in [
            klsf_cq_json.get_instance(),
        ]:
            scheduler.add_job(job.handle, 'interval', seconds=10)

        scheduler.start()
    except Exception as e:
        print(e)
