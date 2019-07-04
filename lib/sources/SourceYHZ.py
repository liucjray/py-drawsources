import datetime
import requests
from bs4 import BeautifulSoup

from lib.IssueInfo import *
import re


class SourceYHZ:
    __domain__ = 'http://www.1hz878.com/'

    def __init__(self, settings):
        self.settings = settings
        self.data = {}
        self.codes = []
        self.issues = []

    def clean(self):
        self.data = {}
        self.codes = []
        self.issues = []

    def parse(self):
        url = self.__domain__ + self.settings['url']

        r = requests.get(url, verify=False)

        soup = BeautifulSoup(r.text, 'lxml')

        selector = "table#codeTable tr"
        trs = soup.select(selector)

        for tr in trs:
            if trs.index(tr) == 0 or trs.index(tr) == 1:
                continue

            # issues
            for issue in tr.find_all("td", class_="title"):
                self.issues.append(issue.text)

            # codes
            codes = []
            for code in tr.find_all("td", class_="code"):
                codes.append(code.text)
            self.codes.append(','.join(codes))

        self.data = dict(zip(self.issues, self.codes))

    def get_codes(self):
        return self.codes

    def get_issues(self):
        return self.issues

    def write(self):
        if self.validate():
            prepare_insert = []
            for issue in self.issues:
                index = self.issues.index(issue)
                row = {
                    'resource': self.settings['resource'],
                    'type': self.settings['type'],
                    'area': self.settings['area'],
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
            print('Validate Error! resource: {} type: {} area: {}'.format(
                self.settings.resource,
                self.settings.type,
                self.settings.area))

    def validate(self):
        return len(self.codes) == len(self.issues) \
               and len(self.codes) > 0 \
               and len(self.issues) > 0

    def handle(self):
        print('Start: %s' % datetime.datetime.now())
        self.clean()
        self.parse()
        self.get_issues()
        self.get_codes()
        self.write()
        print('End: %s' % datetime.datetime.now())


# s = SourceYHZ({
#     'url': '?controller=game&action=bonuscode&lotteryid=20&issuecount=30',
#     'resource': 'yhz',
#     'area': 'bj',
#     'type': 'pk10',
# })
# s.handle()
