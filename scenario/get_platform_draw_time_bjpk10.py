from apscheduler.schedulers.blocking import BlockingScheduler

from drawsources.bomaocai.jsons import pk10_bj_bomaocai as pk10_bj_bomaocai
from drawsources.yhz.jsons import pk10_bj_yhz as pk10_bj_yhz
from drawsources.xybet.jsons import pk10_bj_xybet as pk10_bj_xybet

if __name__ == '__main__':
    try:
        scheduler = BlockingScheduler()
        for job in [
            pk10_bj_bomaocai.get_instance(),
            pk10_bj_yhz.get_instance(),
            pk10_bj_xybet.get_instance(),
        ]:
            scheduler.add_job(job.handle, 'interval', seconds=5)

        scheduler.start()
    except Exception as e:
        print(e)
