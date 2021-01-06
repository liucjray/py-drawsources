from apscheduler.schedulers.blocking import BlockingScheduler

from drawsources.thaihuay import thaihuay_thai_html as thaihuay_thai_html

if __name__ == '__main__':
    try:
        scheduler = BlockingScheduler()

        scheduler.add_job(thaihuay_thai_html.get_instance().handle, 'interval', seconds=5*60)

        scheduler.start()
    except Exception as e:
        print(e)
