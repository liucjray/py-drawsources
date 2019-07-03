import os
import time
from settings import env
from drawsources.minhngoc.html import *

from bs4 import BeautifulSoup

import datetime
import requests
from addict import Dict
from lib.IssueInfo import *


class SourceMinhngoc:
    def __init__(self, settings):
        self.settings = Dict(settings)
        self.data = []
        self.codes = []
        self.issues = []

    def clean(self):
        self.data = self.get_data()
        self.codes = []
        self.issues = []

    def get_data(self):
        chrome_driver_path = os.getenv("CHROME_DRIVER_PATH")
        options = ChromeOptions()
        options.headless = True
        browser = webdriver.Chrome(chrome_driver_path, options=options)
        url = self.settings.url

        try:
            resp = requests.get(url)
            soup = BeautifulSoup(resp.content, 'html.parser')
            box = soup.select('.box_kqxs')
            box = box[0]

            soup = BeautifulSoup(box, 'html.parser')
            code = soup.select('')

            print(box)
            exit()


            issues = []
            issuesElements = browser.find_elements_by_css_selector('div.box_kqxs:nth(0)')

            print(issuesElements)
            exit()

            for element in issuesElements:
                issues.append(element.get_attribute('innerHTML'))

            # 移除無用資訊
            issues = issues[0:-5]

            # 休息一秒確保號碼全部出現
            time.sleep(1)

            codes = []
            trs = browser.find_elements_by_css_selector('#base-table tbody:nth-child(1) tr')
            for tr in trs:
                issueCodes = []
                tds = tr.find_elements_by_tag_name('td')
                for td in tds[0:3]:
                    code = td.find_element_by_tag_name('span').get_attribute('innerHTML')
                    issueCodes.append(code)
                codes.append(','.join(issueCodes))

            result = dict(zip(issues, codes))
            return result

        finally:
            browser.close()

    def get_codes(self):
        self.codes = list(self.data.values())

    def get_issues(self):
        self.issues = list(self.data.keys())

    def write(self):
        if self.validate():
            prepare_insert = []
            for issue in self.issues:
                index = self.issues.index(issue)
                row = {
                    'resource': self.settings.resource,
                    'type': self.settings.type,
                    'area': self.settings.area,
                    'issue': issue,
                    'code': self.codes[index],
                    'created_at': str(datetime.datetime.now())
                }
                prepare_insert.append(row)

            # 切分一百組資料為一個 chunk 避免資料量大無法寫入問題
            chunks = [prepare_insert[x:x + 100] for x in range(0, len(prepare_insert), 100)]

            for chunk in chunks:
                IssueInfo.insert_many(chunk).on_conflict('ignore').execute()
        else:
            print('Validate Error!')

    def validate(self):
        return len(self.codes) == len(self.issues) \
               and len(self.codes) > 0 \
               and len(self.issues) > 0

    def handle(self):
        print('Start: %s' % datetime.datetime.now())
        self.clean()
        self.get_issues()
        self.get_codes()
        self.write()
        print('End: %s' % datetime.datetime.now())


# minhngoc = SourceMinhngoc({
#     'resource': 'minhngoc',
#     'url': 'https://www.minhngoc.net.vn/ket-qua-xo-so/mien-bac.html',
#     'area': 'mien-bac',
#     'type': 'VN_N',
# })
# minhngoc.handle()
