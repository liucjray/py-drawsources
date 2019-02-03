import os
import time
from drawsources._168 import *
from drawsources._168.html import *

chrome_driver_path = os.getenv("CHROME_DRIVER_PATH")
url = 'http://www.1680099.com/beijingsaichePK10.html'

options = ChromeOptions()
options.headless = True
browser = webdriver.Chrome(chrome_driver_path, options=options)
delay = 1
try:
    browser.get(url)
    WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'jrsmhmtjTab')))

    issues = []
    issuesElements = browser.find_elements_by_css_selector('#jrsmhmtjTab td:nth-child(2)')
    for element in issuesElements:
        issues.append(element.get_attribute('innerHTML'))
    # print(issues)

    # 休息一秒確保號碼全部出現
    time.sleep(1)

    codes = []
    codesElements = browser.find_elements_by_css_selector('#jrsmhmtjTab td:nth-child(3)')
    for element in codesElements:
        tmpCodes = element.find_elements_by_css_selector('.imgnumber li i')
        issueCodes = []
        for tmpCode in tmpCodes:
            code = tmpCode.get_attribute('innerHTML')
            issueCodes.append(code)
        codes.append(','.join(issueCodes))
    # print(codes)

    result = dict(zip(issues, codes))
    print(result)

finally:
    browser.close()
