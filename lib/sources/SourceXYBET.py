import datetime
import requests
from addict import Dict
from lib.IssueInfo import *
from helpers.Common import *


class SourceXYBET:
    __domain__ = 'https://www.xybets0.com/'

    def __init__(self, settings):
        self.settings = Dict(settings)
        self.data = Dict()
        self.issues = []
        self.codes = []
        self.draw_at = []

    def clean(self):
        self.data = Dict()
        self.issues = []
        self.codes = []
        self.draw_at = []

    def parse(self):
        url = self.__domain__ + self.settings.url

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        raw_body = self.settings.raw_body

        r = requests.post(url, headers=headers, data=raw_body).json()
        d = dict_get(r, 'items')
        self.data = d

    def get_issues(self):
        for row in self.data:
            issue = "20" + dict_get(row, 'issue')
            self.issues.append(issue)

    def get_codes(self):
        for row in self.data:
            code = dict_get(row, 'code')
            self.codes.append(code)

    def get_draw_at(self):
        for row in self.data:
            self.draw_at.append(None)

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
                    'draw_at': self.draw_at[index],
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
        self.get_draw_at()
        self.write()
        print('End: %s' % datetime.datetime.now())
