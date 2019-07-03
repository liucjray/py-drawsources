import datetime
import requests
import json
from addict import Dict
from lib.IssueInfo import *
from helpers.Common import *


class SourceBBIN:
    __domain__ = ''

    def __init__(self, settings):
        self.settings = Dict(settings)
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
        draw_type = dict_get(self.settings, 'type')
        file_name = "draw-{}.json".format(draw_type)
        resource = dict_get(self.settings, 'resource')
        file_path = os.path.join(os.getenv("STORAGE_PATH"), resource, file_name)

        with open(file_path, encoding='utf-8') as f:
            r = json.load(f)
        d = Dict(r)
        self.data = dict_get(d, 'ret.results', default=None)

    def get_issues(self):
        self.issues = list(self.data.keys())

    def get_codes(self):
        for _ in self.data.values():
            code = []
            for __ in dict_get(_, 'result').values():
                code.append(str(__).zfill(2))
            self.codes.append(','.join(code))

    def get_draw_at(self):
        for _ in self.data.values():
            draw_at = dict_get(_, 'close_timestamp')
            draw_at = datetime.datetime.fromtimestamp(int(draw_at))
            self.draw_at.append(draw_at)

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

