import datetime
import requests
from addict import Dict
from lib.IssueInfo import *
from pymongo import MongoClient
from lib.formatter.Coder import *


class SourceFHLM:
    __domain__ = 'https://www.fhlm.com/_data/'

    def __init__(self, settings):
        self.settings = Dict(settings)
        self.data = Dict()
        self.codes = []
        self.issues = []
        self.infos = []
        self.prepare_insert_rows = []

    def clean(self):
        self.data = Dict()
        self.codes = []
        self.issues = []
        self.infos = []
        self.prepare_insert_rows = []

    def parse(self):
        url = self.__domain__ + self.settings.url
        r = requests.get(url).json()
        d = Dict(r)
        self.data = d.list

    def get_codes(self):
        for code in self.data:
            formatter = Coder(type=self.settings.type, code=code.code)
            formatter_code = formatter.get_code()
            self.codes.append(','.join(formatter_code))

    def get_issues(self):
        for issue in self.data:
            self.issues.append(issue.issue)

    def get_infos(self):
        for issue in self.data:
            self.infos.append(issue.time)

    def write(self):
        if self.validate():
            self.write_prepare()
            self.write_sqlite3()
            self.write_mongo()
        else:
            print('Validate Error! resource: {} type: {} area: {}'.format(
                self.settings.resource,
                self.settings.type,
                self.settings.area))

    def write_prepare(self):
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
            self.prepare_insert_rows.append(row)

    def write_sqlite3(self):
        # 切分一百組資料為一個 chunk 避免資料量大無法寫入問題
        prepare_insert = self.prepare_insert_rows
        chunks = [prepare_insert[x:x + 100] for x in range(0, len(prepare_insert), 100)]

        for chunk in chunks:
            IssueInfo.insert_many(chunk).on_conflict('ignore').execute()

    def write_mongo(self):
        client = MongoClient(os.getenv("MONGODB_ATLAS_CONNECTION"))
        mongodb_atlas = client.get_database(os.getenv("MONGODB_ATLAS_DB"))
        issue_info = mongodb_atlas.issue_info

        # 切分一百組資料為一個 chunk 避免資料量大無法寫入問題
        prepare_insert = self.prepare_insert_rows
        chunks = [prepare_insert[x:x + 100] for x in range(0, len(prepare_insert), 100)]

        for chunk in chunks:
            try:
                # ordered=False 可於 unique index insert 時跳例外
                issue_info.insert_many(chunk, ordered=False)
            except Exception:
                pass

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
