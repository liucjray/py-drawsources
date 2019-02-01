import os
from gemtech import *

chrome_driver_path = os.getenv("CHROME_DRIVER_PATH")
url = 'https://1122008.cn/history/commsscSelf/cqssc'

options = ChromeOptions()
options.headless = True
browser = webdriver.Chrome(chrome_driver_path, options=options)
delay = 1
try:
    browser.get(url)
    WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.lot-history-table table')))
    wait = WebDriverWait(browser, delay)

    issues = []
    issuesElements = browser.find_elements_by_css_selector('.lot-history-table td:nth-child(2)')
    for element in issuesElements:
        issues.append(element.get_attribute('innerHTML'))
    # 移除標題欄位資訊
    del(issues[0])
    # print(issues)

    codes = []
    codesElements = browser.find_elements_by_css_selector('.lot-history-table td:nth-child(3)')
    for element in codesElements:
        tmpCodes = element.find_elements_by_css_selector('.lot-history-table-number .code-result')
        issueCodes = []
        for tmpCode in tmpCodes:
            issueCodes.append(tmpCode.get_attribute('innerHTML'))
        codes.append(','.join(issueCodes))
    # 移除標題欄位資訊
    del (codes[0])
    # print(codes)

    result = dict(zip(issues, codes))
    print(result)

finally:
    browser.close()
