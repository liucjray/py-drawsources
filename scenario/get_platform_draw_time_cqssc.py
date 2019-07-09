from apscheduler.schedulers.blocking import BlockingScheduler

from drawsources.bomaocai.jsons import ssc_cq_bomaocai as ssc_cq_bomaocai
from drawsources.eg.jsons import ssc_cq_eg as ssc_cq_eg
from drawsources.yhz.jsons import ssc_cq_yhz as ssc_cq_yhz
from drawsources.xybet.jsons import ssc_cq_xybet as ssc_cq_xybet

if __name__ == '__main__':
    try:
        scheduler = BlockingScheduler()
        for job in [
            ssc_cq_bomaocai.get_instance(),
            ssc_cq_eg.get_instance(),
            ssc_cq_xybet.get_instance(),
            ssc_cq_yhz.get_instance(),
        ]:
            scheduler.add_job(job.handle, 'interval', seconds=5)

        scheduler.start()
    except Exception as e:
        print(e)
