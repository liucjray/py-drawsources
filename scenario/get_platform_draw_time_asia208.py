from apscheduler.schedulers.blocking import BlockingScheduler

from drawsources._163.jsons import klsf_asia_json as klsf_asia_json
from drawsources._163.jsons import klsf_asia_json as klsf_asia_json2
from drawsources._163.jsons import klsf_asia_json as klsf_asia_json3

if __name__ == '__main__':
    try:
        scheduler = BlockingScheduler()

        scheduler.add_job(klsf_asia_json.get_instance().handle, 'interval', seconds=6)
        scheduler.add_job(klsf_asia_json2.get_instance().handle, 'interval', seconds=6, jitter=2)
        scheduler.add_job(klsf_asia_json3.get_instance().handle, 'interval', seconds=6, jitter=2)

        scheduler.start()
    except Exception as e:
        print(e)
