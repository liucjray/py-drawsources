from datetime import timedelta, datetime
import requests
from addict import Dict
from lib.IssueInfo import *


class SourceLuckyLottoz:
    __domain__ = 'https://luckylottoz.com/'

    def __init__(self, settings):
        self.settings = Dict(settings)
        self.__domain__ = settings.get('domain', self.__domain__)
        self.data = Dict()
        self.codes = []
        self.issues = []
        self.draw_at = []

    def clean(self):
        self.data = Dict()
        self.codes = []
        self.issues = []
        self.draw_at = []

    def parse(self):
        url = self.__domain__ + self.settings.url
        r = requests.get(url).json()
        d = Dict(r)
        self.data = d.result.data

    def get_codes(self):
        for code in self.data:
            self.codes.append(code.preDrawCode)

    def get_issues(self):
        for issue in self.data:
            self.issues.append(issue.preDrawIssue)

    def get_draw_ats(self):
        for issue in self.data:
            self.draw_at.append(issue.preDrawTime)

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
                    'created_at': str(datetime.now())
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
        print('Start: %s' % datetime.now())
        self.clean()
        self.parse()
        self.get_issues()
        self.get_codes()
        self.get_draw_ats()
        self.write()
        print('End: %s' % datetime.now())
