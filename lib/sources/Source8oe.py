import datetime
import requests
from addict import Dict
from lib.IssueInfo import *
from bs4 import BeautifulSoup
import re


class Source8oe:
    __domain__ = 'https://lottery.8oe.com/'

    font_map_code = {
        "&#xe9e7f;": "0",
        "&#xe1720;": "0",
        "&#xf187f;": "0",
        "&#xe824f;": "1",
        "&#xff4e5;": "1",
        "&#xe79f6;": "1",
        "&#xef613;": "2",
        "&#xf38e2;": "2",
        "&#xe36e0;": "2",
        "&#xe4169;": "3",
        "&#xe6834;": "3",
        "&#xf3679;": "3",
        "&#xef804;": "4",
        "&#xf04e5;": "4",
        "&#xef798;": "4",
        "&#xe769e;": "5",
        "&#xe61f5;": "5",
        "&#xe502f;": "5",
        "&#xe785f;": "6",
        "&#xff201;": "6",
        "&#xf0914;": "6",
        "&#xe6839;": "7",
        "&#xe67f3;": "7",
        "&#xf9e58;": "7",
        "&#xee238;": "8",
        "&#xe4501;": "8",
        "&#xe318e;": "8",
        "&#xe4209;": "9",
        "&#xe7650;": "9",
        "&#xe7ef8;": "9",
    }

    def __init__(self, settings):
        self.settings = Dict(settings)
        self.data = Dict()
        self.codes = []
        self.issues = []
        self.infos = []
        self.draw_ats = []

    def clean(self):
        self.data = Dict()
        self.codes = []
        self.issues = []
        self.infos = []
        self.draw_ats = []

    def get_token(self):
        url = self.__domain__ + self.settings.view_url
        r = requests.get(url)
        token = re.findall(r'data\.font = \"(\w{32})\"', r.text)[0]
        return token

    def parse(self):

        token = self.get_token()

        url = self.__domain__ + self.settings.url

        header = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Cookie': 'se=0eef194829e86aa49fc44caf70524d48; __cfduid=d7f653af941d25cede19e5d01928ff22b1582094517; PHPSESSID=s4v0ged1n2d97ie7up30du7qg2; Hm_lvt_8ddac7a4bda5523c8e3763aa582fef10=1582094534; security_session_verify=6f4f6c3ed407c49b83aa672c0a9d7305; Hm_lpvt_8ddac7a4bda5523c8e3763aa582fef10=1582102246',
        }

        form = {
            'limit': '60',
            'date': '2020-02-18',
            'code': '1',
            'path': token,
            'page': '1'
        }
        r = requests.post(url, data=form, headers=header).json()
        d = Dict(r)
        print(r)
        exit()
        self.data = d.data

    def get_font_map_code(self, soup):
        matches = re.findall(r'/(font\d*)/fontello.eot', soup.select('style')[0].text)
        print(matches[0])
        if matches[0] == 'font':
            return self.font_map_code
        elif matches[0] == 'font2':
            return self.font2_map_code
        else:
            print('font map {} not found.'.format(matches[0]))

    def decode_code(self, code_map, code):
        codes = []
        for char in list(code):
            codes.append(str(code_map[char]))
        code = "".join(codes)
        return code

    def get_codes(self):
        return self.codes

    def get_issues(self):
        return self.issues

    def get_draw_ats(self):
        return self.draw_ats

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
                    'draw_at': self.draw_ats[index],
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
        self.get_draw_ats()
        self.write()
        print('End: %s' % datetime.datetime.now())
