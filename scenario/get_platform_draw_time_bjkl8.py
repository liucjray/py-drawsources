from apscheduler.schedulers.blocking import BlockingScheduler

from drawsources.eg.jsons import kl8_bj_eg as kl8_bj_eg
from drawsources.yhz.jsons import kl8_bj_yhz as kl8_bj_yhz

if __name__ == '__main__':
    try:
        scheduler = BlockingScheduler()
        for job in [
            kl8_bj_eg.get_instance(),
            kl8_bj_yhz.get_instance(),
        ]:
            scheduler.add_job(job.handle, 'interval', seconds=5)

        scheduler.start()
    except Exception as e:
        print(e)
