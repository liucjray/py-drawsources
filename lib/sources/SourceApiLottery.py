import datetime
import requests
from addict import Dict
from lib.IssueInfo import *


class SourceApiLottery:
    __domain__ = 'http://www.apilottery.com/'

    def __init__(self, settings):
        self.settings = Dict(settings)
        self.data = Dict()
        self.codes = []
        self.issues = []
        self.infos = []

    def clean(self):
        self.data = Dict()
        self.codes = []
        self.issues = []
        self.infos = []

    def parse(self):
        url = self.__domain__ + self.settings.url
        r = requests.get(url, headers=self.settings.headers).json()
        d = Dict(r)
        self.data = d.data

    def get_codes(self):
        for code in self.data:
            self.codes.append(code.opencode)

    def get_issues(self):
        for issue in self.data:
            self.issues.append(issue.expect)

    def get_infos(self):
        for info in self.data:
            self.infos.append(info.opentime)

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
                    'info': self.infos[index],
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
        self.get_infos()
        self.write()
        print('End: %s' % datetime.datetime.now())
