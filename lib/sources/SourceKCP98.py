import datetime
import requests
from bs4 import BeautifulSoup

from lib.IssueInfo import *


class SourceKCP98:
    __domain__ = 'http://www.98kcp.com/'

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
        url = self.__domain__ + self.settings['uri']
        headers = {'User-Agent': 'Mozilla/5.0'}
        payload = self.settings['payload']

        session = requests.Session()
        r = session.post(url, headers=headers, data=payload).json()

        soup = BeautifulSoup(r['data'], 'html.parser')
        trs = soup.find_all('tr')

        for tr in trs:
            tds = tr.find_all('td')

            # 取得 issues
            issue = '{}-{}'.format(tds[0].text[:8], tds[1].text)
            self.issues.append(issue)

            # 取得 codes
            codes = []
            for code in tds[2].find_all('span', limit=8):
                classes = code.get('class')
                codes.append(classes[0][1:])
            self.codes.append(','.join(codes))

        self.data = dict(zip(self.issues, self.codes))

    def get_codes(self):
        return self.codes

    def get_issues(self):
        return self.issues

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
