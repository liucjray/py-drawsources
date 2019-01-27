import requests

url = 'https://api.api68.com/pks/getPksHistoryList.do?lotCode=10001'

try:
    print('Start')
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

    result = dict(zip(issues, codes))
    print(result)

finally:
    print('Finished')
