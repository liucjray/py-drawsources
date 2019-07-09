import datetime
import requests
from bs4 import BeautifulSoup

from lib.IssueInfo import *
from lib.sources.SourceBase import *
from lib.sources.SourceYHZSSC import *
from lib.sources.SourceYHZPK10 import *
from lib.sources.SourceYHZKL8 import *


class SourceYHZ(SourceBase):
    __domain__ = 'http://www.1hz878.com/'

    def __init__(self, settings):
        self.settings = settings
        self.data = {}
        self.codes = []
        self.issues = []
        self.https_proxy = {}
        self.parser_map = {
            'cqssc': SourceYHZSSC(),
            'bjpk10': SourceYHZPK10(),
            'bjkl8': SourceYHZKL8(),
        }
        self.parser = None

    def clean(self):
        self.data = {}
        self.codes = []
        self.issues = []

    def parse(self):
        url = self.__domain__ + self.settings['url']
        self.https_proxy = {'https': self.get_random_proxy(self.get_proxy_by_country('singapore'))}

        try:
            r = requests.get(url, verify=False, proxies=self.https_proxy)
            area_type = self.settings['area'] + self.settings['type']
            self.data = self.parser_map[area_type].parse(r)
        except Exception as e:
            print('Exception error: ' + str(e))

    def get_issues(self):
        self.issues = list(self.data.keys())

    def get_codes(self):
        self.codes = list(self.data.values())

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
                self.settings['resource'],
                self.settings['type'],
                self.settings['area']))

    def validate(self):
        # print(len(self.codes) == len(self.issues), len(self.codes), len(self.issues))
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


s = SourceYHZ({
    'url': '?controller=game&action=bonuscode&lotteryid=9&issuecount=30',
    'resource': 'yhz',
    'area': 'bj',
    'type': 'kl8',
})
s.handle()
