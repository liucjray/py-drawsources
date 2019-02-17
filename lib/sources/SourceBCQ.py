import os
import time
import datetime
import requests
import json
import uuid

from settings import env

import cfscrape
from addict import Dict
from drawsources.bcquan.html import *
from lib.IssueInfo import *


class SourceBCQ:
    def __init__(self, settings):
        self.settings = settings
        self.data = []
        self.codes = []
        self.issues = []

    def clean(self):
        self.data = self.get_data()
        self.codes = []
        self.issues = []

    def get_data(self):
        scraper = cfscrape.create_scraper(delay=5)
        payload = self.settings['payload']
        resp = scraper \
            .post("https://www.bcquan.me/api/front/lottery/render" + str(uuid.uuid4()), payload) \
            .content
        resp_dict = json.loads(resp.decode('utf8'))

        issues = []
        for element in resp_dict['lotteryList']:
            issues.append(element['issue'])

        codes = []
        for element in resp_dict['lotteryList']:
            codes.append(element['code'])

        result = dict(zip(issues, codes))
        return result

    def get_codes(self):
        self.codes = list(self.data.values())

    def get_issues(self):
        self.issues = list(self.data.keys())

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
            print('Validate Error!')

    def validate(self):
        return len(self.codes) == len(self.issues) \
               and len(self.codes) > 0 \
               and len(self.issues) > 0

    def handle(self):
        print('Start: %s' % datetime.datetime.now())
        self.clean()
        self.get_issues()
        self.get_codes()
        self.write()
        print('End: %s' % datetime.datetime.now())
