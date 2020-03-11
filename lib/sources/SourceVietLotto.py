import datetime
import requests
import re
from bs4 import BeautifulSoup
from lib.sources.SourceBase import *

from lib.IssueInfo import *


class SourceVietLotto(SourceBase):
    __domain__ = 'https://draw.vietlotto.org/'

    def __init__(self, settings):
        self.settings = settings
        self.https_proxy = {}
        self.data = {}
        self.codes = []
        self.issues = []
        self.draw_ats = []

    def clean(self):
        self.data = {}
        self.https_proxy = {}
        self.codes = []
        self.issues = []
        self.draw_ats = []

    def parse(self):
        url = self.__domain__ + self.settings['uri']
        print(url)

        proxy = None
        header = {
            'cookie': 'incap_ses_930_2173795=odFKE3sCxCyZBIQGKgfoDFCdS14AAAAAPjl0qm/tg8C8cTEjaLBdIw==',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
        }

        while True:
            proxy = self.get_random_http_proxy()
            self.https_proxy = {'http': proxy}
            r1 = requests.get(url, proxies=self.https_proxy, headers=header, timeout=2)
            if r1.status_code == 200:
                break

        self.https_proxy = {'http': proxy}
        r = requests.get(url, proxies=self.https_proxy, headers=header, timeout=2)

        soup = BeautifulSoup(r.text, 'lxml')
        items = soup.select('.list_right_box > .item')

        for item in items:
            draw_at = re.search(r'(\d{4}\-\d{2}\-\d{2}\s\d{2}\:\d{2}\:\d{2})', item.select('.time')[0].text)[0]
            self.draw_ats.append(draw_at)

            issue = re.search(r'(\d{8}\-\d{1,3})', item.select('.date')[0].text)[0]
            (date, issue) = issue.split('-')
            issue = "{}-{}".format(date, str(issue).zfill(3))
            self.issues.append(issue)

            codes = []
            for em in item.select('.ball > em'):
                codes.append(em.text)
            self.codes.append(','.join(codes))

        self.data = dict(zip(self.issues, self.codes))

    def get_codes(self):
        return self.codes

    def get_issues(self):
        return self.issues

    def get_draw_ats(self):
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
                    'draw_at': self.draw_ats[index],
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
        return len(self.codes) == len(self.issues) \
               and len(self.codes) > 0 \
               and len(self.issues) > 0

    def handle(self):
        print('Start: %s' % datetime.datetime.now())
        self.clean()
        self.parse()
        self.get_issues()
        self.get_codes()
        self.get_draw_ats()
        self.write()
        print('End: %s' % datetime.datetime.now())
