import os
import datetime
from lib.proxy import *


class ProxyFreeProxyLists:
    __domain__ = 'http://www.freeproxylists.net/zh/?c=CA&s=u'

    def __init__(self):
        chrome_driver_path = os.getenv("CHROME_DRIVER_PATH")
        options = ChromeOptions()
        # options.headless = True
        self.browser = webdriver.Chrome(chrome_driver_path, options=options)

    def parse(self):
        url = self.__domain__
        self.browser.get(url)
        WebDriverWait(self.browser, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'DataGrid')))
        proxy_list_table = self.browser.find_elements_by_css_selector('.DataGrid')
        print(proxy_list_table)
        exit()

    def handle(self):
        print('Start: %s' % datetime.datetime.now())
        self.parse()
        print('End: %s' % datetime.datetime.now())


p = ProxyFreeProxyLists()
p.handle()
