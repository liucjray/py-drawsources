import datetime
import requests
from addict import Dict
from lib.IssueInfo import *
from lib.sources.SourceBase import *


class Source88ICP(SourceBase):
    __domain__ = 'https://www.88icp.com/'

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
        http_proxy = {'http': self.get_random_http_proxy()}
        r = requests.get(url, headers=self.settings.headers, proxies=http_proxy).json()
        d = Dict(r)
        self.data = d.Current

    def get_codes(self):
        self.codes.append(self.data.DrawNumbers)

    def get_issues(self):
        self.issues.append(str(self.data.Period))

    def get_infos(self):
        self.infos.append(str(self.data.DrawTime))

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
