from drawsources._168 import *


def job():
    url = 'https://api.api68.com/lotteryJSFastThree/getJSFastThreeList.do?date=&lotCode=10026'
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
                    'type': 'k3',
                    'area': 'gx',
                    'issue': issue,
                    'code': codes[index],
                    'created_at': datetime.datetime.now()
                }
                data.append(row)
            IssueInfo.insert_many(data).on_conflict('ignore').execute()
    except ():
        print('Exception occurred.')
    finally:
        print('Finish@' + str(datetime.datetime.now()))
