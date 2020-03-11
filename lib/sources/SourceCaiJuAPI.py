import datetime
import requests
import re
from addict import Dict

from lib.IssueInfo import *


class SourceCaiJuAPI:
    __domain__ = 'https://www.caijuapi.com/'

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
        token, view_url = self.get_token()

        url = self.__domain__ + self.settings['uri'] + '&path=' + token

        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Referer': view_url,
            'x-requested-with': 'XMLHttpRequest',
        }
        r = requests.get(url, headers=headers).json()

        d = Dict(r)
        self.data = d.item

    def get_token(self):
        url = self.__domain__ + self.settings['view_uri']
        r = requests.get(url)
        token = re.findall(r'path\:\"(\w{16})\"', r.text)[0]
        return token, url

    def get_codes(self):
        for row in self.data:
            self.codes.append(row.code)

    def get_issues(self):
        for row in self.data:
            self.issues.append(row.issue)

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
