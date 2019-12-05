from dateutil.parser import *
import requests
from bs4 import BeautifulSoup
from lib.IssueInfo import *
import re
from datetime import datetime, timedelta
import time


class SourceAuLuckyLottery8:
    __domain__ = 'https://www.auluckylottery.com/results/lucky-ball-8'

    def __init__(self, settings):
        self.settings = settings
        self.data = {}
        self.codes = []
        self.issues = []
        self.draw_at = []

    def clean(self):
        self.data = {}
        self.codes = []
        self.issues = []
        self.draw_at = []

    def parse(self):
        url = self.__domain__ + self.settings['url']

        r = requests.get(url, verify=False)

        soup = BeautifulSoup(r.text, 'lxml')

        selector = "div.past_numbers"
        divs = soup.select(selector)

        for div in divs:
            # pn_font1 = issue
            issue_html = div.select('div.pn_font1')
            pattern = re.compile(r'(\d{8})')
            issue = pattern.findall(issue_html[0].text)[0]

            # draw_at
            draw_at_html = str(issue_html[0].text).strip().split('(ACST)')[0]
            draw_at_parsed = parse(draw_at_html)
            draw_at = draw_at_parsed.strftime('%Y-%m-%d %H:%M:%S')

            # p_number_ball = code
            codes_html = div.select('div.p_number_ball > div')
            codes = []
            for code_html in codes_html:
                code = code_html.text.zfill(2)
                codes.append(code)

            self.issues.append(issue)
            self.codes.append(','.join(codes))
            self.draw_at.append(draw_at)

        self.data = dict(zip(self.issues, self.codes))

    def get_codes(self):
        return self.codes

    def get_issues(self):
        return self.issues

    def get_draw_at(self):
        return self.draw_at

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
        return len(self.codes) == len(self.issues) == len(self.draw_at) \
               and len(self.codes) > 0 \
               and len(self.issues) > 0 \
               and len(self.draw_at) > 0

    def handle(self):
        print('Start: %s' % datetime.now())
        self.clean()
        self.parse()
        self.get_issues()
        self.get_codes()
        self.write()
        print('End: %s' % datetime.now())
