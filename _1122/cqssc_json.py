import requests

url = 'https://api.950021.com/lottery-client-api/sscs/10101/history?date='
headers = {"Referer": "https://1122008.cn/history/commsscSelf/cqssc", "X-Requested-With": "XMLHttpRequest"}

try:
    print('Start')
    r = requests.get(url, headers=headers)
    j = r.json()
    data = j['content']

    issues = []
    for issue in data:
        issues.append(issue['preDrawIssue'])
    # print(issues)

    codes = []
    for code in data:
        codeFormat = ','.join(str(c) for c in code['preDrawCode'])
        codes.append(codeFormat)
    # print(codes)

    result = dict(zip(issues, codes))
    print(result)

finally:
    print('Finished')
