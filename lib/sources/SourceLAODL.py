import datetime
import requests
from addict import Dict
from lib.IssueInfo import *
from bs4 import BeautifulSoup
import re


class SourceLAODL:
    __domain__ = 'https://laodl.com/'

    def __init__(self, settings):
        self.settings = Dict(settings)
        self.data = Dict()
        self.codes = []
        self.issues = []

    def clean(self):
        self.data = Dict()
        self.codes = []
        self.issues = []

    def parse(self):
        url = self.__domain__ + self.settings.url
        r = requests.get(url).text

        # print(r)

        soup = BeautifulSoup(r, 'lxml')
        rows = soup.select('#main .row-main > .col > .col-inner > .row')[1:]

        # print(len(rows))
        # exit()

        issues = []
        codes = []
        for row in rows:
            col_inner = row.select('.col > .col-inner')[0]
            issue = col_inner.find('h4').text
            issue = issue[-10:].split('/')
            issue.reverse()
            issue = '-'.join(issue)
            issues.append(issue)

            row = col_inner.select('.row')[0]
            code = row.find('h2').text
            codes.append(code[-3:] + ',' + code[1:3])

        print(issues, codes)

        self.issues = issues
        self.codes = codes

    def get_issues(self):
        return self.issues

    def get_codes(self):
        return self.codes


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
            print('Validate Error! resource: {} type: {} area: {}'.format(
                self.settings.resource,
                self.settings.type,
                self.settings.area))


    def validate(self):
        print(self.codes, self.issues)
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


s = SourceLAODL({
    'resource': 'laodl',
    'type': 'la',
    'area': 'la',
    'url': 'com/previous-lottery/',
})
s.handle()
