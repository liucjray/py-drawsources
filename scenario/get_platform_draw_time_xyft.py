from apscheduler.schedulers.blocking import BlockingScheduler

from drawsources.eg.jsons import xyft_malta_json as malta_xyft_eg
from drawsources.bg.jsons import xyft_malta_json as malta_xyft_bg
from drawsources.xybet.jsons import xyft_malta_xybet as malta_xyft_xybet

if __name__ == '__main__':
    try:
        scheduler = BlockingScheduler()
        for job in [
            malta_xyft_eg.get_instance(),
            malta_xyft_bg.get_instance(),
            malta_xyft_xybet.get_instance(),
        ]:
            scheduler.add_job(job.handle, 'interval', seconds=5)

        scheduler.start()
    except Exception as e:
        print(e)
