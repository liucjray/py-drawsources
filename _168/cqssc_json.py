import os
import requests
import datetime
import schedule
from _168 import *
from lib.IssueInfo import *

url = 'https://api.api68.com/CQShiCai/getBaseCQShiCaiList.do?lotCode=10002'

db_name = os.getenv("STORAGE_PATH") + 'cqssc.db'


def job():
    try:
        print('Start@' + str(datetime.datetime.now()))
        r = requests.get(url)
        j = r.json()
        data = j['result']['data']

        issues = []
        for issue in data:
            issues.append(issue['preDrawIssue'])
        # print(issues)

        codes = []
        for code in data:
            codes.append(code['preDrawCode'])
        # print(codes)

        if len(issues) == len(codes):
            data = []
            for issue in issues:
                index = issues.index(issue)
                row = {
                    'resource': '168',
                    'issue': issue,
                    'code': codes[index],
                    'created_at': datetime.datetime.now()
                }
                data.append(row)
            deferred_db.init(db_name)
            IssueInfo.insert_many(data).execute()

    finally:
        print('Finish@' + str(datetime.datetime.now()))


schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
