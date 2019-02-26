import os
import time
from settings import env
from drawsources.ah_upload_cn.html import *

import datetime
import requests
from addict import Dict
from lib.IssueInfo import *


class Source1395P:
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
        url = 'https://www.1395p.com/xync/kaijiang'
        options = ChromeOptions()
        # 设置中文
        options.add_argument('lang=zh_CN.UTF-8')
        # 更换头部
        options.add_argument(
            'user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')

        options.headless = True
        browser = webdriver.Chrome(chrome_driver_path, options=options)

        try:
            delay = 3
            browser.get(url)
            WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#dataContainer')))
            WebDriverWait(browser, delay)

            issues = []
            codes = []
            trs = browser.find_elements_by_css_selector('#dataContainer tbody tr')

            for tr in trs:
                tds = tr.find_elements_by_tag_name('td')
                for td in tds:
                    index = tds.index(td)

                    if index == 0:
                        issue = td.find_element_by_css_selector('.font_gray666').get_attribute('innerHTML')
                        issues.append(issue)

                    if index == 1:
                        code = []
                        spans = td.find_element_by_css_selector('.number_xync').find_elements_by_tag_name('span')
                        for span in spans:
                            code.append(span.get_attribute('class').replace('num', ''))
                        codes.append(','.join(code))

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
