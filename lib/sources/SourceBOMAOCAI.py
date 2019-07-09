import datetime
import requests
from bs4 import BeautifulSoup

from lib.IssueInfo import *
import re


class SourceBOMAOCAI:
    __domain__ = 'https://www.bomaocai.com/'

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

        lott_postion_map = {
            'cq:ssc': 2,
            'bj:pk10': 3,
        }

        position = "{}:{}".format(self.settings['area'], self.settings['type'])
        selector = "div.b > ul:nth-of-type({}) li".format(lott_postion_map[position])
        lis = soup.select(selector)

        for li in lis:
            # issue
            if lis.index(li) == 1:
                issue = re.sub("[^\d]+", "", li.text)
                self.issues.append(issue)

            # code
            if lis.index(li) == 3:
                codes = []
                for code in li.find_all("span"):
                    codes.append(code.text.zfill(2))
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


s = SourceBOMAOCAI({
    'url': 'issueannoucement',
    'resource': 'bomaocai',
    'area': 'cq',
    'type': 'ssc',
})
s.handle()
